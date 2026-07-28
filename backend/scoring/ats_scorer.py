import re

from backend.matcher.skill_normalizer import SkillNormalizer

class ATSScorer:
    """
    Calculates ATS scores based on skill matching,
    experience, education, and certifications.
    """

    # Weight distribution
    REQUIRED_SKILLS_WEIGHT = 50
    PREFERRED_SKILLS_WEIGHT = 15
    EXPERIENCE_WEIGHT = 20
    EDUCATION_WEIGHT = 10
    CERTIFICATION_WEIGHT = 5

    @staticmethod
    def score(
         resume_data: dict,
         jd_data: dict,
         match_result: dict
    ) -> dict:
        """
        Calculate the ATS score and hiring recommendation
        for a resume against a job description.
        """

        score = {
            "required_skills_score": 0,
            "preferred_skills_score": 0,
            "experience_score": 0,
            "education_score": 0,
            "certification_score": 0,
            "total_score": 0,
            "rating": "",
            "recommendation": "",
            "hiring_decision": ""
        }

        # ------------------------
        # Required Skills
        # ------------------------

        required = len(jd_data["required_skills"])
        matched = len(match_result["matched_skills"])

        if required > 0:
            score["required_skills_score"] = round(
                (matched / required)
                * ATSScorer.REQUIRED_SKILLS_WEIGHT,
                2
            )

        # ------------------------
        # Preferred Skills
        # ------------------------

        preferred = {
            SkillNormalizer.normalize(skill)
            for skill in jd_data["preferred_skills"]
        }

        resume_skills = {
            SkillNormalizer.normalize(skill)
            for skill in resume_data["skills"]
        }

        matched_preferred = len(
            preferred.intersection(resume_skills)
)

        if len(preferred) > 0:

            score["preferred_skills_score"] = round(
                (
                    matched_preferred
                    / len(preferred)
                )
                * ATSScorer.PREFERRED_SKILLS_WEIGHT,
                2
            )

        # ------------------------
        # Experience
        # ------------------------

        resume_exp = resume_data["experience"]["total_experience"]
        jd_exp = jd_data["experience"]

        if resume_exp and jd_exp:

            resume_match = re.search(r"\d+", str(resume_exp))
            jd_match = re.search(r"\d+", str(jd_exp))

            resume_years = int(resume_match.group()) if resume_match else 0
            jd_years = int(jd_match.group()) if jd_match else 0

            if resume_years >= jd_years:
                score["experience_score"] = ATSScorer.EXPERIENCE_WEIGHT

        # ------------------------
        # Education
        # ------------------------

        if resume_data["education"]["degree"]:

            score["education_score"] = ATSScorer.EDUCATION_WEIGHT

        # ------------------------
        # Certifications
        # ------------------------

        # Future enhancement
        score["certification_score"] = 0

        # ------------------------
        # Final Score
        # ------------------------

        score["total_score"] = round(

            score["required_skills_score"]
            + score["preferred_skills_score"]
            + score["experience_score"]
            + score["education_score"]
            + score["certification_score"],

            2
        )

        # ------------------------
        # Rating & Recommendation
        # ------------------------

        if score["total_score"] >= 90:

            score["rating"] = "★★★★★"
            score["recommendation"] = "Strongly Recommended"
            score["hiring_decision"] = "Shortlist"

        elif score["total_score"] >= 75:

            score["rating"] = "★★★★☆"
            score["recommendation"] = "Recommended"
            score["hiring_decision"] = "Shortlist"

        elif score["total_score"] >= 60:

            score["rating"] = "★★★☆☆"
            score["recommendation"] = "Consider"
            score["hiring_decision"] = "Hold"

        elif score["total_score"] >= 40:

            score["rating"] = "★★☆☆☆"
            score["recommendation"] = "Weak Match"
            score["hiring_decision"] = "Review"

        else:

            score["rating"] = "★☆☆☆☆"
            score["recommendation"] = "Not Recommended"
            score["hiring_decision"] = "Reject"

        return score


            

