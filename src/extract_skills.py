
from pathlib import Path
import pandas as pd
import re

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

jobs = pd.read_csv(
    DATA / "global_jobs_clean.csv",
    usecols=["job_id", "title", "description"]
)

taxonomy = pd.read_csv(DATA / "skill_taxonomy.csv")

patterns = []

for _, skill in taxonomy.iterrows():
    aliases = [
        re.escape(alias.strip())
        for alias in skill["aliases"].split("|")
        if alias.strip()
    ]

    aliases.sort(key=len, reverse=True)

    patterns.append({
        "skill_name": skill["skill_name"],
        "category": skill["category"],
        "pattern": r"(?<!\w)(?:" + "|".join(aliases) + r")(?!\w)"
    })

results = []

batch_size = 10000

for start in range(0, len(jobs), batch_size):

    batch = jobs.iloc[start:start + batch_size]

    descriptions = batch["description"].fillna("")

    for skill in patterns:

        matched = descriptions.str.contains(
            skill["pattern"],
            case=False,
            regex=True,
            na=False
        )

        if matched.any():

            selected = batch.loc[matched, ["job_id", "title"]].copy()

            selected["skill_name"] = skill["skill_name"]
            selected["category"] = skill["category"]

            results.append(selected)

    print("Jobs processed:", min(start + batch_size, len(jobs)))

extracted = pd.concat(results, ignore_index=True)

extracted = extracted.drop_duplicates(
    subset=["job_id", "skill_name"]
)

extracted.to_csv(
    DATA / "global_skills_extracted.csv",
    index=False
)

print("\nTOTAL JOBS ANALYZED:", len(jobs))
print("TOTAL UNIQUE JOB-SKILL MATCHES:", len(extracted))
print("JOBS WITH DETECTED SKILLS:", extracted["job_id"].nunique())

print("\nTOP 20 SKILLS:")
print(extracted["skill_name"].value_counts().head(20))

print("\nSKILLS BY CATEGORY:")
print(extracted["category"].value_counts())

print("\nSKILL EXTRACTION COMPLETED")
