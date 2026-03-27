from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return LLM(
        model="llama-3.3-70b-versatile",   # ✅ correct format
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1", 
        temperature=0
    )