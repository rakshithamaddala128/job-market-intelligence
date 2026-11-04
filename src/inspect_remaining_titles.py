import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_classified.csv"
)

other = jobs[jobs["role_category"] == "Other"]

keywords = [
    "data",
    "developer",
    "programmer",
    "software",
    "database",
    "technology",
    "technical",
    "system",
    "information",
    "automation",
    "machine",
    "artificial intelligence",
    "cloud",
    "computer",
    "web",
    "analytics",
    "security",
    "qa",
    "quality assurance",
    "devops",
    "programming",
    "network",
    "IT "
]

pattern = "|".join(keywords)

potential = other[
    other["title"].str.contains(
        pattern,
        case=False,
        na=False
    )
]

print("REMAINING POTENTIALLY RELEVANT JOBS:", len(potential))

print("\nTOP 100 TITLES:")
print(
    potential["title"]
    .value_counts()
    .head(100)
    .to_string()
)