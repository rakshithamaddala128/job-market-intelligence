
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA = PROJECT_DIR / "data" / "processed"

india = pd.read_csv(
    DATA / "india_jobs_clean.csv"
)

print("\nTOTAL INDIAN JOB POSTINGS:", len(india))

print("\nTOP 30 JOB TITLES:")
print(
    india["job_title"]
    .value_counts()
    .head(30)
    .to_string()
)

print("\nTOP 30 FUNCTIONAL AREAS:")
print(
    india["functional_area"]
    .value_counts()
    .head(30)
    .to_string()
)

print("\nTOP 30 ROLE CATEGORIES:")
print(
    india["role_category"]
    .value_counts()
    .head(30)
    .to_string()
)

print("\nTOP 30 INDUSTRIES:")
print(
    india["industry"]
    .value_counts()
    .head(30)
    .to_string()
)
