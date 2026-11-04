from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW = PROJECT_DIR / "data" / "raw" / "global"

skills = pd.read_csv(RAW / "skills.csv")

print("\nTOTAL SKILL CATEGORIES:", len(skills))

print("\nALL AVAILABLE SKILLS:")
print(skills.sort_values("skill_name").to_string(index=False))

print("\nSKILL NAME EXAMPLES:")
print(
    skills["skill_name"]
    .sample(min(20, len(skills)), random_state=42)
    .to_list()
)

print("\nDUPLICATE SKILL CODES:", skills["skill_abr"].duplicated().sum())
print("MISSING SKILL NAMES:", skills["skill_name"].isna().sum())