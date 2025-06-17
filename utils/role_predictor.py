def predict_role(text):
    keywords = {
        "Data Science": ["machine learning", "data analysis", "python", "pandas"],
        "Web Development": ["html", "css", "javascript", "react"],
        "Android Development": ["android", "kotlin", "java", "xml"],
        "DevOps": ["docker", "kubernetes", "aws", "jenkins"]
    }
    text = text.lower()
    role_scores = {role: sum(kw in text for kw in kws) for role, kws in keywords.items()}
    predicted = max(role_scores, key=role_scores.get)
    return predicted
