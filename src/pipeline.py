from src.agents.intake_agent import intake_agent
from src.agents.retriever_agent import retrieve_context
from src.agents.planner_agent import planner_agent
from src.agents.verifier_agent import verifier_agent
from src.retriever import load_retriever

retriever = load_retriever()

def run_pipeline(user_input, query):

    # 1️⃣ Intake Agent
    intake = intake_agent(user_input)

    if intake["status"] == "need_info":
        return f"Clarifying questions:\n- " + "\n- ".join(intake["questions"])

    # 2️⃣ Retriever Agent
    context, sources = retrieve_context(query, retriever)

    # 3️⃣ Planner Agent
    plan = planner_agent(context, query, user_input)

    # 4️⃣ Verifier Agent
    final = verifier_agent(plan)

    return final