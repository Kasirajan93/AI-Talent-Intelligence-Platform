import pandas as pd

skills = [
    # Programming Languages
    ("Python", "Programming Language"),
    ("Java", "Programming Language"),
    ("C", "Programming Language"),
    ("C++", "Programming Language"),
    ("C#", "Programming Language"),
    ("JavaScript", "Programming Language"),
    ("TypeScript", "Programming Language"),
    ("Go", "Programming Language"),
    ("Rust", "Programming Language"),
    ("R", "Programming Language"),

    # Databases
    ("SQL", "Database"),
    ("MySQL", "Database"),
    ("PostgreSQL", "Database"),
    ("SQLite", "Database"),
    ("Oracle", "Database"),
    ("MongoDB", "Database"),
    ("Redis", "Database"),
    ("Cassandra", "Database"),

    # Data Science
    ("Data Science", "Data Science"),
    ("Pandas", "Data Science"),
    ("NumPy", "Data Science"),
    ("Matplotlib", "Data Science"),
    ("Seaborn", "Data Science"),
    ("Plotly", "Data Science"),
    ("SciPy", "Data Science"),

    # Machine Learning
    ("Machine Learning", "Machine Learning"),
    ("Scikit-learn", "Machine Learning"),
    ("XGBoost", "Machine Learning"),
    ("LightGBM", "Machine Learning"),
    ("CatBoost", "Machine Learning"),

    # Deep Learning
    ("Deep Learning", "Deep Learning"),
    ("TensorFlow", "Deep Learning"),
    ("Keras", "Deep Learning"),
    ("PyTorch", "Deep Learning"),

    # NLP
    ("Natural Language Processing", "NLP"),
    ("NLTK", "NLP"),
    ("spaCy", "NLP"),
    ("Transformers", "NLP"),
    ("Hugging Face", "NLP"),

    # Cloud
    ("AWS", "Cloud"),
    ("Azure", "Cloud"),
    ("Google Cloud", "Cloud"),

    # DevOps
    ("Docker", "DevOps"),
    ("Kubernetes", "DevOps"),
    ("Jenkins", "DevOps"),

    # Version Control
    ("Git", "Version Control"),
    ("GitHub", "Version Control"),
    ("GitLab", "Version Control"),

    # Web
    ("Flask", "Web Development"),
    ("Django", "Web Development"),
    ("FastAPI", "Web Development"),
    ("React", "Web Development"),

    # BI
    ("Power BI", "Business Intelligence"),
    ("Tableau", "Business Intelligence"),
]

df = pd.DataFrame(skills, columns=["skill", "category"])

df.to_csv(
    "data/knowledge_base/skills.csv",
    index=False
)

print("Knowledge Base Created Successfully!")
print(df.head())
print(f"\nTotal Skills: {len(df)}")