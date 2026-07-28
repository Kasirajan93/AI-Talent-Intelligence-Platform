from backend.matcher.skill_normalizer import SkillNormalizer


class ResumeJDMatcher:
    """
    Matches resume skills against job description skills
    and calculates the match percentage.
    """

    @staticmethod
    def match(
        resume_data: dict,
        jd_data: dict
    ) -> dict:

        resume_skills = set(
            SkillNormalizer.normalize(skill)
            for skill in resume_data["skills"]
        )

        jd_skills = set(
            SkillNormalizer.normalize(skill)
            for skill in jd_data["required_skills"]
        )

        matched_skills = sorted(
            resume_skills.intersection(jd_skills))

        missing_skills = sorted(
            jd_skills.difference(resume_skills))

        if len(jd_skills) == 0:
            match_percentage = 0
        else:
            match_percentage = round(
                (len(matched_skills) / len(jd_skills)) * 100,
                2
            )

        return {

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "match_percentage": match_percentage

        }

