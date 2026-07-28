import streamlit as st


def show_sidebar():

    st.sidebar.title("🤖 AI Talent Intelligence")

    st.sidebar.markdown("---")

    st.sidebar.success("Recruiter Dashboard")

    st.sidebar.markdown(
        """
        ### Features

        ✅ Resume Screening

        ✅ ATS Scoring

        ✅ Candidate Ranking

        ✅ CSV Export
        """
    )