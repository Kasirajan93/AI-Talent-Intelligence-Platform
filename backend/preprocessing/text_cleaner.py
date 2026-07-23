import re


class TextCleaner:
    """
    Cleans extracted resume text before NLP processing.
    """

    @staticmethod
    def clean(text: str) -> str:

        # Remove extra spaces
        text = re.sub(r"[ \t]+", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n+", "\n", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text