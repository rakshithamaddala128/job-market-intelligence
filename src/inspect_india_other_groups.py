from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

india = pd.read_csv(DATA / "india_jobs_classified.csv")

other = india[
    india["role_category_standard"] == "Other"
].copy()

it_related = other[
    other["functional_area"].str.contains(
        r"IT Software|IT Hardware|Analytics|Technical Support",
        case=False,
        na=False
    )
].copy()

print("\nFUNCTIONAL AREA + ROLE CATEGORY COMBINATIONS")
print("-" * 60)

combinations = (
    it_related.groupby(
        ["functional_area", "role_category"]
    )
    .size()
    .reset_index(name="job_count")
    .sort_values("job_count", ascending=False)
)

print(combinations.head(30).to_string(index=False))

print("\nMOST COMMON JOB TITLES IN THESE COMBINATIONS")
print("-" * 60)

print(
    it_related["job_title"]
    .value_counts()
    .head(50)
    .to_string()
)

print("\nTOTAL POTENTIAL IT JOBS:", len(it_related))
