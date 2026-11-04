
import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_classified.csv"
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

    print("\nTITLE:", title)
    print("MATCHED JOBS:", len(matched))

    print(
        matched[["title", "role_category"]]
        .to_string(index=False)
    )
