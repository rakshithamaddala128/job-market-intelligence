
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
GLOBAL_FOLDER = PROJECT_DIR / "data" / "raw" / "global"

files_to_inspect = [
    "job_skills.csv",
    "salaries.csv",
    "benefits.csv",
    "job_industries.csv",
    "skills.csv",
    "industries.csv"
]

for file_name in files_to_inspect:
    file_path = GLOBAL_FOLDER / file_name

    print("\n" + "=" * 55)
    print(file_name)
    print("=" * 55)

    if file_path.exists():
        df = pd.read_csv(file_path, nrows=5)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nFirst 5 rows:")
        print(df.head())
    else:
        print("File not found:", file_name)
