import re


class HeaderNameExtractor:
    """
    Extract the candidate's name from the resume header.
    """

    INVALID_WORDS = {
        "email",
        "phone",
        "mobile",
        "mail",
        "location",
        "linkedin",
        "github",
        "summary",
        "profile",
        "professional",
        "experience",
        "objective",
        "education",
        "skills",
        "visa",
        "status",
        "employer",
        "details",
        "program",
        "manager",
        "business",
        "analyst",
        "scientist",
        "developer",
        "engineer"
    }

    @staticmethod
    def extract(header_lines):

        for line in header_lines:

            line = line.strip()

            if not line:
                continue

            # Remove labels like "Name:"
            line = re.sub(r"^Name\s*:\s*", "", line, flags=re.IGNORECASE)

            # Ignore lines containing email
            if "@" in line:
                continue

            # Ignore lines containing phone numbers
            if re.search(r"\d{3}[-.\s]?\d{3}", line):
                continue

            words = line.split()

            # Candidate names are usually 1–4 words
            if len(words) > 4:
                continue

            # Reject if any invalid keyword appears
            if any(word.lower() in HeaderNameExtractor.INVALID_WORDS for word in words):
                continue

            # Reject if line contains special separators
            if "|" in line or ":" in line:
                continue

            # Reject separator lines
            if set(line) <= {"-", "_", "="}:
                continue

            # Reject lines without any alphabetic characters
            if not any(char.isalpha() for char in line):
                continue

            return line

        return None