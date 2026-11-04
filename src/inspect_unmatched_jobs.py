
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

jobs = pd.read_csv(
    DATA / "global_jobs_classified.csv"
)

descriptions = pd.read_csv(
    DATA / "global_jobs_clean.csv",
    usecols=["job_id", "description"]
)

skills = pd.read_csv(
    DATA / "global_skills_extracted.csv",
    usecols=["job_id"]
)

unmatched = jobs[
    jobs["role_category"] == "IT & Infrastructure"
].merge(
    descriptions,
    on="job_id",
    how="left"
).merge(
    skills[["job_id"]].drop_duplicates(),
    on="job_id",
    how="left",
    indicator=True
)

unmatched = unmatched[
    unmatched["_merge"] == "left_only"
]

print("UNMATCHED JOBS:", len(unmatched))

for _, job in unmatched.iloc[5:15].iterrows():
    print("\nJOB:", job["title"])
    print("DESCRIPTION:", str(job["description"])[:700])

