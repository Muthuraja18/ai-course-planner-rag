def verifier_agent(response):
    if "Citations:" not in response:
        return "❌ Invalid response: Missing citations"

    if "I don’t know" in response:
        return response + "\n\n✔ Safe Abstention"

    return "✔ Verified\n\n" + response