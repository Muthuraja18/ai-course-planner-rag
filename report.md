# AI Course Planning Assistant – Report

## Dataset
The dataset consists of:
- 20+ course descriptions
- Program requirements
- Academic policies

Sources:
- https://catalog.mit.edu/ (Accessed March 2026)
- https://bulletin.stanford.edu/

## Architecture
The system uses an Agentic RAG pipeline:
- Intake Agent
- Retriever Agent (FAISS)
- Planner Agent (Groq LLM)
- Verifier Agent

## Chunking Strategy
- Chunk size: ~500 tokens
- Overlap: 50 tokens

## Retrieval
- Vector store: FAISS
- Top-k: 2

## Prompt Design
- Enforces citations
- Prevents hallucination
- Structured output format

## Evaluation
- 25 test queries
- Categories:
  - Prerequisite checks
  - Chain reasoning
  - Program requirements
  - Unknown queries

## Results
- High citation coverage (~95%)
- Correct prerequisite reasoning
- Proper abstention for unknown queries

## Limitations
- No semester availability
- Limited dataset size

## Future Improvements
- Expand dataset
- Add real university APIs