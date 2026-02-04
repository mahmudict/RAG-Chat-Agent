## RAG Chat System

A Retrieval-Augmented Generation (RAG) system that allows question answering over academic PDFs using FAISS, Sentence Transformers, and a local LLM.

## Features
- Page-aware PDF ingestion
- Section-based semantic chunking
- FAISS vector search
- Local LLM inference (Phi-2)
- CLI chat interface
- FastAPI REST API

## Tech Stack
- Python
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- PyTorch
- FastAPI

## Architecture
PDF → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

## Usage
1. Run ingestion:
```bash
python ingest.py
CLI chat:

python chat.py
API:

uvicorn api:app --reload


---

