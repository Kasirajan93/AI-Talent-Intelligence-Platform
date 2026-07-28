from backend.ranking.candidate_ranker import CandidateRanker
from backend.screening.resume_screener import ResumeScreener
from backend.exporter.csv_exporter import CSVExporter
from backend.pipeline.resume_pipeline import ResumePipeline


resume_files = ResumeScreener.get_resumes("data/resumes")

candidates = []

print("\n===== DETECTED RESUMES =====\n")

for file in resume_files:
    print(file)


for resume_path in resume_files:

    try:

        candidate = ResumePipeline.process(
            resume_path,
            "data/job_descriptions/sample_jd.txt"
        )

        candidates.append(candidate)

    except Exception as e:

        print(f"Error processing {resume_path}: {e}")

ranked_candidates = CandidateRanker.rank(candidates)

CSVExporter.export(
    ranked_candidates,
    "outputs/candidate_rankings.csv"
)


print("\n========== FINAL RANKING ==========\n")



for candidate in ranked_candidates:

    print(f"Rank               : {candidate['rank']}")
    print(f"Candidate          : {candidate['candidate_name']}")
    print(f"ATS Score          : {candidate['ats_score']['total_score']}")
    print(f"Rating             : {candidate['ats_score']['rating']}")
    print(f"Recommendation     : {candidate['ats_score']['recommendation']}")
    print(f"Hiring Decision    : {candidate['ats_score']['hiring_decision']}")
    print("----------------------------------------------")
