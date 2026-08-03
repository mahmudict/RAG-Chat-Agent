# 🧠 RAG Chat System (PDF Question Answering with FAISS + LLM)

A Retrieval-Augmented Generation (RAG) system that enables intelligent question answering over academic PDF documents using vector search (FAISS), sentence embeddings, and a local LLM.

This project demonstrates an end-to-end AI system combining information retrieval, embeddings, and generative AI, exposed via both CLI and FastAPI interfaces.

---

## 📌 Project Motivation

Academic PDFs contain dense and unstructured information, making manual search inefficient.

This system solves this problem by:

- Converting PDFs into searchable semantic chunks  
- Retrieving relevant context using vector similarity  
- Generating accurate answers using a local language model  

👉 Designed for research, education, and real-world document intelligence applications.

---

## ✨ Features

- 📄 Page-aware PDF ingestion  
- 🧩 Semantic chunking based on document structure  
- 🔍 FAISS-based vector similarity search  
- 🤖 Local LLM inference (Phi-2 or similar)  
- 💬 CLI-based chat interface  
- 🌐 FastAPI REST API for integration  

---

## 🧱 System Architecture

```
PDF Documents
→ Text Extraction & Chunking
→ Sentence Embeddings (Transformers)
→ FAISS Vector Index
→ Top-K Retrieval
→ Local LLM (Phi-2)
→ Generated Answer
```

---

## 🛠 Tech Stack

- Python  
- FAISS  
- Sentence Transformers  
- Hugging Face Transformers  
- PyTorch  
- FastAPI  

---

## 📁 Project Structure

```
RAG-Chat-Agent/
│── api.py           # FastAPI server
│── chat.py          # CLI chat interface
│── ingest.py        # PDF ingestion pipeline
│── utils.py         # Helper functions
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mahmudict/RAG-Chat-Agent.git
cd RAG-Chat-Agent
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔹 1. Ingest PDF documents
```bash
python ingest.py
```

This will:
- Extract text from PDFs  
- Split into semantic chunks  
- Generate embeddings  
- Build FAISS index  

---

### 🔹 2. Run CLI chat interface
```bash
python chat.py
```

---

### 🔹 3. Start FastAPI server
```bash
uvicorn api:app --reload
```

API will be available at:
```
http://127.0.0.1:8000
```

---

## 📡 Example API Request

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d '{"question": "Summarize the document"}'
```

---

## 📊 Key Design Decisions

### 🧩 Chunking Strategy
- Section-based semantic chunking improves retrieval accuracy  
- Maintains context across document sections  

### 🔍 Vector Search
- FAISS enables fast nearest neighbor search  
- Efficient for large document collections  

### 🤖 LLM Integration
- Uses local LLM inference (no external API dependency)  
- Ensures privacy and offline capability  

---

## 🧠 Skills Demonstrated

- End-to-end AI system design  
- Retrieval-Augmented Generation (RAG)  
- Vector databases (FAISS)  
- NLP and embeddings  
- API development (FastAPI)  
- Modular Python engineering  

---

## 📌 Limitations

- Model performance depends on embedding quality  
- No cloud deployment yet  
- Designed primarily for academic PDFs  

---

## 🚀 Future Improvements

- Docker containerization  
- Cloud deployment (AWS EC2 / S3)  
- Retrieval evaluation metrics  
- Streaming responses  

---

## 📄 Important Note

- This repository focuses on **system design and implementation**  
- No sensitive or proprietary datasets or models are included  
- Intended for educational and portfolio purposes only  

---

## 👨‍💻 Author

**Md. Mahmudul Hasan**

- AI / ML Engineer (aspiring)  
- Research background in medical AI (fMRI, autism detection)  
- Experience in machine learning, deep learning, and AI systems  

---

## 📚 Publications & Research

- Peer-reviewed conference papers (IEEE, 2019)  
- Peer-reviewed abstracts (Neurology, 2025; Journal of Neuroimaging, 2026)  
- Master’s thesis: Autism Spectrum Disorder detection and functional connectivity pattern mining using fMRI with CNNs  


---

## 📜 License

MIT License
