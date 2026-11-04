import pandas as pd

df = pd.read_csv("data/processed/india_jobs_classified.csv")

for category in [
    "AI & Machine Learning",
    "Data Analytics",
    "Software Development",
    "IT & Infrastructure",
    "Quality Assurance"
]:
    sample = df[df["role_category_standard"] == category]

    print(f"\nCATEGORY: {category}")
    print(f"Total: {len(sample)}")
    print("-" * 70)

    print(
        sample[[
            "job_title",
            "functional_area",
            "role_category",
            "manual_review"
        ]].head(30).to_string(index=False)
    )