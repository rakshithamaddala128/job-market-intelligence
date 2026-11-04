import pandas as pd

skills = pd.read_csv("data/raw/global/job_skills.csv")
taxonomy = pd.read_csv("data/raw/global/skills.csv")

print("\nJOB SKILLS DATA:")
print(skills.head(10).to_string(index=False))

print("\nUNIQUE SKILL CODES IN JOB SKILLS:")
print(skills["skill_abr"].nunique())

print("\nSKILL CODE FREQUENCY:")
print(
    skills["skill_abr"]
    .value_counts()
    .head(20)
)

print("\nSKILL CODE AND NAME:")
print(
    skills.merge(taxonomy, on="skill_abr")
    .groupby(["skill_abr", "skill_name"])
    .size()
    .reset_index(name="record_count")
    .sort_values("record_count", ascending=False)
    .to_string(index=False)
)