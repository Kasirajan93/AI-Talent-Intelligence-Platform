import streamlit as st


def show_candidate_details(ranked_candidates):
    """
    Display detailed information for each ranked candidate.
    """

    st.subheader("📋 Candidate Details")

    for candidate in ranked_candidates:

        with st.expander(
            f"#{candidate['rank']} - {candidate['candidate_name']} "
            f"(ATS: {candidate['ats_score']['total_score']})"
        ):

            resume = candidate["resume_data"]
            match = candidate["match_result"]
            ats = candidate["ats_score"]

            # -------------------------
            # Basic Information
            # -------------------------
            st.markdown("### 👤 Basic Information")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Name:**", resume.get("name", "N/A"))
                st.write("**Education:**", resume.get("education", "N/A"))

            with col2:
                st.write("**Experience:**", resume.get("experience", "N/A"))
                st.write("**Contact:**", resume.get("contact", "N/A"))

            st.divider()

            # -------------------------
            # ATS Score
            # -------------------------
            st.markdown("### 📊 ATS Evaluation")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("ATS Score", ats["total_score"])

            with col2:
                st.metric("Skill Match", f"{match['match_percentage']}%")

            st.write("**Rating:**", ats["rating"])
            st.write("**Recommendation:**", ats["recommendation"])
            st.write("**Hiring Decision:**", ats["hiring_decision"])

            st.divider()

            # -------------------------
            # Skills
            # -------------------------
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### ✅ Matched Skills")

                matched = match.get("matched_skills", [])

                if matched:
                    for skill in matched:
                        st.success(skill)
                else:
                    st.info("No matched skills")

            with col2:
                st.markdown("### ❌ Missing Skills")

                missing = match.get("missing_skills", [])

                if missing:
                    for skill in missing:
                        st.error(skill)
                else:
                    st.success("No missing skills")

            st.divider()

            # -------------------------
            # Resume Skills
            # -------------------------
            st.markdown("### 🛠 Resume Skills")

            skills = resume.get("skills", [])

            if skills:
                st.write(", ".join(skills))
            else:
                st.info("No skills found")