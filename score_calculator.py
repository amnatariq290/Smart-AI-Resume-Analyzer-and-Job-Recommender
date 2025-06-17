def calculate_score(text, role):
    role_keywords = {
        "Data Science": ["python", "machine learning", "pandas", "data"],
        "Web Development": ["html", "css", "javascript", "react"],
        "Android Development": ["android", "kotlin", "java"],
        "DevOps": ["docker", "jenkins", "aws"]
    }
    keywords = role_keywords.get(role, [])
    text = text.lower()
    match_count = sum(1 for word in keywords if word in text)
    score = int((match_count / len(keywords)) * 100)
    return score
