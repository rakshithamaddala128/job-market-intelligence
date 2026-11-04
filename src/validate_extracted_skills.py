
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

jobs = pd.read_csv(
    DATA / "global_jobs_classified.csv",
    usecols=["job_id", "role_category"]
)

skills = pd.read_csv(
    DATA / "global_skills_extracted.csv",
    usecols=["job_id", "skill_name"]
)

jobs_with_skills = skills[["job_id"]].drop_duplicates()

analysis = jobs.merge(
    jobs_with_skills,
    on="job_id",
    how="left",
    indicator=True
)

analysis["has_skills"] = (
    analysis["_merge"] == "both"
)

coverage = (
    analysis.groupby("role_category")
    .agg(
        total_jobs=("job_id", "nunique"),
        jobs_with_skills=("has_skills", "sum")
    )
    .reset_index()
)

coverage["coverage_percentage"] = (
    coverage["jobs_with_skills"]
    / coverage["total_jobs"] * 100
)

print("\nSKILL COVERAGE BY JOB CATEGORY:")
print(
    coverage.sort_values(
        "coverage_percentage",
        ascending=False
    ).to_string(index=False)
)

print("\nTARGET CATEGORY COVERAGE:")

target = coverage[
    coverage["role_category"] != "Other"
]

target_jobs = target["total_jobs"].sum()
target_matched = target["jobs_with_skills"].sum()

print("Total target jobs:", target_jobs)
print("Target jobs with skills:", target_matched)
print(
    "Target coverage: {:.2f}%".format(
        target_matched / target_jobs * 100
    )
)
