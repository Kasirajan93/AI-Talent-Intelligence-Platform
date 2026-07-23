import csv
import os

# ========= Skill Categories ========= #

programming_languages = [
    "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript",
    "Go", "Rust", "R", "MATLAB", "Scala", "Kotlin", "Swift",
    "PHP", "Ruby", "Perl", "Dart", "Julia", "Bash"
]

databases = [
    "MySQL", "PostgreSQL", "SQLite", "MongoDB", "Oracle",
    "Microsoft SQL Server", "MariaDB", "Redis", "Cassandra",
    "DynamoDB", "Firebase", "Neo4j", "Elasticsearch"
]

data_science = [
    "NumPy", "Pandas", "Matplotlib", "Seaborn",
    "Scikit-learn", "SciPy", "Statsmodels",
    "Jupyter Notebook", "Google Colab",
    "EDA", "Feature Engineering", "Data Cleaning",
    "Data Visualization", "Statistical Analysis"
]

machine_learning = [
    "Machine Learning",
    "Deep Learning",
    "Supervised Learning",
    "Unsupervised Learning",
    "Reinforcement Learning",
    "Regression",
    "Classification",
    "Clustering",
    "Decision Trees",
    "Random Forest",
    "XGBoost",
    "LightGBM",
    "CatBoost"
]

# ==================================== #

skills = (
    programming_languages
    + databases
    + data_science
    + machine_learning
)

# Remove duplicates and sort
skills = sorted(set(skills))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

output_dir = os.path.join(BASE_DIR, "data", "knowledge_base")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "skills.csv")

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["skill"])

    for skill in skills:
        writer.writerow([skill])

print(f"✅ Generated {len(skills)} skills.")
print(f"Saved to: {output_path}")