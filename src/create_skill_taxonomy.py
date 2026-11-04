
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT = PROJECT_DIR / "data" / "processed" / "skill_taxonomy.csv"

skills = [
    ["Python", "Programming", "Python"],
    ["Java", "Programming", "Java"],
    ["C++", "Programming", "C++"],
    ["JavaScript", "Programming", "JavaScript"],
    ["TypeScript", "Programming", "TypeScript"],

    ["HTML", "Web Development", "HTML"],
    ["CSS", "Web Development", "CSS"],
    ["React", "Web Development", "React"],
    ["Node.js", "Web Development", "Node.js|Node JS"],

    ["SQL", "Databases", "SQL|Structured Query Language"],
    ["MySQL", "Databases", "MySQL"],
    ["PostgreSQL", "Databases", "PostgreSQL"],
    ["MongoDB", "Databases", "MongoDB"],

    ["Excel", "Data Analytics", "Excel|Microsoft Excel"],
    ["Power BI", "Data Analytics", "Power BI|Microsoft Power BI"],
    ["Tableau", "Data Analytics", "Tableau"],
    ["Pandas", "Data Analytics", "Pandas"],
    ["NumPy", "Data Analytics", "NumPy"],
    ["Statistics", "Data Analytics", "Statistics"],
    ["Data Analysis", "Data Analytics", "Data Analysis|Data Analytics"],
    ["Data Visualization", "Data Analytics", "Data Visualization"],

    ["Machine Learning", "AI & Machine Learning", "Machine Learning|ML"],
    ["Deep Learning", "AI & Machine Learning", "Deep Learning"],
    ["Natural Language Processing", "AI & Machine Learning", "Natural Language Processing|NLP"],
    ["Computer Vision", "AI & Machine Learning", "Computer Vision"],
    ["TensorFlow", "AI & Machine Learning", "TensorFlow"],
    ["PyTorch", "AI & Machine Learning", "PyTorch"],
    ["Scikit-learn", "AI & Machine Learning", "Scikit-learn|Sklearn"],
    ["Generative AI", "AI & Machine Learning", "Generative AI|GenAI"],
    ["Large Language Models", "AI & Machine Learning", "Large Language Models|LLMs"],

    ["Apache Spark", "Data Engineering & Cloud", "Apache Spark|Spark"],
    ["Hadoop", "Data Engineering & Cloud", "Hadoop"],
    ["ETL", "Data Engineering & Cloud", "ETL"],
    ["AWS", "Data Engineering & Cloud", "AWS|Amazon Web Services"],
    ["Azure", "Data Engineering & Cloud", "Azure|Microsoft Azure"],
    ["Google Cloud", "Data Engineering & Cloud", "Google Cloud|GCP"],

    ["Git", "Developer Tools", "Git"],
    ["GitHub", "Developer Tools", "GitHub"],
    ["Docker", "Developer Tools", "Docker"],
    ["Kubernetes", "Developer Tools", "Kubernetes"],

    ["Windows", "Operating Systems", "Windows"],
    ["Windows Server", "Operating Systems", "Windows Server"],
    ["System Administration", "Systems Administration", "System Administration|Systems Administration"],
    ["Server Administration", "Systems Administration", "Server Administration"],
    ["SCCM / MECM", "Systems Administration", "SCCM|MECM|Microsoft Endpoint Configuration Manager|System Center Configuration Manager"],
    ["Patch Management", "Systems Administration", "Patch Management|Patch Remediation"],

    ["IT Support", "IT Support", "IT Support"],
    ["Technical Support", "IT Support", "Technical Support"],
    ["Desktop Support", "IT Support", "Desktop Support"],
    ["Troubleshooting", "IT Support", "Troubleshooting"],
    ["Remote Support", "IT Support", "Remote Support"],
    ["Hardware Support", "IT Support", "Hardware Support|Computer Hardware"],

    ["Networking", "Networking", "Networking|Network Infrastructure"],
    ["LAN", "Networking", "LAN|Local Area Network"],
    ["WAN", "Networking", "WAN|Wide Area Network"],
    ["Cisco", "Networking", "Cisco"],
    ["Cisco ASA", "Networking", "Cisco ASA"],
    ["Palo Alto Networks", "Networking", "Palo Alto|Palo Alto Networks"],
    ["F5 Load Balancer", "Networking", "F5 Load Balancer|F5 Load Balancing"],

    ["Microsoft Defender", "Cybersecurity", "Microsoft Defender"],
    ["Microsoft Purview", "Cybersecurity", "Microsoft Purview"],
    ["CrowdStrike", "Cybersecurity", "CrowdStrike"],

    ["Data Center", "Cloud & Infrastructure", "Data Center|Datacenter"],
    ["Cloud Computing", "Cloud & Infrastructure", "Cloud Computing"],

    ["Agile", "Professional Competencies", "Agile|Agile Methodology"],
    ["Scrum", "Professional Competencies", "Scrum|Scrum Framework"],
    ["Project Management", "Professional Competencies", "Project Management"],

]

taxonomy = pd.DataFrame(
    skills,
    columns=["skill_name", "category", "aliases"]
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

taxonomy.to_csv(OUTPUT, index=False)

print("TECHNICAL SKILL TAXONOMY CREATED")
print("Total skills:", len(taxonomy))
print("\nSkills by category:")
print(taxonomy.groupby("category").size())
