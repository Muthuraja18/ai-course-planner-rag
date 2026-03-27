from src.ingestion import load_documents, chunk_documents
from src.embeddings import create_vector_store

docs = []

docs += load_documents("data/courses/")
docs += load_documents("data/programs/")
docs += load_documents("data/policies/")

chunks = chunk_documents(docs)

print(f"Loaded {len(chunks)} chunks")

create_vector_store(chunks)

print("✅ FAISS index created successfully!")