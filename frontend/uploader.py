import streamlit as st


def upload_files():

    st.header("📄 Upload Job Description")

    jd_file = st.file_uploader(
        "Choose Job Description",
        type=["txt"]
    )

    st.header("📁 Upload Resumes")

    resume_files = st.file_uploader(
        "Choose Resume Files",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    return jd_file, resume_files