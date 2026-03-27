def intake_agent(user_input):
    missing = []

    if not user_input.get("completed_courses"):
        missing.append("completed courses")

    if not user_input.get("target_program"):
        missing.append("target program")

    if missing:
        return {
            "status": "need_info",
            "questions": [f"Please provide {m}" for m in missing]
        }

    return {"status": "ok", "data": user_input}