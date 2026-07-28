import re
from backend.extractor.skill_extractor import SkillExtractor


class JDInformationExtractor:

    @staticmethod
    def extract(jd_text):

        jd = {
            "job_title": None,
            "required_skills": [],
            "preferred_skills": [],
            "experience": None,
            "education": None
        }

        # ----------------------------
        # Job Title
        # ----------------------------
        lines = [line.strip() for line in jd_text.split("\n") if line.strip()]
        if lines:
            jd["job_title"] = lines[0]

        # ----------------------------
        # Experience
        # ----------------------------
        exp = re.search(r'(\d+\+?\s*years?)', jd_text, re.IGNORECASE)
        if exp:
            jd["experience"] = exp.group(1)

        # ----------------------------
        # Education
        # ----------------------------
        edu = re.search(
            r'Education:\s*(.*)',
            jd_text,
            re.IGNORECASE
        )

        if edu:
            jd["education"] = edu.group(1).strip()

        # ----------------------------
        # Required Skills Section
        # ----------------------------
        required_match = re.search(
            r"Required Skills:(.*?)(Preferred:|Education:|$)",
            jd_text,
            re.DOTALL | re.IGNORECASE
        )

        if required_match:
            required_text = required_match.group(1)

            

            jd["required_skills"] = SkillExtractor.extract(required_text)

            

        # ----------------------------
        # Preferred Skills Section
        # ----------------------------
        preferred_match = re.search(
            r"Preferred:(.*?)(Education:|$)",
            jd_text,
            re.DOTALL | re.IGNORECASE
        )

        if preferred_match:
            preferred_text = preferred_match.group(1)
            jd["preferred_skills"] = SkillExtractor.extract(preferred_text)

        return jd