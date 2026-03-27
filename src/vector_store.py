import os
from langchain_community.vectorstores import FAISS 
from src.embeddings import get_embeddings
from src.ingestion import load_docs, split_docs

DB_PATH = "db/faiss_index"

def create_db():
    print("🔄 Creating FAISS DB...")

    docs = load_docs()
    if not docs:
        raise ValueError("❌ No documents found in data/docs")

    chunks = split_docs(docs)
    embeddings = get_embeddings()

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)

    print("✅ FAISS DB created successfully")
    return db


def load_db():
    embeddings = get_embeddings()

    if not os.path.exists(DB_PATH):
        return create_db()

    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )