import csv
import os
import re


class SkillExtractor:

    @staticmethod
    def load_skills():

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        skills_path = os.path.join(
            base_dir,
            "data",
            "knowledge_base",
            "skills.csv"
        )

        skills = []

        with open(skills_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                skills.append(row["skill"].strip())

        return skills

    @staticmethod
    def extract(text):

        text = text.lower()

        detected_skills = []

        skills = SkillExtractor.load_skills()

        for skill in skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):
                detected_skills.append(skill)

        return sorted(set(detected_skills))