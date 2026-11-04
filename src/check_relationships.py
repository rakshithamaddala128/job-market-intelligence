
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
GLOBAL_FOLDER = PROJECT_DIR / "data" / "raw" / "global"

postings = pd.read_csv(GLOBAL_FOLDER / "postings.csv", usecols=["job_id"])
job_skills = pd.read_csv(GLOBAL_FOLDER / "job_skills.csv")
salaries = pd.read_csv(GLOBAL_FOLDER / "salaries.csv")
job_industries = pd.read_csv(GLOBAL_FOLDER / "job_industries.csv")

posting_ids = set(postings["job_id"].dropna())

print("Total LinkedIn postings:", len(posting_ids))

for name, df in [
    ("Job skills", job_skills),
    ("Salaries", salaries),
    ("Job industries", job_industries)
]:
    matched = df["job_id"].isin(posting_ids).sum()
    unmatched = len(df) - matched

    print("\n" + name)
    print("Total records:", len(df))
    print("Matched records:", matched)
    print("Unmatched records:", unmatched)
    print("Match percentage:", round(matched / len(df) * 100, 2))
