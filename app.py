import streamlit as st
import pandas as pd

from frontend.sidebar import show_sidebar
from frontend.uploader import upload_files
from frontend.file_manager import save_uploaded_file
from frontend.candidate_details import show_candidate_details

from backend.pipeline.resume_pipeline import ResumePipeline
from backend.ranking.candidate_ranker import CandidateRanker


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Resume Screening Bot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

show_sidebar()

# ---------------------------------------------------
# Main Title
# ---------------------------------------------------

st.title(" 🤖 AI Talent Intelligence Platform" )
                     


st.markdown("---")

# ---------------------------------------------------
# Upload Files
# ---------------------------------------------------

jd_file, resume_files = upload_files()

# Upload Status

if jd_file:
    st.success("✅ Job Description Uploaded")

if resume_files:
    st.success(f"✅ {len(resume_files)} Resume(s) Uploaded")

st.markdown("---")

# ---------------------------------------------------
# Analyze Button
# ---------------------------------------------------

analyze = st.button("🚀 Analyze Candidates")

# ---------------------------------------------------
# Process Files
# ---------------------------------------------------

if analyze:

    # -------------------------------
    # Validation
    # -------------------------------

    if jd_file is None:
        st.error("❌ Please upload a Job Description.")
        st.stop()

    if not resume_files:
        st.error("❌ Please upload at least one Resume.")
        st.stop()

    candidates = []

    # -------------------------------
    # Save Job Description
    # -------------------------------

    jd_path = save_uploaded_file(
        jd_file,
        "temp/job_descriptions"
    )

    progress = st.progress(0)

    # -------------------------------
    # Process Resumes
    # -------------------------------

    for index, resume in enumerate(resume_files):

        try:

            resume_path = save_uploaded_file(
                resume,
                "temp/resumes"
            )

            candidate = ResumePipeline.process(
                resume_path,
                jd_path
            )

            candidates.append(candidate)

        except Exception as e:

            st.warning(f"Skipped {resume.name}")

            st.error(str(e))

        progress.progress((index + 1) / len(resume_files))

    # -------------------------------
    # Ranking
    # -------------------------------

    ranked_candidates = CandidateRanker.rank(candidates)

    st.success("✅ Analysis Completed Successfully!")

    # -------------------------------
    # Convert to DataFrame
    # -------------------------------

    rows = []

    for candidate in ranked_candidates:

        rows.append({

            "Rank": candidate["rank"],
            "Candidate": candidate["candidate_name"],
            "ATS Score": candidate["ats_score"]["total_score"],
            "Rating": candidate["ats_score"]["rating"],
            "Recommendation": candidate["ats_score"]["recommendation"],
            "Hiring Decision": candidate["ats_score"]["hiring_decision"]

        })

    df = pd.DataFrame(rows)

    # -------------------------------
    # Dashboard Metrics
    # -------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Candidates", len(df))

    with col2:
        st.metric(
            "Average ATS",
            round(df["ATS Score"].mean(), 2)
        )

    with col3:
        shortlisted = len(
            df[df["Hiring Decision"] == "Shortlist"]
        )

        st.metric("Shortlisted", shortlisted)

    st.markdown("---")

    # -------------------------------
    # Ranking Table
    # -------------------------------

    st.subheader("🏆 Candidate Rankings")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    show_candidate_details(ranked_candidates)
    
    # -------------------------------
    # Download CSV
    # -------------------------------

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Rankings (CSV)",
        data=csv,
        file_name="candidate_rankings.csv",
        mime="text/csv"
    )