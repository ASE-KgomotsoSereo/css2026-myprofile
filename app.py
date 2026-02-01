import streamlit as st
import pandas as pd

# Set the page title
st.set_page_config(page_title="Kgomotso's STEM Research", layout="centered")

# Main title
st.title("Kgomotso Sereo - STEM Research Profile")

# About Me section
st.header("About Me")
st.write("""
I am a Computer Science student and STEM researcher. 
My research focuses on identifying and addressing **gaps in digitalization in schools and universities**, 
including access to technology, ICT infrastructure, and digital learning tools.
""")

# Research Focus
st.header("Research Focus / Interests")
st.write("""
- Assessing **digital infrastructure gaps** in schools and universities.
- Evaluating **ICT adoption** by teachers and students.
- Studying **digital literacy** among learners.
- Exploring ways to **improve access to technology** for STEM education.
""")

# Sample Findings Table
data = pd.DataFrame({
    "Institution": ["School A", "University B", "School C"],
    "Digital Infrastructure Score": [45, 78, 52],
    "ICT Access Challenges": [
        "Limited computers, low internet speed",
        "Partial access to labs, software outdated",
        "Few devices, no Wi-Fi in classrooms"
    ]
})
st.subheader("Sample Findings")
st.dataframe(data)

# Contact section
st.header("Contact")
st.write("Email: kgomotso@example.com")
st.write("LinkedIn / Portfolio: [Your Link Here](https://www.linkedin.com/)")

# Optional: Closing remark
st.markdown("---")
st.write("This page showcases my ongoing research on STEM digitalization gaps and ICT challenges in education.")
