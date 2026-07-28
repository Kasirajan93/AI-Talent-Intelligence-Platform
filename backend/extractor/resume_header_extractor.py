import re


class ResumeHeaderExtractor:
    """
    Extracts the header section of a resume.

    The header usually contains:
    - Name
    - Designation
    - Email
    - Phone
    - Location
    - LinkedIn
    - GitHub
    """

    HEADER_STOP_WORDS = {
        "PROFILE",
        "SUMMARY",
        "PROFESSIONAL SUMMARY",
        "CAREER SUMMARY",
        "OBJECTIVE",
        "WORK EXPERIENCE",
        "EXPERIENCE",
        "EMPLOYMENT",
        "PROJECTS",
        "EDUCATION",
        "TECHNICAL SKILLS",
        "SKILLS",
        "CERTIFICATIONS",
        "ACADEMICS",
        "PROFESSIONAL EXPERIENCE",
        "AREAS OF EXPERTISE",
        "KEY SKILLS",
        "CORE COMPETENCIES"
    }

    @staticmethod
    def extract(text: str):

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        header = []

        for line in lines:

            upper = line.upper()

            if upper in ResumeHeaderExtractor.HEADER_STOP_WORDS:
                break

            header.append(line)

            # Safety limit
            if len(header) >= 15:
                break

        return header