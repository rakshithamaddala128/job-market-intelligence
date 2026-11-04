import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_classified.csv"
)

other = jobs[jobs["role_category"] == "Other"]

keywords = [
    "data", "developer", "software", "database",
    "technology", "technical", "system", "cloud",
    "computer", "analytics", "security", "network",
    "programmer", "automation", "engineer",
    "IT ", "information technology"
]

pattern = "|".join(keywords)

potential = other[
    other["title"].str.contains(
        pattern,
        case=False,
        na=False
    )
]

print("POTENTIALLY RELEVANT TITLES:", len(potential))

print("\nTOP 100 TITLES:")

print(
    potential["title"]
    .value_counts()
    .head(100)
    .to_string()
)