import pandas as pd
import re

jobs = pd.read_csv(
    "data/processed/global_jobs_clean.csv",
    usecols=["job_id", "title", "description"],
    nrows=100
)

taxonomy = pd.read_csv(
    "data/processed/skill_taxonomy.csv"
)

results = []

for _, job in jobs.iterrows():

    description = str(job["description"]).lower()

    for _, skill in taxonomy.iterrows():

        aliases = skill["aliases"].split("|")

        for alias in aliases:

            pattern = r"(?<!\w)" + re.escape(alias.lower()) + r"(?!\w)"

            if re.search(pattern, description):

                results.append({
                    "job_id": job["job_id"],
                    "title": job["title"],
                    "skill_name": skill["skill_name"],
                    "category": skill["category"]
                })

                break

extracted = pd.DataFrame(results)

if not extracted.empty:
    extracted = extracted.drop_duplicates(
        subset=["job_id", "skill_name"]
    )

    extracted.to_csv(
        "data/processed/global_skills_extracted_sample.csv",
        index=False
    )

    print("TOTAL JOBS ANALYZED:", len(jobs))
    print("TOTAL SKILL MATCHES:", len(extracted))
    print("\nTOP EXTRACTED SKILLS:")
    print(extracted["skill_name"].value_counts().head(20))

    print("\nEXTRACTED RECORDS:")
    print(extracted.head(20).to_string(index=False))

else:
    print("No skills were identified.")

print("\nSAMPLE EXTRACTION COMPLETED")