import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from docker_tools import list_containers, start_nginx, stop_container

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI DevOps Assistant")
st.write("Ask me anything about Linux, Git, Docker, Kubernetes or DevOps.")

question = st.text_area("Your Question")

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question.")
    else:
        q = question.lower().strip()

        if "list containers" in q:
            st.code(list_containers())

        elif "start nginx" in q:
            st.success(start_nginx())

        elif "stop nginx" in q:
            st.success(stop_container("my-nginx"))

        else:
            response = model.generate_content(question)
            st.write(response.text)