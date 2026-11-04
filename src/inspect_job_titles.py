import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_clean.csv",
    usecols=["title"]
)

print("TOTAL JOB TITLES:", len(jobs))

print("\nMOST COMMON JOB TITLES:")
print(jobs["title"].value_counts().head(50).to_string())

print("\nJOB TITLE SAMPLES:")
print(jobs["title"].drop_duplicates().head(100).to_string(index=False))