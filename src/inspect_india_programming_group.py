from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

india = pd.read_csv(DATA / "india_jobs_classified.csv")

group = india[
    (india["role_category_standard"] == "Other") &
    (india["functional_area"].str.contains(
        "IT Software - Application Programming",
        case=False,
        na=False
    )) &
    (india["role_category"].str.contains(
        "Programming & Design",
        case=False,
        na=False
    ))
].copy()

print("TOTAL JOBS:", len(group))

print("\nRANDOM SAMPLE OF 50 JOBS")
print("-" * 60)

print(
    group[
        ["job_title", "functional_area", "role_category"]
    ]
    .sample(
        n=min(50, len(group)),
        random_state=42
    )
    .to_string(index=False)
)

print("\nTOP 50 JOB TITLES")
print("-" * 60)

print(
    group["job_title"]
    .value_counts()
    .head(50)
    .to_string()
)