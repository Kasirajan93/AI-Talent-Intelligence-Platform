from backend.parser.parser import ResumeParser
from backend.preprocessing.text_cleaner import TextCleaner
from backend.extractor.resume_information_extractor import ResumeInformationExtractor
from backend.jd_parser.jd_parser import JDParser
from backend.jd_parser.jd_information_extractor import JDInformationExtractor
from backend.matcher.resume_jd_matcher import ResumeJDMatcher
from backend.scoring.ats_scorer import ATSScorer
from backend.extractor.header_name_extractor import HeaderNameExtractor
from backend.extractor.resume_header_extractor import ResumeHeaderExtractor
from backend.extractor.filename_name_extractor import FilenameNameExtractor
from backend.extractor.candidate_name_engine import CandidateNameEngine


class ResumePipeline:

    @staticmethod
    def process(resume_path, jd_path):

        # -----------------------------
        # Parse Resume
        # -----------------------------
        raw_text = ResumeParser.extract_text(resume_path)

        clean_text = TextCleaner.clean(raw_text)

        # -----------------------------
        # Header Extraction (Debug)
        # -----------------------------
        header = ResumeHeaderExtractor.extract(clean_text)

        header_name = HeaderNameExtractor.extract(header)
        filename_name = FilenameNameExtractor.extract(resume_path)

        # -----------------------------
        # Resume Information Extraction
        # -----------------------------
        resume_data = ResumeInformationExtractor.extract(clean_text)

        # ---------------------------------
        # Candidate Name Decision Engine
        # ---------------------------------

        candidate_name = CandidateNameEngine.get_name(
            header_name=header_name,
            filename_name=filename_name,
            extracted_name=resume_data["name"]
        )

        resume_data["name"] = candidate_name

        # -----------------------------
        # Job Description
        # -----------------------------
        jd_text = JDParser.read(jd_path)

        jd_data = JDInformationExtractor.extract(jd_text)

        # -----------------------------
        # Matching
        # -----------------------------
        match_result = ResumeJDMatcher.match(
            resume_data,
            jd_data
        )

        # -----------------------------
        # ATS Score
        # -----------------------------
        ats_score = ATSScorer.score(
            resume_data,
            jd_data,
            match_result
        )

        # -----------------------------
        # Final Output
        # -----------------------------
        return {
            "candidate_name": candidate_name,
            "resume_data": resume_data,
            "match_result": match_result,
            "ats_score": ats_score
        }