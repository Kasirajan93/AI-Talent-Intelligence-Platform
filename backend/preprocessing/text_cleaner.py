import re


class TextCleaner:
    """
    Cleans extracted resume text before NLP processing.
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Normalize extracted resume text by removing
        unnecessary whitespace and blank lines.
        """

        if not text:
            return ""

        # Remove extra spaces and tabs
        text = re.sub(r"[ \t]+", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n+", "\n", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text