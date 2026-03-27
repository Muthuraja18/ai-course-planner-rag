from crewai import Task

def intake_task(agent, query):
    return Task(
        description=f"""
Check if input is missing info.

Query: {query}

If missing → ask 1-2 questions.
Else → say "Sufficient".
""",
        expected_output="Clarification or confirmation",
        agent=agent
    )


def retrieval_task(agent, query):
    return Task(
        description=f"""
Retrieve relevant catalog data.

Query: {query}

Use tool.
""",
        expected_output="Relevant chunks",
        agent=agent
    )


def planning_task(agent, query):
    return Task(
        description=f"""
STRICT FORMAT ONLY.

Query: {query}

Answer:
Why:
Citations:
Clarifying questions:
Assumptions:

Rules:
- Must include ALL sections
- If missing → write 'None'
- Use retrieved data only
""",
        expected_output="Structured output",
        agent=agent
    )


def verification_task(agent):
    return Task(
        description="""
Ensure output format is correct.

Do NOT remove content.

If missing sections → add them.
""",
        expected_output="Final structured output",
        agent=agent
    )