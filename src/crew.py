from crewai import Crew, Process
from src.agents import retriever_agent, planner_agent, verifier_agent
from src.tasks import retrieval_task, planning_task, verification_task


def run_crew(query):
    try:
        # 🔹 Initialize agents
        retriever = retriever_agent()
        planner = planner_agent()
        verifier = verifier_agent()

        # 🔹 Define tasks
        retrieval_t = retrieval_task(retriever, query)

        planning_t = planning_task(planner, query)
        planning_t.context = [retrieval_t]   # depends on retrieved data

        verification_t = verification_task(verifier)
        verification_t.context = [planning_t]  # depends on planner output

        # 🔹 Create Crew
        crew = Crew(
            agents=[retriever, planner, verifier],
            tasks=[retrieval_t, planning_t, verification_t],
            process=Process.sequential,   # ensures proper flow
            verbose=False                 # keep False to reduce token usage
        )

        # 🔹 Execute
        result = crew.kickoff()

        # 🔥 Ensure output is never empty
        if not result or str(result).strip() == "":
            return """Answer: Not generated
Why: No output returned from system
Citations: None
Clarifying questions: None
Assumptions: None"""

        return str(result)

    except Exception as e:
        error_msg = str(e)

        # 🔥 Handle rate limit
        if "rate limit" in error_msg.lower() or "429" in error_msg:
            return """Answer: Rate limit reached
Why: API usage exceeded. Please wait and try again.
Citations: None
Clarifying questions: Try again after some time
Assumptions: Free tier API limitation"""

        return f"""Answer: Error occurred
Why: {error_msg}
Citations: None
Clarifying questions: None
Assumptions: System error"""