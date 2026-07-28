import re


class SkillNormalizer:
    """
    Normalizes skill names by handling abbreviations,
    aliases, and common spelling variations.
    """

    ALIASES = {
        "ml": "machine learning",
        "dl": "deep learning",
        "ai": "artificial intelligence",
        "js": "javascript",
        "ts": "typescript",
        "tf": "tensorflow",
        "cv": "computer vision",
        "nlp": "natural language processing",
        "node": "node.js",
        "postgres": "postgresql",
        "ms sql": "microsoft sql server",
        "aws s3": "amazon s3",
        "aws ec2": "amazon ec2",
        "k8s": "kubernetes",

        # Common spelling variations
        "tensor flow": "tensorflow",
        "sci kit learn": "scikit-learn",
        "scikit learn": "scikit-learn",
        "node js": "node.js",
        "nodejs": "node.js",
        "c sharp": "c#"
    }

    @classmethod
    def normalize(cls, skill: str) -> str:
        """
        Convert a skill into its normalized form for
        accurate comparison and matching.
        """

        if not skill:
            return ""

        skill = skill.lower().strip()

        # Remove punctuation except # and +
        skill = re.sub(r"[^\w\s#+.-]", "", skill)

        # Collapse multiple spaces
        skill = " ".join(skill.split())

        return cls.ALIASES.get(skill, skill)