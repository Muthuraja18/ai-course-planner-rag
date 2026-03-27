from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents(data_path):
    docs = []
    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path, file))
            docs.extend(loader.load())
    return docs


def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)
    return chunks