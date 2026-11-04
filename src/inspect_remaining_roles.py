
import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_classified.csv"
)

other = jobs[jobs["role_category"] == "Other"]

keywords = [
    "developer",
    "programmer",
    "software",
    "data engineer",
    "data analyst",
    "data scientist",
    "database",
    "cloud",
    "devops",
    "cyber",
    "security engineer",
    "network",
    "system administrator",
    "site reliability",
    "technical program manager",
    "technical project manager",
    "technology officer",
    "technology manager",
    "mainframe",
    "snowflake",
    "tableau",
    "power bi",
    "automation tester",
    "test automation",
    "qa engineer"
]

pattern = "|".join(keywords)

potential = other[
    other["title"].str.contains(
        pattern,
        case=False,
        na=False
    )
]

print("CANDIDATE JOB POSTINGS:", len(potential))

print("\nCANDIDATE TITLES:")

print(
    potential["title"]
    .value_counts()
    .head(100)
    .to_string()
)
