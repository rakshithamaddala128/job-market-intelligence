
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

india = pd.read_csv(DATA / "india_jobs_classified.csv")

pattern = (
    r"developer|programmer|software engineer|"
    r"devops|dev-ops|system admin|"
    r"network engineer|database admin|"
    r"security engineer|cloud engineer|"
    r"data engineer|big data|"
    r"test engineer|software tester|"
    r"automation tester"
)

other = india[
    india["role_category_standard"] == "Other"
].copy()

potential = other[
    other["job_title"].str.contains(
        pattern,
        case=False,
        na=False
    )
]

print("TOTAL POTENTIAL JOBS:", len(potential))

print("\nSAMPLE OF 100 JOB TITLES")
print("-" * 60)

sample = potential.sample(
    n=min(100, len(potential)),
    random_state=21
)

print(
    sample[
        ["job_title", "functional_area", "role_category"]
    ].to_string(index=False)
)
