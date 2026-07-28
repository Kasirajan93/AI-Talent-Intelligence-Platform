import csv
import os


class CSVExporter:

    @staticmethod
    def export(candidates, output_path):

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Rank",
                "Candidate",
                "ATS Score",
                "Rating",
                "Recommendation",
                "Hiring Decision"
            ])

            for candidate in candidates:

                ats = candidate["ats_score"]

                writer.writerow([
                    candidate["rank"],
                    candidate["candidate_name"],
                    ats["total_score"],
                    ats["rating"],
                    ats["recommendation"],
                    ats["hiring_decision"]
                ])

        print(f"\nCSV exported successfully to: {output_path}")