
import pandas as pd

df = pd.read_csv("data/processed/india_jobs_classified.csv")

other = df[df["role_category_standard"] == "Other"].copy()

print("\nTOTAL JOBS IN OTHER:", len(other))

print("\nPOTENTIAL MISCLASSIFIED IT JOBS")
print("-" * 90)

patterns = (
    r"developer|programmer|software|engineer|"
    r"data|analytics|hadoop|big data|etl|"
    r"machine learning|artificial intelligence|"
    r"devops|cloud|network|database|"
    r"administrator|security|testing|tester|"
    r"qa|java|python|\.net|android|ios|"
    r"full stack|backend|frontend|"
    r"tableau|power bi|informatica|"
    r"cognos|sap|oracle|linux|windows"
)

candidates = other[
    other["job_title"].fillna("").str.contains(
        patterns, case=False, regex=True
    )
]

print("Potential candidates:", len(candidates))

print("\nSAMPLE OF 100 CANDIDATES")
print("-" * 90)

columns = [
    "job_title",
    "functional_area",
    "role_category",
    "role_category_standard",
    "manual_review"
]

print(
    candidates[columns]
    .sample(min(100, len(candidates)), random_state=42)
    .to_string(index=False)
)

print("\nMANUAL REVIEW COUNTS IN OTHER")
print(other["manual_review"].value_counts().to_string())
