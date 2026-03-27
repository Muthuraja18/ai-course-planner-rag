from crewai import Agent
from src.tools import retrieve_docs
from src.llm import get_llm

llm = get_llm()

def intake_agent():
    return Agent(
        role="Student Intake Agent",
        goal="Identify missing student info and ask clarifying questions",
        backstory="Expert academic advisor",
        llm=llm,
        verbose=False
    )

def retriever_agent():
    return Agent(
        role="Catalog Retriever",
        goal="Retrieve relevant academic catalog content",
        backstory="Search expert",
        tools=[retrieve_docs],
        llm=llm,
        verbose=False
    )

def planner_agent():
    return Agent(
        role="Course Planner",
        goal="Decide eligibility and generate course plan",
        backstory="Strict academic planner",
        llm=llm,
        verbose=False
    )

def verifier_agent():
    return Agent(
        role="Verifier",
        goal="Check correctness, citations, and prevent hallucination",
        backstory="Strict auditor",
        llm=llm,
        verbose=False
    )