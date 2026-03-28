# 🧠 AI Course Planner with RAG

---

## 📌 Description
An AI-powered course planning assistant that uses **Retrieval-Augmented Generation (RAG)** with a **multi-agent system (CrewAI)** to answer academic queries such as prerequisites, eligibility, and semester planning.

---

## 🎯 Problem Statement

Students often struggle to understand course prerequisites, eligibility, and academic planning.

Traditional systems provide static information, but lack intelligent reasoning.

This project builds an AI-powered assistant that:
- understands queries
- retrieves relevant academic data
- provides structured, explainable answers with citations

---

## 🚀 Features

- ✅ Prerequisite checking (Eligible / Not Eligible)
- ✅ Multi-hop prerequisite reasoning
- ✅ Course plan generation for next semester
- ✅ Citation-based answers (grounded in dataset)
- ✅ Clarifying questions for missing input
- ✅ Safe fallback ("I don’t have that information")
- ✅ Multi-agent architecture

---

## 🛠 Tech Stack

- Python  
- LangChain  
- FAISS (Vector Store)  
- Streamlit  
- CrewAI  
- Groq (LLaMA Models)  

---

## 🧠 Architecture (Multi-Agent System)

1. **Intake Agent**
   - Validates user query
   - Detects missing information

2. **Retriever Agent**
   - Fetches relevant chunks from FAISS

3. **Planner Agent**
   - Generates structured answer

4. **Verifier Agent**
   - Ensures:
     - correctness  
     - no hallucination  
     - proper citations  

---

## 🔄 RAG Pipeline Flow

1. Load documents (courses, programs, policies)  
2. Chunk text (500 size, 50 overlap)  
3. Generate embeddings  
4. Store in FAISS  
5. Process user query:
   - Retrieve relevant chunks  
   - Generate answer  
   - Verify output  

---

## 📊 Dataset

- 📘 20+ course descriptions  
- 📗 program requirements  
- 📙 academic policies  

---

## 🔗 Sources

- https://catalog.mit.edu/ (March 2026)  
- https://bulletin.stanford.edu/ (March 2026)  
- https://www.example-university.edu/policies (March 2026)  

---

## 📊 Evaluation Strategy

- 25+ test queries  
- Categories:
  - prerequisite reasoning  
  - multi-step planning  

Evaluation metrics:
- correctness  
- citation grounding  
- reasoning quality  

---

## ⚙️ Setup & Run
2️⃣ Add API key (.env)
GROQ_API_KEY=your_key_here
3️⃣ Build vector index
python build_index.py
4️⃣ Run Streamlit app
streamlit run app.py
5️⃣ Run evaluation
python evaluation/evaluation.py
### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
