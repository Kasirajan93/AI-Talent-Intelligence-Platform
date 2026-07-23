import re


class ExperienceExtractor:

    JOB_TITLES = [
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
    def extract(text):

        experience = {
            "total_experience": None,
            "job_titles": []
        }

        # Find experience like "7 years", "2.5 years"
        match = re.search(
            r"(\d+(?:\.\d+)?)\s*\+?\s*(years?|yrs?)",
            text,
            re.IGNORECASE
        )

        if match:
            experience["total_experience"] = match.group()

        # Find job titles
        text_lower = text.lower()

        for title in ExperienceExtractor.JOB_TITLES:
            if title.lower() in text_lower:
                experience["job_titles"].append(title)

        experience["job_titles"] = sorted(
            list(set(experience["job_titles"]))
        )

        return experience