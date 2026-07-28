from knowledge_sources.programming_languages import PROGRAMMING_LANGUAGES
from knowledge_sources.databases import DATABASES
from knowledge_sources.data_science import DATA_SCIENCE
from knowledge_sources.machine_learning import MACHINE_LEARNING
from knowledge_sources.deep_learning import DEEP_LEARNING
from knowledge_sources.cloud import CLOUD
from knowledge_sources.devops import DEVOPS
from knowledge_sources.version_control import VERSION_CONTROL
from knowledge_sources.business_intelligence import BUSINESS_INTELLIGENCE
import pandas as pd

from config.settings import (
    KNOWLEDGE_BASE_DIR,
    SKILLS_FILE,
    SKILL_ALIASES_FILE,
    JOB_ROLES_FILE,
    CERTIFICATIONS_FILE,
    COMPANIES_FILE,
    UNIVERSITIES_FILE,
)

# ======================================================
# Skills
# ======================================================

skills = []

for skill in PROGRAMMING_LANGUAGES:
    skills.append({
        "skill": skill,
        "category": "Programming",
        "subcategory": "Language"
    })

for skill in DATABASES:
    skills.append({
        "skill": skill,
        "category": "Database",
        "subcategory": "Database"
    })

for skill in DATA_SCIENCE:
    skills.append({
        "skill": skill,
        "category": "Data Science",
        "subcategory": "Core"
    })

for skill in MACHINE_LEARNING:
    skills.append({
        "skill": skill,
        "category": "Machine Learning",
        "subcategory": "Core"
    })

for skill in DEEP_LEARNING:
    skills.append({
        "skill": skill,
        "category": "Deep Learning",
        "subcategory": "Core"
    })

for skill in CLOUD:
    skills.append({
        "skill": skill,
        "category": "Cloud",
        "subcategory": "Core"
    })

for skill in DEVOPS:
    skills.append({
        "skill": skill,
        "category": "DevOps",
        "subcategory": "Core"
    })

for skill in VERSION_CONTROL:
    skills.append({
        "skill": skill,
        "category": "Version Control",
        "subcategory": "Core"
    })    

for skill in BUSINESS_INTELLIGENCE:
    skills.append({
        "skill": skill,
        "category": "Business Intelligence",
        "subcategory": "Visualization"
    })


# ======================================================
# Skill Aliases
# ======================================================

aliases = [
    {"alias": "ML", "standard_skill": "Machine Learning"},
    {"alias": "DL", "standard_skill": "Deep Learning"},
    {"alias": "AI", "standard_skill": "Artificial Intelligence"},
    {"alias": "JS", "standard_skill": "JavaScript"},
    {"alias": "K8s", "standard_skill": "Kubernetes"},
]

# ======================================================
# Job Roles
# ======================================================

roles = [
    {"role": "Data Scientist", "domain": "Data"},
    {"role": "Data Engineer", "domain": "Data"},
    {"role": "ML Engineer", "domain": "AI"},
    {"role": "Backend Developer", "domain": "Software"},
    {"role": "Frontend Developer", "domain": "Software"},
    {"role": "DevOps Engineer", "domain": "Cloud"},
]

# ======================================================
# Certifications
# ======================================================

certifications = [
    {"certification": "AWS Certified Cloud Practitioner", "vendor": "AWS"},
    {"certification": "AWS Solutions Architect Associate", "vendor": "AWS"},
    {"certification": "Microsoft Azure Fundamentals", "vendor": "Microsoft"},
]

# ======================================================
# Companies
# ======================================================

companies = [
    {"company": "Google", "industry": "Technology"},
    {"company": "Microsoft", "industry": "Technology"},
    {"company": "Amazon", "industry": "Technology"},
    {"company": "Infosys", "industry": "IT Services"},
]

# ======================================================
# Universities
# ======================================================

universities = [
    {"university": "Anna University", "country": "India"},
    {"university": "IIT Madras", "country": "India"},
    {"university": "Stanford University", "country": "USA"},
]

# ======================================================
# Save CSV Files
# ======================================================

KNOWLEDGE_BASE_DIR.mkdir(parents=True, exist_ok=True)

pd.DataFrame(skills).to_csv(SKILLS_FILE, index=False)
pd.DataFrame(aliases).to_csv(SKILL_ALIASES_FILE, index=False)
pd.DataFrame(roles).to_csv(JOB_ROLES_FILE, index=False)
pd.DataFrame(certifications).to_csv(CERTIFICATIONS_FILE, index=False)
pd.DataFrame(companies).to_csv(COMPANIES_FILE, index=False)
pd.DataFrame(universities).to_csv(UNIVERSITIES_FILE, index=False)

print("Knowledge base generated successfully!")