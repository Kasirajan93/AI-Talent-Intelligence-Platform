from backend.extractor.candidate_name_extractor import CandidateNameExtractor
from backend.extractor.contact_extractor import ContactExtractor
from backend.extractor.skill_extractor import SkillExtractor
from backend.extractor.education_extractor import EducationExtractor
from backend.extractor.experience_extractor import ExperienceExtractor


class ResumeInformationExtractor:
    """
    Extracts structured information from cleaned resume text.
    """

    @staticmethod
    def extract(text: str) -> dict:

        return {
            "name" : CandidateNameExtractor.extract(text),
            "contact": ContactExtractor.extract(text),
            "skills": SkillExtractor.extract(text),
            "education": EducationExtractor.extract(text),
            "experience": ExperienceExtractor.extract(text)
        }