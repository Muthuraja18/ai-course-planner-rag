from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def load_retriever():
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
         "vectorstore/faiss_index",
         embedding,
         allow_dangerous_deserialization=True
         )
    retriever = db.as_retriever(search_kwargs={"k": 2})

    return retriever