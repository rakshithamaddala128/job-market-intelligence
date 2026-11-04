
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

india = pd.read_csv(DATA / "india_jobs_classified.csv")

other = india[
    india["role_category_standard"] == "Other"
].copy()

pattern = (
    r"developer|programmer|software engineer|"
    r"devops|dev-ops|system admin|"
    r"network engineer|database admin|"
    r"security engineer|cloud engineer|"
    r"data engineer|big data|"
    r"test engineer|software tester|"
    r"automation tester|php developers?"
)

potential = other[
    other["job_title"].str.contains(
        pattern,
        case=False,
        na=False,
        regex=True
    )
]

print("POTENTIAL MISCLASSIFIED JOBS:", len(potential))

print("\nSAMPLE OF 60 JOBS")
print("-" * 60)

print(
    potential[
        ["job_title", "functional_area", "role_category"]
    ]
    .sample(
        n=min(60, len(potential)),
        random_state=42
    )
    .to_string(index=False)
)

print("\nMOST COMMON TITLES")
print("-" * 60)

print(
    potential["job_title"]
    .value_counts()
    .head(40)
    .to_string()
)
