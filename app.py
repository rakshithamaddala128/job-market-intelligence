
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Job Market Intelligence",
    page_icon="📊",
    layout="wide"
)

DATA = Path("data/processed")

st.title("📊 Job Market Intelligence & Skill Gap Analyzer")
st.markdown(
    "### Comparative Analysis of Indian and Global IT Job Markets"
)


# LOAD DATA
@st.cache_data
def load_data():
    filenames = {
        "india_jobs": "india_jobs_classified.csv",
        "global_jobs": "global_jobs_classified.csv",
        "india_skills": "india_skills_extracted.csv",
        "global_skills": "global_skills_extracted.csv",
        "comparison": "india_global_skill_comparison.csv",
        "categories": "india_global_category_comparison.csv",
        "common": "common_skills.csv",
        "specific": "market_specific_skills.csv"
    }

    result = {}

    for key, filename in filenames.items():
        path = DATA / filename

        if not path.exists():
            raise FileNotFoundError(f"Missing file: {path}")

        result[key] = pd.read_csv(path)

    return result


try:
    data = load_data()
except Exception as error:
    st.error(f"Data loading error: {error}")
    st.stop()


india_jobs = data["india_jobs"]
global_jobs = data["global_jobs"]
india_skills = data["india_skills"]
global_skills = data["global_skills"]
comparison = data["comparison"]
categories = data["categories"]
common = data["common"]
specific = data["specific"]


# SIDEBAR
st.sidebar.title("Navigation")
st.sidebar.write("Explore the job market datasets.")
st.sidebar.markdown("---")
st.sidebar.write("**India dataset:** 2019")
st.sidebar.write("**Global dataset:** 2023–2024")


# OVERVIEW METRICS
india_total = india_jobs["uniq_id"].nunique()
global_total = global_jobs["job_id"].nunique()

india_covered = india_skills["uniq_id"].nunique()
global_covered = global_skills["job_id"].nunique()

india_coverage = india_covered / india_total * 100
global_coverage = global_covered / global_total * 100

st.header("Market Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Indian Job Postings", f"{india_total:,}")
c2.metric("Global Job Postings", f"{global_total:,}")
c3.metric("India Skill Coverage", f"{india_coverage:.2f}%")
c4.metric("Global Skill Coverage", f"{global_coverage:.2f}%")

st.markdown("---")


# DASHBOARD TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Market Overview",
    "Skill Analysis",
    "Category Comparison",
    "Market Opportunities",
    "India Job Analysis"
])


# TAB 1: MARKET OVERVIEW
with tab1:

    st.subheader("Job Role Distribution")

    india_roles = (
        india_jobs["role_category_standard"]
        .value_counts()
        .rename_axis("Role")
        .reset_index(name="Job Count")
    )
    india_roles["Market"] = "India"

    global_roles = (
        global_jobs["role_category"]
        .value_counts()
        .rename_axis("Role")
        .reset_index(name="Job Count")
    )
    global_roles["Market"] = "Global"

    role_data = pd.concat(
        [india_roles, global_roles],
        ignore_index=True
    )

    fig = px.bar(
        role_data,
        x="Role",
        y="Job Count",
        color="Market",
        barmode="group",
        title="Job Distribution by Role Category"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Skill Extraction Coverage")

    coverage = pd.DataFrame({
        "Market": ["India", "Global"],
        "Jobs With Detected Skills": [
            india_covered, global_covered
        ],
        "Jobs Without Detected Skills": [
            india_total - india_covered,
            global_total - global_covered
        ]
    })

    coverage_long = coverage.melt(
        id_vars="Market",
        var_name="Skill Detection",
        value_name="Jobs"
    )

    fig = px.bar(
        coverage_long,
        x="Market",
        y="Jobs",
        color="Skill Detection",
        barmode="stack",
        title="Skill Extraction Coverage"
    )

    st.plotly_chart(fig, use_container_width=True)


# TAB 2: SKILL ANALYSIS
with tab2:

    st.subheader("Top Skills Across Markets")

    market = st.selectbox(
        "Select Market",
        ["India", "Global"]
    )

    top_n = st.slider(
        "Number of Skills",
        5, 30, 15
    )

    demand_column = (
        "india_demand_pct"
        if market == "India"
        else "global_demand_pct"
    )

    top_skills = comparison.nlargest(
        top_n, demand_column
    )

    fig = px.bar(
        top_skills.sort_values(demand_column),
        x=demand_column,
        y="skill_name",
        orientation="h",
        title=f"Top {top_n} Skills in {market}",
        labels={
            demand_column: "Job Demand (%)",
            "skill_name": "Skill"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("India vs Global Skill Demand")

    selected = comparison.nlargest(
        15, "india_demand_pct"
    )

    selected = selected.melt(
        id_vars="skill_name",
        value_vars=[
            "india_demand_pct",
            "global_demand_pct"
        ],
        var_name="Market",
        value_name="Demand (%)"
    )

    selected["Market"] = selected["Market"].map({
        "india_demand_pct": "India",
        "global_demand_pct": "Global"
    })

    fig = px.bar(
        selected,
        x="skill_name",
        y="Demand (%)",
        color="Market",
        barmode="group",
        title="Skill Demand Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detailed Skill Comparison")

    st.dataframe(
        comparison[[
            "skill_name",
            "india_demand_pct",
            "global_demand_pct",
            "demand_gap_percentage_points",
            "market_presence"
        ]].sort_values(
            "india_demand_pct",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )


# TAB 3: CATEGORY COMPARISON
with tab3:

    st.subheader("Demand by Skill Category")

    view = st.radio(
        "Select View",
        ["India vs Global", "India", "Global"],
        horizontal=True
    )

    if view == "India":

        category_data = categories.sort_values(
            "india_demand_pct"
        )

        fig = px.bar(
            category_data,
            x="india_demand_pct",
            y="skill_category",
            orientation="h",
            title="Indian Skill Category Demand"
        )

    elif view == "Global":

        category_data = categories.sort_values(
            "global_demand_pct"
        )

        fig = px.bar(
            category_data,
            x="global_demand_pct",
            y="skill_category",
            orientation="h",
            title="Global Skill Category Demand"
        )

    else:

        category_data = categories.melt(
            id_vars="skill_category",
            value_vars=[
                "india_demand_pct",
                "global_demand_pct"
            ],
            var_name="Market",
            value_name="Demand (%)"
        )

        category_data["Market"] = category_data["Market"].map({
            "india_demand_pct": "India",
            "global_demand_pct": "Global"
        })

        fig = px.bar(
            category_data,
            x="skill_category",
            y="Demand (%)",
            color="Market",
            barmode="group",
            title="India vs Global Category Demand"
        )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Category Demand Gap")

    gap_data = categories.sort_values(
        "demand_gap_percentage_points"
    )

    fig = px.bar(
        gap_data,
        x="demand_gap_percentage_points",
        y="skill_category",
        orientation="h",
        title="India vs Global Demand Gap",
        labels={
            "demand_gap_percentage_points": "Percentage Points",
            "skill_category": "Category"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        categories,
        use_container_width=True,
        hide_index=True
    )


# TAB 4: MARKET OPPORTUNITIES
with tab4:

    st.subheader("Common Skills Across Both Markets")

    st.metric("Common Skills", len(common))

    st.dataframe(
        common[[
            "skill_name",
            "india_demand_pct",
            "global_demand_pct"
        ]].sort_values(
            "india_demand_pct",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("Market-Specific Detected Skills")

    india_only = specific[
        specific["market_presence"] == "India Only"
    ]

    global_only = specific[
        specific["market_presence"] == "Global Only"
    ]

    left, right = st.columns(2)

    with left:
        st.write("India Only")
        st.dataframe(
            india_only[["skill_name", "india_demand_pct"]],
            use_container_width=True,
            hide_index=True
        )

    with right:
        st.write("Global Only")
        st.dataframe(
            global_only[["skill_name", "global_demand_pct"]],
            use_container_width=True,
            hide_index=True
        )

    st.info(
        "Market-specific skills are detected in only one dataset. "
        "This does not prove they are absent from the other market."
    )


# TAB 5: INDIA JOB ANALYSIS
with tab5:

    st.subheader("Indian Job Market Analysis")

    if "location" in india_jobs.columns:

        locations = (
            india_jobs["location"]
            .dropna()
            .astype(str)
            .value_counts()
            .head(15)
            .rename_axis("Location")
            .reset_index(name="Job Count")
        )

        fig = px.bar(
            locations.sort_values("Job Count"),
            x="Job Count",
            y="Location",
            orientation="h",
            title="Top 15 Job Locations in India"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Explore Indian Job Postings")

    roles = sorted(
        india_jobs["role_category_standard"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_role = st.selectbox(
        "Filter by Job Category",
        ["All"] + roles
    )

    filtered = india_jobs.copy()

    if selected_role != "All":
        filtered = filtered[
            filtered["role_category_standard"] == selected_role
        ]

    st.metric("Matching Job Postings", f"{len(filtered):,}")

    display_columns = [
        col for col in [
            "job_title",
            "role_category_standard",
            "location",
            "job_experience_required",
            "job_salary",
            "manual_review"
        ]
        if col in filtered.columns
    ]

    st.dataframe(
        filtered[display_columns].head(500),
        use_container_width=True,
        hide_index=True
    )

    st.caption("Showing a maximum of 500 job postings.")


# FOOTER
st.markdown("---")

st.caption(
    "Job Market Intelligence & Skill Gap Analyzer | "
    "Academic Portfolio Project"
)

st.caption(
    "India dataset: 2019 | Global dataset: 2023–2024. "
    "Classification is rule-based and skill extraction "
    "depends on available source data."
)
