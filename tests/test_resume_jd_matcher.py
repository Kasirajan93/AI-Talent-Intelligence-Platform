from backend.matcher.resume_jd_matcher import ResumeJDMatcher


resume_data = {
    "skills": [
        "Python",
        "ML",
        "SQL",
        "Tensor Flow"
    ]
}

jd_data = {
    "required_skills": [
        "Python",
        "Machine Learning",
        "SQL",
        "TensorFlow"
    ]
}


result = ResumeJDMatcher.match(
    resume_data,
    jd_data
)

print("\n===== MATCH RESULT =====")
print(result)