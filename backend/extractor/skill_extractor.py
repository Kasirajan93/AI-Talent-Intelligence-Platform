import csv
import os
import re


class SkillExtractor:
    """
    Extracts technical skills from resume text using a predefined
    skills database stored in skills.csv.
    """

    _skills: list[str] | None = None

    @staticmethod
    def load_skills() -> list[str]:
        """
        Load skills from skills.csv.

        The skills are cached after the first read to avoid
        reading the CSV file for every resume.
        """

        if SkillExtractor._skills is not None:
            return SkillExtractor._skills

        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )

        skills_path = os.path.join(
            base_dir,
            "data",
            "knowledge_base",
            "skills.csv"
        )

        skills: list[str] = []

        with open(skills_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                skills.append(row["skill"].strip())

        SkillExtractor._skills = skills

        return SkillExtractor._skills

    @staticmethod
    def extract(text: str) -> list[str]:
        """
        Extract matching technical skills from resume text.

        Args:
            text: Cleaned resume text.

        Returns:
            A sorted list of unique detected skills.
        """

        text = text.lower()

        detected_skills: list[str] = []

        skills = SkillExtractor.load_skills()

        for skill in skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):
                detected_skills.append(skill)

        return sorted(set(detected_skills))