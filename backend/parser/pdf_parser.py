import fitz  # PyMuPDF


class PDFParser:
    """
    Extracts text from PDF resumes.
    """

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        text = ""

        try:
            document = fitz.open(pdf_path)

            for page in document:
                text += page.get_text()

            document.close()

            return text.strip()

        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")