from backend.extractor.name_extractor_v2 import NameExtractorV2
from backend.extractor.contact_extractor import ContactExtractor
from backend.extractor.skill_extractor import SkillExtractor
from backend.extractor.education_extractor import EducationExtractor
from backend.extractor.experience_extractor import ExperienceExtractor


class ResumeInformationExtractor:

    @staticmethod
    def extract(text):

        return {
            "name": NameExtractorV2.extract(text),
            "contact": ContactExtractor.extract(text),
            "skills": SkillExtractor.extract(text),
            "education": EducationExtractor.extract(text),
            "experience": ExperienceExtractor.extract(text)
        }