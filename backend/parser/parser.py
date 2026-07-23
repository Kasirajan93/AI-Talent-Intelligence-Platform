import os

from backend.parser.pdf_parser import PDFParser
from backend.parser.docx_parser import DOCXParser


class ResumeParser:

    @staticmethod
    def extract_text(file_path: str):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return PDFParser.extract_text(file_path)

        elif extension == ".docx":
            return DOCXParser.extract_text(file_path)

        else:
            raise ValueError("Unsupported file format")