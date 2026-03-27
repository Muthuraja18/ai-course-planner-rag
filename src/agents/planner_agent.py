import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def planner_agent(context, query, user_input):
     
    prompt = f"""
You are an AI Course Planning Assistant.

STRICT RULES:
- Only use provided context
- Always include citations
- If unsure, say: "I don’t have that information in the provided catalog"
- DO NOT hallucinate
- Include "Next Step" in reasoning when applicable
- Do NOT assume which courses the student has or has not completed
- If missing, ask clarifying questions instead
- Format output with bullet points and line breaks
- Do NOT assume completed courses unless explicitly provided
- Only cite course catalog / program / policy documents
- Citations must include section names (e.g., Core Requirements, Electives)
- Prefer prerequisite sections when available

--------------------------------------
CONTEXT:
{context}
--------------------------------------

STUDENT PROFILE:
Completed Courses: {user_input.get("completed_courses")}
Target Program: {user_input.get("target_program")}

--------------------------------------
QUESTION:
{query}
--------------------------------------

OUTPUT FORMAT (STRICT):

Answer / Plan:
- Write clear final decision

Why (requirements/prereqs satisfied):
- Step 1 explanation
- Step 2 explanation

Citations:
- Section-based sources (e.g., "Program Requirements: Core Requirements")

Clarifying questions (if needed):
- Only if necessary

Assumptions / Not in catalog:
- Clearly mention missing info

"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ stable model
        messages=[
            {"role": "system", "content": "You are a strict academic advisor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content