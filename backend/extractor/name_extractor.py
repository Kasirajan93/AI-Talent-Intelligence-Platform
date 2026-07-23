import spacy

nlp = spacy.load("en_core_web_sm")


class NameExtractor:

    @staticmethod
    def extract(text: str):

        doc = nlp(text)

        for entity in doc.ents:

            if entity.label_ == "PERSON":
                return entity.text

        return None