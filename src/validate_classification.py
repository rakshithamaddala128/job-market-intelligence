
import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_classified.csv"
)

categories = [
    "AI & Machine Learning",
    "Data Analytics",
    "Software Development",
    "IT & Infrastructure",
    "Quality Assurance"
]

for category in categories:

    sample = jobs[
        jobs["role_category"] == category
    ].sample(
        n=min(20, len(jobs[jobs["role_category"] == category])),
        random_state=42
    )

    print("\n" + "=" * 70)
    print("CATEGORY:", category)
    print("=" * 70)

    print(
        sample[["title", "role_category"]]
        .to_string(index=False)
    )
