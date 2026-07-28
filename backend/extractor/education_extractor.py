import re


class EducationExtractor:

    """
    Extracts education details such as degree and
    graduation year from resume text.
    """

    DEGREE_PATTERNS: list[str] = [
        r"\bB\.?Tech\b",
        r"\bB\.?E\.?\b",
        r"\bB\.?Sc\b",
        r"\bB\.?Com\b",
        r"\bB\.?A\b",
        r"\bB\.?C\.?A\b",
        r"\bB\.?B\.?A\b",
        r"\bB\.?A\.?M\.?S\.?\b",
        r"\bM\.?Tech\b",
        r"\bM\.?E\.?\b",
        r"\bM\.?Sc\b",
        r"\bM\.?Com\b",
        r"\bM\.?A\b",
        r"\bM\.?C\.?A\b",
        r"\bMBA\b",
        r"\bPh\.?D\b"
    ]

    @staticmethod
    def extract(text: str) -> dict:
        """
        Extract degree and graduation year from resume text.
        """

        education = {
            "degree": None,
            "graduation_year": None
        }

        # Degree
        for pattern in EducationExtractor.DEGREE_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                education["degree"] = match.group()
                break

        # Graduation Year
        years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)

        if years:
            education["graduation_year"] = years[-1]

        return education