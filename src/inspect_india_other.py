
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

india = pd.read_csv(
    DATA / "india_jobs_classified.csv"
)

other = india[
    india["role_category_standard"] == "Other"
]

print("TOTAL OTHER JOBS:", len(other))

print("\nIT-RELATED FUNCTIONAL AREAS IN OTHER:")

it_related = other[
    other["functional_area"].str.contains(
        r"IT Software|IT Hardware|Analytics|Technical Support",
        case=False,
        na=False
    )
]

print("Potential IT jobs:", len(it_related))

print(
    it_related[
        ["job_title", "functional_area", "role_category"]
    ]
    .sample(
        n=min(40, len(it_related)),
        random_state=42
    )
    .to_string(index=False)
)
