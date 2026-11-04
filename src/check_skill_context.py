
from pathlib import Path
import pandas as pd
import re

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

jobs = pd.read_csv(
    DATA / "global_jobs_clean.csv",
    usecols=["job_id", "title", "description"]
)

skills = pd.read_csv(
    DATA / "global_skills_extracted.csv",
    usecols=["job_id", "skill_name"]
)

check_skills = ["Power BI", "SQL", "GitHub", "Data Center"]

sample = skills[
    skills["skill_name"].isin(check_skills)
].sample(
    n= min(20, len(skills[skills["skill_name"].isin(check_skills)])),
    random_state=42
)

sample = sample.merge(jobs, on="job_id", how="left")

for _, row in sample.iterrows():
    description = str(row["description"])
    skill = row["skill_name"]

    matches = list(
        re.finditer(re.escape(skill), description, re.IGNORECASE)
    )

    print("\n" + "=" * 70)
    print("JOB:", row["title"])
    print("SKILL:", skill)
    print("OCCURRENCES:", len(matches))

    if matches:
        for match in matches:
            start = max(0, match.start() - 120)
            end = min(len(description), match.end() + 120)
            print("CONTEXT:", description[start:end])
    else:
        print("Canonical skill name not found; check its taxonomy aliases.")
