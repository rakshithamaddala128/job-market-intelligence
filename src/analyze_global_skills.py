
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
PROCESSED = PROJECT_DIR / "data" / "processed"
REPORTS = PROJECT_DIR / "reports"

REPORTS.mkdir(parents=True, exist_ok=True)

jobs = pd.read_csv(PROCESSED / "global_jobs_clean.csv")
skills = pd.read_csv(PROCESSED / "global_skills_clean.csv")

skills = skills.dropna(subset=["skill_name"])
skills["skill_name"] = skills["skill_name"].str.strip()

skills = skills[skills["skill_name"] != ""]

skill_demand = (
    skills.groupby("skill_name")["job_id"]
    .nunique()
    .reset_index(name="job_count")
)

total_jobs = jobs["job_id"].nunique()
jobs_with_skills = skills["job_id"].nunique()

skill_demand["job_percentage"] = (
    skill_demand["job_count"] / total_jobs * 100
).round(2)

skill_demand = skill_demand.sort_values(
    by="job_count",
    ascending=False
)

top_20 = skill_demand.head(20)

print("\nGLOBAL JOB MARKET - TOP 20 DEMANDED SKILLS")
print("=" * 55)
print(top_20.to_string(index=False))

print("\nTotal job postings:", total_jobs)
print("Jobs with skill information:", jobs_with_skills)
print(
    "Skill information coverage:",
    round(jobs_with_skills / total_jobs * 100, 2),
    "%"
)

top_20.to_csv(
    REPORTS / "global_top_20_skills.csv",
    index=False
)

plt.figure(figsize=(12, 8))

plt.barh(
    top_20["skill_name"].iloc[::-1],
    top_20["job_count"].iloc[::-1]
)

plt.xlabel("Number of Job Postings")
plt.ylabel("Skills")
plt.title("Top 20 Most Demanded Skills - Global Job Market")
plt.tight_layout()

plt.savefig(
    REPORTS / "global_top_20_skills.png",
    dpi=300
)

plt.show()

print("\nAnalysis completed.")
print("Results saved in:", REPORTS)
