import pdfplumber


class PDFParser:
    """
    Extracts text from PDF resumes using pdfplumber.
    """

    @staticmethod
    def extract_text(pdf_path: str) -> str:

        text = ""

        try:
            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            return text.strip()

        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")