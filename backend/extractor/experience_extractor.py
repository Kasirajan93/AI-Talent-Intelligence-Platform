import re


class ExperienceExtractor:
    """
    Extracts total work experience and job titles
    from resume text.
    """

    JOB_TITLES: list[str] = [
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Machine Learning Engineer",
        "AI Engineer",
        "Software Engineer",
        "Python Developer",
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "Business Analyst",
        "Project Manager",
        "Product Manager",
        "Doctor",
        "Ayurvedic Doctor",
        "Research Intern",
        "Intern"
    ]

    @staticmethod
    def extract(text: str) -> dict:
        """
        Extract total experience and detected job titles
        from resume text.
        """

        experience = {
            "total_experience": None,
            "job_titles": []
        }

        match = re.search(
            r"(\d+(?:\.\d+)?)\s*\+?\s*(years?|yrs?)",
            text,
            re.IGNORECASE
        )

        if match:
            experience["total_experience"] = match.group()

        text_lower = text.lower()

        for title in ExperienceExtractor.JOB_TITLES:
            pattern = r"\b" + re.escape(title.lower()) + r"\b"

            if re.search(pattern, text_lower):
                experience["job_titles"].append(title)

        experience["job_titles"] = sorted(
            set(experience["job_titles"])
        )

        return experience