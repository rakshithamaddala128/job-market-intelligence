
import pandas as pd
import re
from pathlib import Path

INPUT_FILE = Path("data/processed/india_jobs_clean.csv")
OUTPUT_FILE = Path("data/processed/india_jobs_classified.csv")


def clean_text(value):
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value).lower().strip())


def matches(text, patterns):
    return any(re.search(p, text) for p in patterns)


AI_PATTERNS = [
    r"\bdata scientist\b",
    r"\bdata science director\b",
    r"\bdirector\s*[-,]?\s*data science\b",
    r"\bmachine learning\b",
    r"\bdeep learning\b",
    r"\bartificial intelligence\b",
    r"\bartifical intelligence\b",
    r"\bai\s*/\s*ml\b",
    r"\bml\s*/\s*ai\b",
    r"\bai engineer\b",
    r"\bai developer\b",
    r"\bml engineer\b",
    r"\bml developer\b",
    r"\bnlp engineer\b",
    r"\bcomputer vision\b",
    r"\bneural network\b",
    r"\bspeech scientist\b",
    r"\bdata science consultant\b",
    r"\bconsultant.*machine learning\b",
    r"\bmachine learning.*consultant\b",
    r"\bautomation solution architect.*machine learning\b",
    r"\bprincipal machine learning\b",
    r"\bproduct development engineer.*machine learning\b"
]

QA_PATTERNS = [
    r"\bquality assurance\b",
    r"\bqa engineer\b",
    r"\bqa analyst\b",
    r"\bqa manager\b",
    r"\bquality analyst\b",
    r"\bsoftware tester\b",
    r"\bsoftware testing\b",
    r"\bsoftware test engineer\b",
    r"\btest engineer\b",
    r"\btesting engineer\b",
    r"\bautomation test",
    r"\bmanual test",
    r"\bperformance test",
    r"\bsystem test",
    r"\bembedded test",
    r"\bmobile app testing\b",
    r"\btesting of mobile app\b",
    r"\bhil test\b",
    r"\bselenium\b",
    r"\bqtp\b",
    r"\btest automation\b",
    r"\btesting analyst\b",
    r"\bsdet\b",
    r"\bpenetration testing\b"
]

INFRA_PATTERNS = [
    r"\bdev[\s-]?ops\b",
    r"\bsystem administrator\b",
    r"\bsystems administrator\b",
    r"\bsystem admin\b",
    r"\bsysadmin\b",
    r"\bnetwork administrator\b",
    r"\bnetwork admin\b",
    r"\bnetwork engineer\b",
    r"\bnetwork security\b",
    r"\blinux administrator\b",
    r"\blinux architect\b",
    r"\bsystem architect.*linux\b",
    r"\bwindows administrator\b",
    r"\bserver administrator\b",
    r"\bdatabase administrator\b",
    r"\boracle dba\b",
    r"\bsql dba\b",
    r"\bsybase database administrator\b",
    r"\bdba\b",
    r"\bcloud engineer\b",
    r"\bcloud administrator\b",
    r"\bazure.*(engineer|architect|administrator|paas)\b",
    r"\b(microsoft windows azure|windows azure)\b",
    r"\binfrastructure engineer\b",
    r"\binfrastructure administrator\b",
    r"\binfrastructure support\b",
    r"\bsite reliability engineer\b",
    r"\bsre\b",
    r"\bcyber ?security\b",
    r"\binformation security\b",
    r"\bsecurity engineer\b",
    r"\bsecurity analyst\b",
    r"\bsecurity operations\b",
    r"\bpenetration testing\b",
    r"\bdesktop support\b",
    r"\bdesktop engineer\b",
    r"\bit support\b",
    r"\bhardware & networking\b",
    r"\bhardware and networking\b",
    r"\bhardware engineer\b",
    r"\btechnical support\b",
    r"\bhelp ?desk\b",
    r"\bdata center operator\b",
    r"\bdata centre operator\b",
    r"\bcitrix\b",
    r"\bmiddleware administrator\b",
    r"\bcloud operations\b",
    r"\bnetwork operations\b",
    r"\bbig data support\b",
    r"\bhadoop administrator\b",
    r"\bplatform administrator\b",
    r"\bdatabase administration\b",
    r"\bunix administrator\b",
    r"\bnetwork jobs\b",
    r"\bcisco voice engineer\b",
    r"\bcompiler support engineer\b",
    r"\btfs admin\b"
]

ANALYTICS_PATTERNS = [
    r"\bdata analyst\b",
    r"\bdata engineer\b",
    r"\bbig data (developer|architect|engineer|lead)\b",
    r"\bbig data lead developer\b",
    r"\bhadoop (developer|engineer)\b",
    r"\blead.*hadoop.*engineer\b",
    r"\bsenior.*hadoop.*engineer\b",
    r"\b(etl|extract transform load) (developer|engineer)\b",
    r"\betl developer\b",
    r"\binformatica\b",
    r"\bdatastage\b",
    r"\bdata warehouse\b",
    r"\bdatawarehousing\b",
    r"\bdata warehousing\b",
    r"\bdata management developer\b",
    r"\bteradata\b",
    r"\bssis\b",
    r"\bssrs\b",
    r"\bssas\b",
    r"\bpower ?bi\b",
    r"\btableau\b",
    r"\bqlik(view|sense)?\b",
    r"\bcognos\b",
    r"\bbusiness objects\b",
    r"\bbusiness intelligence\b",
    r"\banalytics\b",
    r"\bmis executive\b",
    r"\bmis coordinator\b",
    r"\breporting analyst\b",
    r"\bsas (programmer|developer|analyst)\b",
    r"\bmdm developer\b",
    r"\bdata integration\b",
    r"\bweb data analyst\b",
    r"\bmicrostrategy\b",
    r"\bdecision support\b",
    r"\badobe analytics\b",
    r"\bsap bw\b",
    r"\bdata modelling\b",
    r"\bdata modeling\b",
    r"\bdata analysis\b",
    r"\bdata analysis.*reporting\b"
]

SOFTWARE_PATTERNS = [
    r"\bsoftware (developer|engineer|programmer)\b",
    r"\bsoftware development engineer\b",
    r"\bsoftware programmer\b",
    r"\bsoftware engineering lead\b",
    r"\bsoftware engineer.*backend\b",
    r"\bapplication developer\b",
    r"\bapplication programmer\b",
    r"\bbackend (developer|engineer|programmer)\b",
    r"\bback end (developer|engineer)\b",
    r"\bfrontend (developer|engineer)\b",
    r"\bfront end (developer|engineer)\b",
    r"\bfull[\s-]?stack (developer|engineer)\b",
    r"\bweb (developer|programmer)\b",
    r"\bui developer\b",
    r"\bapi developer\b",
    r"\bmobile application developer\b",
    r"\bmobile app developer\b",
    r"\bapp developer\b",
    r"\bandroid developer",
    r"\bios developer",
    r"\bflutter developer\b",
    r"\bionic developer\b",
    r"\bjava\b",
    r"\bpython developer\b",
    r"\bphp developer",
    r"\bcodeigniter\b",
    r"\b\.net\b",
    r"\bdot[\s-]?net\b",
    r"\basp\.?net\b",
    r"\bc# developer\b",
    r"\bc\+\+ developer\b",
    r"\bnode\.?js\b",
    r"\bangular(js)?\b",
    r"\breact(js)?\b",
    r"\bruby on rails\b",
    r"\bjavascript developer\b",
    r"\bwordpress developer\b",
    r"\bshopify developer\b",
    r"\bmagento developer\b",
    r"\bdrupal developer\b",
    r"\bsalesforce(\.com)? developer\b",
    r"\bsfdc developer\b",
    r"\bsharepoint developer\b",
    r"\bservicenow developer\b",
    r"\bsap abap\b",
    r"\bsap developer\b",
    r"\bsap concur developer\b",
    r"\boracle apps (technical )?(developer|consultant)\b",
    r"\boracle atg\b",
    r"\boracle adf\b",
    r"\boaf developer\b",
    r"\btibco developer\b",
    r"\bhybris developer\b",
    r"\baem developer\b",
    r"\bpega(system)? developer\b",
    r"\bpegasystemdeveloper\b",
    r"\bodoo developer\b",
    r"\bcrm developer(s)?\b",
    r"\berp developer\b",
    r"\bmainframe developer\b",
    r"\bcobol developer\b",
    r"\brpg developer\b",
    r"\bas400 developer\b",
    r"\bmulesoft developer\b",
    r"\bwtx/itx developer\b",
    r"\bbsp engineer\b",
    r"\bhpc developer\b",
    r"\bcompiler engineer\b",
    r"\bcompiler developer\b",
    r"\bembedded software (developer|engineer)\b",
    r"\bembedded developer\b",
    r"\bkernel programmer\b",
    r"\bdevice driver developer\b",
    r"\bwindows driver developer\b",
    r"\brpa developer\b",
    r"\bvba developer\b",
    r"\bblockchain developer\b",
    r"\bdatabase developer\b",
    r"\bsql developer\b",
    r"\balgorithm developer\b",
    r"\bui.*developer\b",
    r"\bdeveloper.*ui\b",
    r"\bmainframe programmer\b",
    r"\bodi developer\b",
    r"\bsoftware engineer\b",
    r"\bsenior programmer\b",
    r"\bprogrammer(s)?\b",
    r"\btrainee software engineer(s)?\b",
    r"\bsoftware testing tool developer\b"
]


def classify_job(row):
    title = clean_text(row.get("job_title", ""))
    functional = clean_text(row.get("functional_area", ""))
    role = clean_text(row.get("role_category", ""))

    metadata = f"{functional} {role}"
    combined = f"{title} {metadata}"

    if not title:
        return "Other", True

    # Exclude clearly non-IT job families
    if matches(title, [
        r"\bsales\b",
        r"\bbusiness development\b",
        r"\bpre[\s-]?sales\b",
        r"\brecruiter\b",
        r"\bhr executive\b",
        r"\baccountant\b",
        r"\baccounts executive\b",
        r"\bsecurity guard\b",
        r"\bmechanical design engineer\b",
        r"\belevator.*engineer\b",
        r"\bcnc.*sales\b",
        r"\bcontent developer\b",
        r"\binstructional designer\b",
        r"\bgraphic designer\b",
        r"\bweb designer\b",
        r"\bcampaign developer\b",
        r"\bemail developer\b",
        r"\bclinical data programmer\b",
        r"\bcnc programmer\b",
        r"\bprocess developer\b",
        r"\bdata entry\b",
        r"\bcall center\b",
        r"\bcall centre\b"
    ]):
        return "Other", False

    # AI and Machine Learning
    if matches(title, AI_PATTERNS):
        if matches(metadata, [
            r"\bmedical\b",
            r"\bclinical\b",
            r"\bhealthcare\b",
            r"\bpharmaceutical",
            r"\bbiotechnology\b",
            r"\bmedical professional\b"
        ]):
            return "Other", True

        if matches(title, [
            r"\btrainer\b",
            r"\bprofessor\b",
            r"\bfaculty\b"
        ]):
            return "Other", True

        if matches(title, [
            r"\bresearch scholar\b",
            r"\bdirector\b",
            r"\bmanager\b",
            r"\bassociate manager\b"
        ]):
            return "AI & Machine Learning", True

        if matches(title, [r"\balgorithm developer\b"]) and not matches(
            title,
            [r"\bmachine learning\b", r"\bartificial intelligence\b", r"\bdeep learning\b"]
        ):
            return "Software Development", False

        if matches(title, [r"\bdata scientist\b"]):
            return "AI & Machine Learning", False

        return "AI & Machine Learning", False

    # Quality Assurance
    if matches(title, QA_PATTERNS):
        if matches(functional, [
            r"\bmanufactur",
            r"\bproduction\b",
            r"\bmechanical\b"
        ]) and not matches(title, [
            r"\bsoftware\b",
            r"\bautomation test\b",
            r"\bselenium\b",
            r"\bmobile app testing\b",
            r"\btesting of mobile app\b"
        ]):
            return "Other", True

        return "Quality Assurance", False

    # IT and Infrastructure
    if matches(title, INFRA_PATTERNS):
        if matches(title, [
            r"\btechnical support\b",
            r"\bproduct support\b",
            r"\bcustomer support\b",
            r"\binbound technical support\b"
        ]) and matches(metadata, [
            r"\bites\b",
            r"\bbpo\b",
            r"\bvoice\b",
            r"\bcustomer service\b"
        ]) and not matches(title, [
            r"\bnetwork\b",
            r"\bserver\b",
            r"\bdesktop\b",
            r"\bcloud\b",
            r"\bdatabase\b",
            r"\bsystem\b",
            r"\binfrastructure\b",
            r"\bsecurity\b",
            r"\bdevops\b",
            r"\blinux\b",
            r"\bwindows\b"
        ]):
            return "Other", True

        if matches(title, [
            r"\btechnical support\b",
            r"\bproduct support\b",
            r"\bdesktop engineer\b",
            r"\bhardware engineer\b"
        ]):
            return "IT & Infrastructure", True

        if matches(metadata, [
            r"\bsales\b",
            r"\bretail sales\b"
        ]) and not matches(title, [
            r"\bnetwork\b",
            r"\bsecurity\b",
            r"\bdevops\b",
            r"\bcloud\b",
            r"\bdatabase\b",
            r"\badministrator\b"
        ]):
            return "Other", True

        return "IT & Infrastructure", False

    # Data Analytics
    if matches(title, ANALYTICS_PATTERNS):
        if matches(metadata, [
            r"\bpre[\s-]?sales\b",
            r"\bretail sales\b",
            r"\binstitutional sales\b",
            r"\bmedical professional\b"
        ]):
            return "Other", True

        if matches(title, [
            r"\bmanager\b",
            r"\bdirector\b",
            r"\bhead\b",
            r"\blead\b"
        ]):
            return "Data Analytics", True

        if matches(title, [
            r"\bmis executive\b",
            r"\bdata analyst\b",
            r"\bdata analysis\b",
            r"\bbig data analyst\b"
        ]) and matches(metadata, [
            r"\bbpo\b",
            r"\bites\b",
            r"\bvoice\b",
            r"\bcustomer service\b"
        ]):
            return "Data Analytics", True

        if matches(title, [
            r"\binformatica administration\b",
            r"\bdatabase administration\b"
        ]):
            return "IT & Infrastructure", True

        return "Data Analytics", False

    # Software Development
    if matches(title, SOFTWARE_PATTERNS):
        if matches(title, [
            r"\btool developer\b"
        ]) and matches(title, [
            r"\barticulate\b",
            r"\bcaptivate\b"
        ]):
            return "Other", True

        if matches(title, [
            r"\bindustrial automation\b",
            r"\bautomation.*industrial\b"
        ]):
            return "Other", True

        if matches(title, [
            r"\bsoftware engineer\b",
            r"\bsoftware engineering\b"
        ]) and matches(functional, [
            r"\bengineering design\b",
            r"\bproduction\b",
            r"\bmanufacturing\b"
        ]):
            return "Software Development", True

        if matches(title, [
            r"\bdeveloper\b",
            r"\bengineer\b"
        ]) and matches(title, [
            r"\bui/ux\b",
            r"\bdesigner\b"
        ]):
            return "Software Development", True

        return "Software Development", False

    # Ambiguous technical roles: keep in Other and request review
    review_patterns = [
        r"\bdeveloper\b",
        r"\bprogrammer\b",
        r"\bengineer\b",
        r"\barchitect\b",
        r"\bconsultant\b",
        r"\btechnical support\b",
        r"\bsupport engineer\b",
        r"\bdata migration\b",
        r"\bdata management\b",
        r"\btester\b",
        r"\btesting\b",
        r"\bcloud\b",
        r"\bbig data\b",
        r"\bsecurity\b",
        r"\bdatabase\b",
        r"\bnetwork\b",
        r"\bdesktop\b",
        r"\bmainframe\b",
        r"\bcompiler\b",
        r"\bsap\b",
        r"\boracle\b",
        r"\bsql\b",
        r"\bjava\b",
        r"\bpython\b",
        r"\bwindows\b",
        r"\blinux\b",
        r"\bdata scientist\b",
        r"\banalyst\b",
        r"\bdata analysis\b",
        r"\bdata science\b",
        r"\bapplication\b",
        r"\bsoftware\b",
        r"\bplatform\b",
        r"\btrainee\b",
        r"\bgraduate engineer\b"
    ]

    return "Other", matches(title, review_patterns)


def main():
    df = pd.read_csv(INPUT_FILE)

    results = df.apply(classify_job, axis=1)

    df["role_category_standard"] = [result[0] for result in results]
    df["manual_review"] = [result[1] for result in results]

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nINDIA JOB CLASSIFICATION - VERSION 9")
    print("=" * 50)

    print(f"Total records: {len(df):,}")

    counts = df["role_category_standard"].value_counts()
    percentages = (counts / len(df) * 100).round(2)

    print("\nCATEGORY COUNTS")
    print(counts.to_string())

    print("\nCATEGORY PERCENTAGES")
    print(percentages.to_string())

    print("\nMANUAL REVIEW")
    print(df["manual_review"].value_counts().to_string())

    print("\nMANUAL REVIEW PERCENTAGE")
    print(
        (df["manual_review"].value_counts(normalize=True) * 100)
        .round(2)
        .to_string()
    )

    print(f"\nSaved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
