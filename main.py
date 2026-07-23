from backend.parser.parser import ResumeParser
from backend.preprocessing.text_cleaner import TextCleaner
from backend.extractor.resume_information_extractor import ResumeInformationExtractor
from pprint import pprint
from backend.jd_parser.jd_parser import JDParser

resume_path = "data/resumes/sample_resume.pdf"

# Parse Resume
raw_text = ResumeParser.extract_text(resume_path)

# Clean Text
clean_text = TextCleaner.clean(raw_text)

# Extract All Resume Information
resume_data = ResumeInformationExtractor.extract(clean_text)

print("\n===== RESUME INFORMATION =====\n")
pprint(resume_data)

# ===============================
# Job Description Parsing
# ===============================

jd_text = JDParser.read("data/job_descriptions/sample_jd.txt")

print("\n===== JOB DESCRIPTION =====\n")
print(jd_text)