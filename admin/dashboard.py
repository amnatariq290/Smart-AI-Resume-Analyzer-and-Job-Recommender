import streamlit as st
import plotly.express as px
import pandas as pd

def show_dashboard():
    st.title("📊 Admin Dashboard")

    data = {
        "Domains": ["Data Science", "Web Development", "Android Development", "DevOps"],
        "Users": [45, 67, 23, 31]
    }
    df = pd.DataFrame(data)

    st.subheader("Users by Predicted Domain")
    fig = px.pie(df, names="Domains", values="Users", title="User Distribution")
    st.plotly_chart(fig)

    st.subheader("Feedback (Mock)")
    st.write("✔ Feature Requested: More Resume Tips")
    st.write("✔ Most Recommended Role: Web Development")

