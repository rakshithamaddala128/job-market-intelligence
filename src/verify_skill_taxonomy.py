import pandas as pd

taxonomy = pd.read_csv("data/processed/skill_taxonomy.csv")

print("TOTAL SKILLS:", len(taxonomy))
print("DUPLICATE SKILL NAMES:", taxonomy["skill_name"].duplicated().sum())
print("MISSING VALUES:\n", taxonomy.isnull().sum())
print("\nDUPLICATE SKILL NAMES:")
print(taxonomy[taxonomy["skill_name"].duplicated(keep=False)])
print("\nCATEGORY COUNTS:")
print(taxonomy["category"].value_counts())