
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

df = pd.read_csv(DATA / "india_jobs_classified.csv")

categories = [
    "AI & Machine Learning",
    "Data Analytics",
    "Software Development",
    "IT & Infrastructure",
    "Quality Assurance"
]

print("\nVERSION 5 CLASSIFICATION VALIDATION")
print("=" * 75)

for category in categories:

    sample = df[
        df["role_category_standard"] == category
    ]

    print(f"\n\nCATEGORY: {category}")
    print("Total records:", len(sample))
    print("-" * 75)

    if len(sample) > 0:
        display_columns = [
            "job_title",
            "functional_area",
            "role_category"
        ]

        print(
            sample[display_columns]
            .sample(n=min(30, len(sample)), random_state=42)
            .to_string(index=False)
        )


print("\n\nPOTENTIAL MISCLASSIFIED JOBS IN OTHER")
print("=" * 75)

other = df[
    df["role_category_standard"] == "Other"
].copy()

pattern = (
    r"developer|programmer|software engineer|"
    r"devops|dev-ops|system admin|network engineer|"
    r"database admin|security engineer|cloud engineer|"
    r"data engineer|big data|hadoop|"
    r"test engineer|software tester|"
    r"automation tester|embedded software|"
    r"mainframe|webmethods|splunk developer|"
    r"magento developer|angular developer|"
    r"java developer|php developer|python developer|"
    r"dot.?net developer|ios developer|"
    r"android developer|blockchain developer"
)

candidates = other[
    other["job_title"].str.contains(
        pattern,
        case=False,
        na=False,
        regex=True
    )
]

print("Potential candidates:", len(candidates))
print("-" * 75)

print(
    candidates[
        [
            "job_title",
            "functional_area",
            "role_category"
        ]
    ]
    .sample(
        n=min(60, len(candidates)),
        random_state=42
    )
    .to_string(index=False)
)
