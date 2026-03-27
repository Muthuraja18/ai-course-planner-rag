from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(chunks):
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    from langchain.vectorstores import FAISS
    vectorstore = FAISS.from_documents(chunks, embedding)
    vectorstore.save_local("vectorstore/faiss_index")

    return vectorstore