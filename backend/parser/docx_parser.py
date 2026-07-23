from docx import Document


class DOCXParser:
    """
    Extracts text from DOCX resumes.
    """

    @staticmethod
    def extract_text(docx_path: str) -> str:
        try:
            document = Document(docx_path)

            text = []

            for paragraph in document.paragraphs:
                text.append(paragraph.text)

            return "\n".join(text).strip()

        except Exception as e:
            raise Exception(f"Error reading DOCX: {e}")