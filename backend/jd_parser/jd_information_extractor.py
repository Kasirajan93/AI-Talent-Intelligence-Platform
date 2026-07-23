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

        # ---------- Job Title ----------
        lines = [line.strip() for line in jd_text.split("\n") if line.strip()]

        if lines:
            jd["job_title"] = lines[0]

        # ---------- Experience ----------
        match = re.search(
            r"(\d+\+?\s*(?:years?|yrs?))",
            jd_text,
            re.IGNORECASE
        )

        if match:
            jd["experience"] = match.group()

        # ---------- Education ----------
        education_match = re.search(
            r"(Bachelor.*|Master.*|B\.Tech.*|B\.E.*|BAMS.*)",
            jd_text,
            re.IGNORECASE
        )

        if education_match:
            jd["education"] = education_match.group().strip()

        # ---------- Skills ----------
        skills = SkillExtractor.extract(jd_text)

        jd["required_skills"] = skills

        return jd