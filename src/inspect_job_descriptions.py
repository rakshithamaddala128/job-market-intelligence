import pandas as pd

jobs = pd.read_csv(
    "data/raw/global/postings.csv",
    usecols=["job_id", "title", "description"],
    nrows=10
)

for index, row in jobs.iterrows():
    print("\nJOB TITLE:", row["title"])
    print("\nDESCRIPTION:")
    print(str(row["description"])[:1500])
    print("\n" + "=" * 80)