import streamlit as st
import pandas as pd
from PIL import Image

# Set page config
st.set_page_config(page_title="Kgomotso Sereo – STEM Research", layout="centered")

# Title with color
st.markdown("<h1 style='color: darkblue;'>Kgomotso Sereo – STEM Research Profile</h1>", unsafe_allow_html=True)

# Profile image
image = Image.open("stem_research.png")
st.image(image, caption="Kgomotso Sereo", width=200)

# Sidebar
st.sidebar.title("About Me")
st.sidebar.image("stem_research.png", width=150)
st.sidebar.info("""
💻 Computer Science student  
🔬 STEM researcher  
🌍 Community development enthusiast
""")

# About Me section
st.header("About Me")
st.write("""
I am a Computer Science student and STEM researcher.
My research focuses on gaps in digitalization in schools and universities,
particularly access to ICT infrastructure and digital learning tools.
""")

# Research Focus section
st.header("Research Focus")
st.write("""
- 📌 Digital infrastructure gaps in education  
- 📌 ICT access in schools and universities  
- 📌 Digital literacy for STEM learning  
- 📌 Technology-enabled education systems
""")

# Research Overview Table
data = pd.DataFrame({
    "Area": ["Schools", "Universities", "Rural Institutions"],
    "Challenge Level": ["High", "Medium", "Very High"]
})
st.subheader("Research Overview")
st.dataframe(data)

# Contact section
st.header("Contact")
st.write("✉️ Email: kgomotsosereo1@example.com")
