
import pandas as pd
import re
from pathlib import Path

INPUT_FILE = Path("data/processed/india_jobs_classified.csv")
TAXONOMY_FILE = Path("data/processed/skill_taxonomy.csv")

OUTPUT_SKILLS = Path("data/processed/india_skills_extracted.csv")
OUTPUT_DEMAND = Path("data/processed/india_skill_demand.csv")
OUTPUT_CATEGORY = Path("data/processed/india_skill_category_demand.csv")


def normalize(text):
    text = str(text).lower().strip()
    text = re.sub(r"[^a-z0-9+#.]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def main():
    jobs = pd.read_csv(INPUT_FILE)
    taxonomy = pd.read_csv(TAXONOMY_FILE)

    alias_lookup = {}

    for _, row in taxonomy.iterrows():
        skill_name = str(row["skill_name"]).strip()
        category = str(row["category"]).strip()

        aliases = str(row["aliases"]).split("|")
        aliases.append(skill_name)

        for alias in aliases:
            alias = normalize(alias)

            if alias:
                alias_lookup[alias] = (skill_name, category)

    records = []

    for _, job in jobs.iterrows():
        raw_skills = job["key_skills"]

        if pd.isna(raw_skills):
            continue

        job_skills = set()

        for item in str(raw_skills).split("|"):
            normalized = normalize(item)

            if normalized in alias_lookup:
                skill_name, category = alias_lookup[normalized]

                if skill_name not in job_skills:
                    records.append({
                        "uniq_id": job["uniq_id"],
                        "job_title": job["job_title"],
                        "role_category_standard": job["role_category_standard"],
                        "skill_name": skill_name,
                        "skill_category": category,
                        "location": job["location"]
                    })

                    job_skills.add(skill_name)

    extracted = pd.DataFrame(records)

    if extracted.empty:
        print("No matching skills found. Check taxonomy aliases and separators.")
        return

    extracted.to_csv(OUTPUT_SKILLS, index=False)

    total_jobs = jobs["uniq_id"].nunique()

    demand = (
        extracted.groupby(["skill_name", "skill_category"])
        .agg(
            job_count=("uniq_id", "nunique")
        )
        .reset_index()
        .sort_values("job_count", ascending=False)
    )

    demand["demand_percentage"] = (
        demand["job_count"] / total_jobs * 100
    ).round(2)

    demand.to_csv(OUTPUT_DEMAND, index=False)

    category_demand = (
        extracted.groupby("skill_category")
        .agg(
            skill_matches=("uniq_id", "size"),
            unique_jobs=("uniq_id", "nunique"),
            unique_skills=("skill_name", "nunique")
        )
        .reset_index()
        .sort_values("skill_matches", ascending=False)
    )

    category_demand["job_coverage_percentage"] = (
        category_demand["unique_jobs"] / total_jobs * 100
    ).round(2)

    category_demand.to_csv(OUTPUT_CATEGORY, index=False)

    jobs_with_skills = extracted["uniq_id"].nunique()

    print("\nINDIAN SKILL EXTRACTION SUMMARY")
    print("=" * 55)
    print(f"Total jobs: {total_jobs:,}")
    print(f"Jobs with matched skills: {jobs_with_skills:,}")
    print(f"Unique skill matches: {len(extracted):,}")
    print(f"Unique skills found: {extracted['skill_name'].nunique():,}")

    print("\nTOP 20 INDIAN SKILLS")
    print(demand.head(20).to_string(index=False))

    print("\nSKILL CATEGORY DEMAND")
    print(category_demand.to_string(index=False))

    print("\nFILES SAVED")
    print(OUTPUT_SKILLS)
    print(OUTPUT_DEMAND)
    print(OUTPUT_CATEGORY)


if __name__ == "__main__":
    main()
