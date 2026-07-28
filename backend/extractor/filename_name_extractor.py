import os
import re


class FilenameNameExtractor:
    """
    Extract candidate name from resume filename.

    Examples:
        kasi_rajan_data_science.pdf
            -> Kasi Rajan

        Abiral_Pandey_Fullstack_Java.docx
            -> Abiral Pandey

        RaviBurra_Certified PM_DevOps.docx
            -> Ravi Burra

        Resume.pdf
            -> None
    """

    IGNORE_WORDS = {
        "resume",
        "cv",
        "final",
        "latest",
        "updated",
        "update",
        "copy",
        "profile",
        "data",
        "science",
        "developer",
        "engineer",
        "analyst",
        "manager",
        "project",
        "qa",
        "java",
        "python",
        "fullstack",
        "devops",
        "business",
        "certified",
        "pm"
    }

    @staticmethod
    def extract(file_path):

        filename = os.path.basename(file_path)

        filename = os.path.splitext(filename)[0]

        filename = filename.replace("_", " ")
        filename = filename.replace("-", " ")

        # Split CamelCase
        filename = re.sub(r"([a-z])([A-Z])", r"\1 \2", filename)

        words = []

        for word in filename.split():

            clean = word.lower()

            if clean in FilenameNameExtractor.IGNORE_WORDS:
                continue

            if len(word) == 1:
                continue

            if word.isdigit():
                continue

            words.append(word.title())

        if len(words) >= 2:
            return " ".join(words[:2])

        if len(words) == 1:
            return words[0]

        return None