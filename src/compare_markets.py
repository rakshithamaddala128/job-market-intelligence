
import pandas as pd
from pathlib import Path

DATA = Path("data/processed")

india_skills = pd.read_csv(DATA / "india_skills_extracted.csv")
global_skills = pd.read_csv(DATA / "global_skills_extracted.csv")

india_jobs = pd.read_csv(DATA / "india_jobs_classified.csv")
global_jobs = pd.read_csv(DATA / "global_jobs_classified.csv")

india_total = india_jobs["uniq_id"].nunique()
global_total = global_jobs["job_id"].nunique()

india_skills["skill_name"] = india_skills["skill_name"].str.strip()
global_skills["skill_name"] = global_skills["skill_name"].str.strip()

india_demand = (
    india_skills.groupby("skill_name")
    .agg(
        india_job_count=("uniq_id", "nunique"),
        india_category=("skill_category", "first")
    )
    .reset_index()
)

global_demand = (
    global_skills.groupby("skill_name")
    .agg(
        global_job_count=("job_id", "nunique"),
        global_category=("category", "first")
    )
    .reset_index()
)

comparison = pd.merge(
    india_demand,
    global_demand,
    on="skill_name",
    how="outer"
)

comparison["india_job_count"] = comparison["india_job_count"].fillna(0).astype(int)
comparison["global_job_count"] = comparison["global_job_count"].fillna(0).astype(int)

comparison["india_demand_pct"] = (
    comparison["india_job_count"] / india_total * 100
).round(2)

comparison["global_demand_pct"] = (
    comparison["global_job_count"] / global_total * 100
).round(2)

comparison["demand_gap_percentage_points"] = (
    comparison["india_demand_pct"] - comparison["global_demand_pct"]
).round(2)

comparison["market_presence"] = comparison.apply(
    lambda row: (
        "Both Markets"
        if row["india_job_count"] > 0 and row["global_job_count"] > 0
        else "India Only"
        if row["india_job_count"] > 0
        else "Global Only"
    ),
    axis=1
)

comparison["skill_category"] = (
    comparison["india_category"].combine_first(comparison["global_category"])
)

comparison = comparison.sort_values(
    "india_demand_pct", ascending=False
)

comparison.to_csv(DATA / "india_global_skill_comparison.csv", index=False)

top_india = comparison.nlargest(20, "india_demand_pct")
top_global = comparison.nlargest(20, "global_demand_pct")

top_india.to_csv(DATA / "india_global_top_skills.csv", index=False)

common = comparison[comparison["market_presence"] == "Both Markets"]
india_only = comparison[comparison["market_presence"] == "India Only"]
global_only = comparison[comparison["market_presence"] == "Global Only"]

common.to_csv(DATA / "common_skills.csv", index=False)

specific = pd.concat([india_only, global_only])
specific.to_csv(DATA / "market_specific_skills.csv", index=False)

india_categories = (
    india_skills.groupby("skill_category")
    .agg(india_jobs=("uniq_id", "nunique"))
    .reset_index()
    .rename(columns={"skill_category": "skill_category"})
)

global_categories = (
    global_skills.groupby("category")
    .agg(global_jobs=("job_id", "nunique"))
    .reset_index()
    .rename(columns={"category": "skill_category"})
)

category_comparison = pd.merge(
    india_categories,
    global_categories,
    on="skill_category",
    how="outer"
).fillna(0)

category_comparison["india_demand_pct"] = (
    category_comparison["india_jobs"] / india_total * 100
).round(2)

category_comparison["global_demand_pct"] = (
    category_comparison["global_jobs"] / global_total * 100
).round(2)

category_comparison["demand_gap_percentage_points"] = (
    category_comparison["india_demand_pct"]
    - category_comparison["global_demand_pct"]
).round(2)

category_comparison.to_csv(
    DATA / "india_global_category_comparison.csv",
    index=False
)

print("\nINDIA VS GLOBAL MARKET COMPARISON")
print("=" * 60)

print(f"India jobs: {india_total:,}")
print(f"Global jobs: {global_total:,}")

print(f"\nIndia unique skills: {india_skills['skill_name'].nunique()}")
print(f"Global unique skills: {global_skills['skill_name'].nunique()}")
print(f"Common skills: {len(common)}")
print(f"India-only skills: {len(india_only)}")
print(f"Global-only skills: {len(global_only)}")

print("\nTOP 20 INDIA SKILLS")
print(top_india[[
    "skill_name", "india_demand_pct", "global_demand_pct"
]].to_string(index=False))

print("\nTOP 20 GLOBAL SKILLS")
print(top_global[[
    "skill_name", "india_demand_pct", "global_demand_pct"
]].to_string(index=False))

print("\nCATEGORY COMPARISON")
print(category_comparison.to_string(index=False))

print("\nALL COMPARISON FILES SAVED SUCCESSFULLY.")
