import re
import spacy

nlp = spacy.load("en_core_web_sm")


class NameExtractorV2:

    IGNORE_WORDS = {
        "PROFILE", "SUMMARY", "SKILLS", "PROJECTS", "EDUCATION",
        "EXPERIENCE", "CERTIFICATIONS", "CONTACT",
        "DATA SCIENTIST", "SOFTWARE ENGINEER", "MACHINE LEARNING",
        "MADURAI", "TAMIL NADU", "INDIA"
    }

    @staticmethod
    def extract(text: str):

        # Check first 10 non-empty lines
        lines = [line.strip() for line in text.split("\n") if line.strip()]

        for line in lines[:10]:

            upper = line.upper()

            if upper in NameExtractorV2.IGNORE_WORDS:
                continue

            # Candidate name:
            # 2 to 4 words, letters only
            if re.fullmatch(r"[A-Za-z.\s]{3,40}", line):
                return line

        # Fallback to spaCy
        doc = nlp(text)

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text

        return None