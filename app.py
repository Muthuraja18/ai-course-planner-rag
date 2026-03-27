import streamlit as st
from src.pipeline import run_pipeline

st.title("🎓 AI Course Planning Assistant")

query = st.text_input("Ask your question")

completed = st.text_input("Completed Courses")
program = st.text_input("Target Program")

user_input = {
    "completed_courses": completed,
    "target_program": program
}

if st.button("Generate Plan"):
    result = run_pipeline(user_input, query)

    st.subheader("📘 Result")
    st.markdown(result)