import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_clean.csv",
    usecols=["job_id", "title", "description"]
)

matches = pd.read_csv(
    "data/processed/global_skills_extracted_sample.csv"
)

for skill in ["C", "Excel", "Python", "SQL"]:

    print("\nSKILL:", skill)
    print("=" * 60)

    selected = matches[matches["skill_name"] == skill]

    for _, row in selected.iterrows():

        job = jobs[jobs["job_id"] == row["job_id"]]

        if not job.empty:
            print("\nJOB TITLE:", job.iloc[0]["title"])
            print("DESCRIPTION:")
            print(str(job.iloc[0]["description"])[:500])