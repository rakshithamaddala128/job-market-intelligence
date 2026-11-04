# 📊 Job Market Intelligence & Skill Gap Analyzer

An interactive data analytics project that compares Indian and global job markets, identifies in-demand technical skills, and analyzes differences in skill demand across job categories.

Built using Python, Pandas, Streamlit, and Plotly.

---

## 🎯 Project Overview

The Job Market Intelligence & Skill Gap Analyzer provides insights into employment trends and technical skill requirements using job posting datasets from India and the global market.

The project focuses on:

- Analyzing job market trends.
- Identifying in-demand technical skills.
- Comparing Indian and global skill demand.
- Classifying job roles into standardized categories.
- Identifying common and market-specific skills.
- Visualizing insights through an interactive dashboard.

---

## 📂 Datasets

The project uses two job market datasets:

### 1. Indian Job Market
- Source: Naukri.com job postings dataset.
- Dataset period: July–August 2019.
- Original records: Approximately 30,000.
- Cleaned job records: 29,418.

### 2. Global Job Market
- Source: LinkedIn job postings dataset.
- Dataset period: 2023–2024.
- Cleaned job records: 123,842.

**Note:** The datasets cover different time periods and are not a real-time representation of the current job market.

---

## ⚙️ Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Data Analysis | Exploratory Data Analysis |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Streamlit |
| Machine Learning | Scikit-learn |
| Development | VS Code, Jupyter Notebook |
| Version Control | Git, GitHub |

---

## 🔍 Project Workflow

1. Data collection from Indian and global job posting datasets.
2. Data cleaning and preprocessing.
3. Standardization of job role categories.
4. Creation of a skill taxonomy.
5. Extraction of skills from job postings.
6. Analysis of skill demand.
7. Comparison of Indian and global job markets.
8. Development of an interactive Streamlit dashboard.

---

## 📈 Key Findings

### Dataset Overview

| Metric | India | Global |
|---|---:|---:|
| Job Postings | 29,418 | 123,842 |
| Unique Detected Skills | 57 | 67 |
| Skill Coverage | 32.35% | 40.16% |

### Important Observations

- Programming skills show relatively higher demand in the Indian dataset.
- Data Analytics has a higher share of detected skill demand in the global dataset.
- Database-related skills have a notable presence in the Indian dataset.
- Professional competencies and project management skills show considerable demand globally.
- The analysis identified 57 common detected skills and 10 additional detected skills in the global dataset.

These findings describe the available datasets, not the entire job market.

---

## 📊 Dashboard Preview

### Market Overview

![Market Overview](screenshots/dashboard_overview.png)

### Skill Analysis

![Skill Analysis](screenshots/skill_analysis.png)

---

## 🖥️ Interactive Dashboard Features

The Streamlit dashboard contains five main sections:

1. **Market Overview** – Overall comparison of Indian and global job postings.
2. **Skill Analysis** – Exploration of in-demand technical skills.
3. **