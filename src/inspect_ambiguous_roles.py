
import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_clean.csv",
    usecols=["job_id", "title", "description"]
)

titles = [
    "PL/SQL Developer",
    "Big Data Engineer",
    "Product Compliance QA Engineer"
]

for title in titles:

    matched = jobs[
        jobs["title"].str.contains(
            title,
            case=False,
            na=False,
            regex=False
        )
    ]

    print("\n" + "=" * 70)
    print("TITLE:", title)
    print("=" * 70)

    print("MATCHED JOBS:", len(matched))

    for _, job in matched.head(3).iterrows():

        print("\nJOB TITLE:", job["title"])
        print("JOB ID:", job["job_id"])

        description = str(job["description"])

        print("\nJOB DESCRIPTION:")
        print(description[:2000])
        print("\n" + "-" * 70)
