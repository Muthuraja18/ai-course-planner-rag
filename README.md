# 🎓 AI Course Planning Assistant (Agentic RAG)

## 📌 Overview
This project is a Retrieval-Augmented Generation (RAG) based AI assistant designed to help students plan their academic courses using university catalog data.

The system answers prerequisite queries, suggests semester plans, and ensures all responses are strictly grounded in catalog documents with proper citations.

---

## 🚀 Features

- ✅ Prerequisite checking (Eligible / Not Eligible)
- ✅ Multi-hop prerequisite reasoning
- ✅ Course plan generation for next semester
- ✅ Citation-based answers (grounded in dataset)
- ✅ Clarifying questions when data is missing
- ✅ Safe abstention ("I don’t have that information...")
- ✅ Multi-agent architecture

---

## 🧠 Architecture

This system follows an **Agentic RAG pipeline**:

### 🔹 Agents

1. **Intake Agent**
   - Collects and validates student input
   - Handles missing information

2. **Retriever Agent**
   - Fetches relevant catalog content using FAISS

3. **Planner Agent**
   - Generates course plan / answers using LLM (Groq)

4. **Verifier Agent**
   - Ensures:
     - No hallucination
     - Proper citations
     - Correct prerequisite logic

---

## 🏗️ RAG Pipeline

1. **Data Ingestion**
   - Reads course, program, and policy documents

2. **Chunking**
   - Chunk size: ~500 tokens  
   - Overlap: ~50 tokens  

3. **Embeddings**
   - Model: Sentence Transformers

4. **Vector Store**
   - FAISS

5. **Retriever**
   - Top-K: 2

6. **LLM**
   - Groq (LLaMA models)

---

## 📁 Project Structure
