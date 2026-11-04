
import pandas as pd

jobs = pd.read_csv(
    "data/processed/global_jobs_clean.csv",
    usecols=["job_id", "title"]
)

jobs["title_clean"] = (
    jobs["title"]
    .str.lower()
    .str.strip()
)

role_keywords = {
    "AI & Machine Learning": [
        "machine learning",
        "ml engineer",
        "ai engineer",
        "ai/ml",
        "artificial intelligence",
        "deep learning",
        "data scientist",
        "nlp engineer",
        "computer vision"
    ],

    "Data Analytics": [
        "data analyst",
        "business analyst",
        "business intelligence",
        "bi analyst",
        "analytics",
        "reporting analyst",
        "data engineer",
        "data architect",
        "data modeler",
        "power bi developer",
        "etl developer",
        "sql developer",
        "business systems analyst",
        "business system analyst",
        "geographic information systems analyst",
        "gis analyst",
        "principal statistical programmer",
        "snowflake developer",
        "tableau developer",
        "power bi architect",
        "sas developer",
        "big data developer",
        "big data engineer",
        "lead big data engineer"
    ],

    "Software Development": [
        "software engineer",
        "software development engineer",
        "software developer",
        "full stack",
        "frontend developer",
        "front-end developer",
        "front end developer",
        "front end engineer",
        "front-end engineer",
        "backend",
        "back end",
        "web developer",
        "application developer",
        "java developer",
        "python developer",
        "dotnet developer",
        ".net developer",
        "salesforce developer",
        "react developer",
        "android developer",
        "ios developer",
        "ruby on rails developer",
        "java technical lead",
        "senior developer",
        "technical lead",
        "mainframe developer",
        "axiom developer",
        "drupal developer",
        "appian developer",
        "aem developer",
        "sharepoint developer",
        "angular developer",
        "php developer",
        "react native developer",
        "scala developer",
        "pega developer",
        "flutter developer",
        "golang developer",
        "software architect",
        "pl/sql developer",
        "oracle pl/sql developer"
    ],

    "IT & Infrastructure": [
        "cybersecurity data engineer",
        "servicenow technical business systems analyst",
        "technical project manager",
        "technical program manager",
        "chief technology officer",
        "information technology manager",
        "database manager",
        "site reliability engineer",
        "cloud solutions architect",
        "cloud infrastructure engineer",
        "software support specialist",
        "mainframe engineer",
        "it support",
        "it specialist",
        "information technology support",
        "information technology technician",
        "technical support",
        "system administrator",
        "systems administrator",
        "system engineer",
        "systems engineer",
        "system analyst",
        "systems analyst",
        "network engineer",
        "network administrator",
        "network architect",
        "cloud engineer",
        "cloud architect",
        "database administrator",
        "database developer",
        "devops",
        "cybersecurity",
        "cyber security",
        "information security",
        "application security",
        "security engineer",
        "security architect",
        "security analyst",
        "servicenow developer",
        "data center technician",
        "datacenter technician",
        "it project manager",
        "it manager"
    ],

    "Quality Assurance": [
        "software quality assurance",
        "software qa",
        "qa engineer",
        "qa analyst",
        "qa tester",
        "software tester",
        "automation tester",
        "test automation",
        "performance test engineer",
        "software test engineer",
        "test engineer - software",
        "selenium tester",
        "tosca automation engineer"
    ]
}


def classify_role(title):

    if pd.isna(title):
        return "Other"

    title = title.lower().strip()

    if "pl/sql developer" in title or "pl sql developer" in title:
        return "Software Development"

    if "product compliance qa engineer" in title:
        return "Other"

    for category, keywords in role_keywords.items():

        for keyword in keywords:

            if keyword in title:
                return category

    return "Other"


jobs["role_category"] = jobs["title_clean"].apply(classify_role)


print("\nTOTAL JOB POSTINGS:", len(jobs))

print("\nROLE CATEGORY COUNTS:")
print(jobs["role_category"].value_counts())

print("\nSAMPLE CLASSIFIED JOBS:")

for category in role_keywords:

    print("\n", category)

    print(
        jobs[jobs["role_category"] == category]["title"]
        .drop_duplicates()
        .head(25)
        .to_string(index=False)
    )


output_path = "data/processed/global_jobs_classified.csv"

jobs.to_csv(output_path, index=False)

print("\nCLASSIFICATION COMPLETED")
print("Saved file:", output_path)
