
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

india = pd.read_csv(
    DATA / "india_jobs_classified.csv"
)

categories = [
    "AI & Machine Learning",
    "Data Analytics",
    "Software Development",
    "IT & Infrastructure",
    "Quality Assurance",
    "Other"
]

for category in categories:

    sample = india[
        india["role_category_standard"] == category
    ]

    print("\n" + "=" * 70)
    print("CATEGORY:", category)
    print("TOTAL JOBS:", len(sample))
    print("=" * 70)

    print(
        sample[
            ["job_title", "functional_area", "role_category"]
        ]
        .sample(
            n=min(20, len(sample)),
            random_state=42
        )
        .to_string(index=False)
    )
