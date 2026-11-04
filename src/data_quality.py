
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
GLOBAL_FOLDER = PROJECT_DIR / "data" / "raw" / "global"
INDIA_FOLDER = PROJECT_DIR / "data" / "raw" / "india"

files = [
    GLOBAL_FOLDER / "postings.csv",
    GLOBAL_FOLDER / "job_skills.csv",
    GLOBAL_FOLDER / "salaries.csv",
    GLOBAL_FOLDER / "benefits.csv",
    GLOBAL_FOLDER / "job_industries.csv",
    GLOBAL_FOLDER / "skills.csv",
    GLOBAL_FOLDER / "industries.csv"
]

india_files = sorted(INDIA_FOLDER.glob("*.csv"))
files.extend(india_files)

for file_path in files:
    print("\n" + "=" * 60)
    print(file_path.name)
    print("=" * 60)

    if not file_path.exists():
        print("File not found")
        continue

    if file_path.name == "postings.csv":
        df = pd.read_csv(file_path, nrows=10000)
        print("Inspection sample: first 10,000 rows")
    else:
        df = pd.read_csv(file_path)

    print("Rows inspected:", len(df))
    print("Columns:", len(df.columns))
    print("Duplicate rows:", df.duplicated().sum())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nUnique job IDs:")
    if "job_id" in df.columns:
        print(df["job_id"].nunique())

    if "Uniq Id" in df.columns:
        print("\nUnique Indian job IDs:")
        print(df["Uniq Id"].nunique())
