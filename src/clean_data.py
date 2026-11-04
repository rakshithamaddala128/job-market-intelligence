
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW = PROJECT_DIR / "data" / "raw"
PROCESSED = PROJECT_DIR / "data" / "processed"

PROCESSED.mkdir(parents=True, exist_ok=True)

india_file = next((RAW / "india").glob("*.csv"))

india = pd.read_csv(india_file)
global_jobs = pd.read_csv(RAW / "global" / "postings.csv")

india.columns = india.columns.str.strip().str.lower().str.replace(" ", "_")
global_jobs.columns = global_jobs.columns.str.strip().str.lower()

india = india.drop_duplicates(subset="uniq_id")
global_jobs = global_jobs.drop_duplicates(subset="job_id")

india = india.dropna(subset=["job_title", "location"])
global_jobs = global_jobs.dropna(subset=["title", "location", "description"])

india["job_title"] = india["job_title"].str.strip()
india["location"] = india["location"].str.strip()
global_jobs["title"] = global_jobs["title"].str.strip()
global_jobs["location"] = global_jobs["location"].str.strip()

india.to_csv(PROCESSED / "india_jobs_clean.csv", index=False)
global_jobs.to_csv(PROCESSED / "global_jobs_clean.csv", index=False)

global_folder = RAW / "global"

skills = pd.read_csv(global_folder / "job_skills.csv")
skill_names = pd.read_csv(global_folder / "skills.csv")

skills_clean = skills.merge(
    skill_names,
    on="skill_abr",
    how="left"
)

skills_clean = skills_clean.merge(
    global_jobs[["job_id"]],
    on="job_id",
    how="inner"
)

skills_clean = skills_clean.drop_duplicates()

skills_clean.to_csv(
    PROCESSED / "global_skills_clean.csv",
    index=False
)

salaries = pd.read_csv(global_folder / "salaries.csv")
salaries_clean = salaries.merge(
    global_jobs[["job_id"]],
    on="job_id",
    how="inner"
)

salaries_clean.to_csv(
    PROCESSED / "global_salaries_clean.csv",
    index=False
)

industries = pd.read_csv(global_folder / "job_industries.csv")
industry_names = pd.read_csv(global_folder / "industries.csv")

industries_clean = industries.merge(
    industry_names,
    on="industry_id",
    how="left"
)

industries_clean = industries_clean.merge(
    global_jobs[["job_id"]],
    on="job_id",
    how="inner"
)

industries_clean = industries_clean.drop_duplicates()

industries_clean.to_csv(
    PROCESSED / "global_industries_clean.csv",
    index=False
)

print("DATA CLEANING COMPLETED")

print("\nIndia jobs:", len(india))
print("Global jobs:", len(global_jobs))
print("Global skill records:", len(skills_clean))
print("Global salary records:", len(salaries_clean))
print("Global industry records:", len(industries_clean))

print("\nProcessed files saved in:", PROCESSED)
