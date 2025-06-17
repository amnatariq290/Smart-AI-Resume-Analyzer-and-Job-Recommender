def recommend_courses(role):
    courses = {
        "Data Science": [
            {"title": "Data Science Specialization - Coursera", "url": "https://www.coursera.org/specializations/jhu-data-science"},
            {"title": "Machine Learning - Coursera", "url": "https://www.coursera.org/learn/machine-learning"}
        ],
        "Web Development": [
            {"title": "Frontend Developer Path - Codecademy", "url": "https://www.codecademy.com/learn/paths/front-end-engineer-career-path"},
            {"title": "Responsive Web Design - freeCodeCamp", "url": "https://www.freecodecamp.org/learn/responsive-web-design/"}
        ],
        "Android Development": [
            {"title": "Android Basics by Google", "url": "https://developer.android.com/courses/pathways/android-basics"},
            {"title": "Kotlin for Android", "url": "https://developer.android.com/kotlin"}
        ],
        "DevOps": [
            {"title": "Learn DevOps - Udemy", "url": "https://www.udemy.com/course/learn-devops/"},
            {"title": "CI/CD with Jenkins - Udemy", "url": "https://www.udemy.com/course/cicd-pipeline-jenkins/"}
        ]
    }
    return courses.get(role, [])
