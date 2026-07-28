class CandidateNameEngine:
    """
    Decides the best candidate name from multiple sources.

    Priority:
        1. Header Name
        2. Filename Name
        3. Existing Extractor
    """

    @staticmethod
    def get_name(
        header_name,
        filename_name,
        extracted_name
    ):

        # Highest Priority
        if header_name:
            return header_name

        # Second Priority
        if filename_name:
            return filename_name

        # Last Resort
        if extracted_name:
            return extracted_name

        return "Unknown Candidate"