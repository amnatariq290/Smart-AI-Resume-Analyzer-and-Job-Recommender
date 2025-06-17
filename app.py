import streamlit as st
from utils.resume_parser import parse_resume
from utils.role_predictor import predict_role
from utils.score_calculator import calculate_score
from utils.course_recommender import recommend_courses
from admin.dashboard import show_dashboard
import pdfminer
import pandas as pd

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Resume Analyzer & Career Recommender")

menu = ["Home", "Admin Dashboard"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    if uploaded_file:
        resume_text = parse_resume(uploaded_file)

        st.subheader("Extracted Information")
        st.write(resume_text)

        role = predict_role(resume_text)
        st.success(f"Predicted Career Domain: {role}")

        score = calculate_score(resume_text, role)
        st.info(f"Resume Score: {score}/100")

        st.subheader("Recommended Courses")
        for course in recommend_courses(role):
            st.markdown(f"- [{course['title']}]({course['url']})")
elif choice == "Admin Dashboard":
    show_dashboard()
