import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI DevOps Assistant")
st.write("Ask me anything about Linux, Git, Docker, Kubernetes or DevOps.")

question = st.text_area("Your Question")

if st.button("Ask"):
    if question:
        response = model.generate_content(question)
        st.success(response.text)
    else:
        st.warning("Please enter a question.")