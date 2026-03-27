from crewai.tools import tool
from src.vector_store import load_db

@tool("Catalog Retriever Tool")
def retrieve_docs(query: str) -> str:
    """
    Retrieve course info from FAISS DB.
    """
    try:
        db = load_db()
        docs = db.similarity_search(query, k=3)

        if not docs:
            return "No documents found."

        result = ""
        for i, d in enumerate(docs):
            source = d.metadata.get("source", "unknown")
            content = d.page_content[:500]

            result += f"\nChunk {i+1} (Source: {source}):\n{content}\n"

        return result

    except Exception as e:
        return f"Error: {str(e)}"