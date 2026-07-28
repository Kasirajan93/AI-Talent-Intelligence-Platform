class CandidateRanker:

    @staticmethod
    def rank(candidates):

        """
        candidates = [
            {
                "candidate_name": "...",
                "ats_score": {...}
            }
        ]
        """

        ranked = sorted(
            candidates,
            key=lambda x: x["ats_score"]["total_score"],
            reverse=True
        )

        for index, candidate in enumerate(ranked, start=1):

            candidate["rank"] = index

        return ranked