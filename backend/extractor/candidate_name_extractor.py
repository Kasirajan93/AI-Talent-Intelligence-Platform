import re
import spacy

nlp = spacy.load("en_core_web_sm")


class CandidateNameExtractor:

    @staticmethod
    def extract(text):

        # -----------------------------------------
        # STEP 1 : Look for "Name:"
        # -----------------------------------------

        pattern = re.compile(
            r"Name\s*:\s*([A-Z][A-Za-z.\- ]+)",
            re.IGNORECASE
        )

        match = pattern.search(text)

        if match:

            return match.group(1).strip()

        # -----------------------------------------
        # STEP 2 : spaCy PERSON entities
        # -----------------------------------------

        doc = nlp(text[:5000])

        for ent in doc.ents:

            if ent.label_ != "PERSON":
                continue

            candidate = ent.text.strip()

            words = candidate.split()

            if 2 <= len(words) <= 4:

                if all(word[0].isupper() for word in words):

                    return candidate

        # -----------------------------------------
        # STEP 3 : Fallback
        # -----------------------------------------

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        blacklist = {

            "PROFILE",
            "SUMMARY",
            "OBJECTIVE",
            "SKILLS",
            "TECHNICAL",
            "PROJECTS",
            "EDUCATION",
            "EXPERIENCE",
            "CERTIFICATIONS",
            "EMPLOYER",
            "DETAILS",
            "EMAIL",
            "PHONE",
            "CONTACT",
            "VISA",
            "STATUS"

        }

        for line in lines[:20]:

            upper = line.upper()

            if any(word in upper for word in blacklist):
                continue

            if (
                "@"
                in line
                or "http"
                in line.lower()
                or "+"
                in line
            ):
                continue

            words = line.split()

            if 2 <= len(words) <= 4:

                if all(
                    re.fullmatch(
                        r"[A-Z][A-Za-z.\-']*",
                        word
                    )
                    for word in words
                ):
                    return line

        return "Unknown Candidate"