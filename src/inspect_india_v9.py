
import pandas as pd

df = pd.read_csv("data/processed/india_jobs_classified.csv")

columns = [
    "job_title",
    "functional_area",
    "role_category",
    "role_category_standard",
    "manual_review"
]

print("\nVERSION 9 CLASSIFICATION SUMMARY")
print("=" * 90)

print(df["role_category_standard"].value_counts().to_string())

print("\nMANUAL REVIEW SUMMARY")
print(df["manual_review"].value_counts().to_string())

for category in [
    "AI & Machine Learning",
    "Data Analytics",
    "Software Development",
    "IT & Infrastructure",
    "Quality Assurance",
    "Other"
]:
    subset = df[df["role_category_standard"] == category]

    print("\n")
    print("=" * 90)
    print(f"CATEGORY: {category}")
    print(f"TOTAL: {len(subset)}")
    print("=" * 90)

    print(
        subset[columns]
        .sample(min(25, len(subset)), random_state=42)
        .to_string(index=False)
    )

print("\nOTHER CATEGORY: POTENTIAL IT CANDIDATES")

other = df[df["role_category_standard"] == "Other"]

patterns = (
    r"developer|programmer|software|engineer|data|analytics|"
    r"hadoop|big data|etl|machine learning|artificial intelligence|"
    r"devops|cloud|network|database|administrator|security|"
    r"testing|tester|qa|java|python|\.net|android|ios|"
    r"full stack|backend|frontend|tableau|power bi|informatica|"
    r"cognos|sap|oracle|linux|windows"
)

candidates = other[
    other["job_title"].fillna("").str.contains(
        patterns, case=False, regex=True
    )
]

print(f"\nPotential candidates: {len(candidates)}")

print(
    candidates[columns]
    .sample(min(60, len(candidates)), random_state=42)
    .to_string(index=False)
)
