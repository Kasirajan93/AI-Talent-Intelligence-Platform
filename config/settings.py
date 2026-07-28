from pathlib import Path

# ======================================================
# Project Root
# ======================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================================================
# Data Directories
# ======================================================
DATA_DIR = BASE_DIR / "data"

RESUME_DIR = DATA_DIR / "resumes"
JD_DIR = DATA_DIR / "job_descriptions"
KNOWLEDGE_BASE_DIR = DATA_DIR / "knowledge_base"

# ======================================================
# Knowledge Base Files
# ======================================================
SKILLS_FILE = KNOWLEDGE_BASE_DIR / "skills.csv"
SKILL_ALIASES_FILE = KNOWLEDGE_BASE_DIR / "skill_aliases.csv"
JOB_ROLES_FILE = KNOWLEDGE_BASE_DIR / "job_roles.csv"
CERTIFICATIONS_FILE = KNOWLEDGE_BASE_DIR / "certifications.csv"
COMPANIES_FILE = KNOWLEDGE_BASE_DIR / "companies.csv"
UNIVERSITIES_FILE = KNOWLEDGE_BASE_DIR / "universities.csv"

# ======================================================
# Output Directory
# ======================================================
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# ======================================================
# Supported File Types
# ======================================================
SUPPORTED_RESUME_EXTENSIONS = [".pdf", ".docx", ".txt"]