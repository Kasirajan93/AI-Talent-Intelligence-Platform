import re


class ContactExtractor:
    """
    Extracts contact details such as email, phone,
    GitHub, and LinkedIn from resume text.
    """

    @staticmethod
    def extract(text: str) -> dict:
        """
        Extract contact information from resume text.
        """

        result = {
            "email": None,
            "phone": None,
            "github": None,
            "linkedin": None
        }

        # Email
        email = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        if email:
            result["email"] = email.group()

        # Phone Number
        phone = re.search(
            r"(\+91[\-\s]?)?[6-9]\d{4}[\-\s]?\d{5}",
            text
        )

        if phone:
            result["phone"] = phone.group()

        # GitHub
        github = re.search(
            r"github\.com/[A-Za-z0-9_-]+",
            text,
            re.IGNORECASE
        )

        if github:
            result["github"] = github.group()

        # LinkedIn
        linkedin = re.search(
            r"linkedin\.com/in/[A-Za-z0-9_-]+/?",
            text,
            re.IGNORECASE
        )

        if linkedin:
            result["linkedin"] = linkedin.group().rstrip("/")

        return result