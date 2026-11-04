
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

jobs = pd.read_csv(
    DATA / "global_jobs_clean.csv",
    usecols=["job_id", "title", "description"]
)

skills = pd.read_csv(
    DATA / "global_skills_extracted.csv",
    usecols=["job_id", "skill_name", "category"]
)

sample = skills.sample(
    n=min(30, len(skills)),
    random_state=42
)

sample = sample.merge(
    jobs,
    on="job_id",
    how="left"
)

for _, row in sample.iterrows():
    print("\n" + "=" * 70)
    print("JOB TITLE:", row["title"])
    print("EXTRACTED SKILL:", row["skill_name"])
    print("CATEGORY:", row["category"])
    print("DESCRIPTION:")
    print(str(row["description"])[:1200])
