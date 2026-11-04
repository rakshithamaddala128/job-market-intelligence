
import pandas as pd
import numpy as np
import sklearn

print("Job Market Intelligence project setup successful!")
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("Scikit-learn version:", sklearn.__version__)

jobs = pd.DataFrame({
    "job_title": ["Data Analyst", "ML Engineer", "Data Analyst"],
    "required_skill": ["SQL", "Python", "Power BI"]
})

print("\nSample job data:")
print(jobs)
