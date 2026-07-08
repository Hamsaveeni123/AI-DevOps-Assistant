import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="AI DevOps Assistant", page_icon="🤖")

st.title("🤖 AI DevOps Assistant")
st.write("Ask me anything about Linux, Git, Docker, Kubernetes or DevOps.")

question = st.text_area("Your Question")

if st.button("Ask"):
    if question:
        response = model.generate_content(question)
        st.success(response.text)
    else:
        st.warning("Please enter a question.")