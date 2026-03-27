def retrieve_context(query, retriever):
    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([doc.page_content for doc in docs])
    sources = [doc.metadata.get("source", "unknown") for doc in docs]

    return context, sources