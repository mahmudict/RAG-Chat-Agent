Markdown
1
# 🧠 RAG Chat System (PDF Question Answering with FAISS + LLM)
2
 
3
A Retrieval-Augmented Generation (RAG) system that enables intelligent question answering over academic PDF documents using vector search (FAISS), sentence embeddings, and a local LLM.
4
 
5
This project demonstrates an end-to-end AI system combining **information retrieval, embeddings, and generative AI**, exposed via both CLI and FastAPI interfaces.
6
 
7
---
8
 
9
## 📌 Project Motivation
10
 
11
Academic PDFs contain dense and unstructured information, making manual search inefficient.
12
 
13
This system solves that problem by:
14
- Converting PDFs into searchable semantic chunks
15
- Retrieving relevant context using vector similarity
16
- Generating accurate answers using a local language model
17
 
18
👉 Designed for research, education, and real-world document intelligence applications.
19
 
20
---
21
 
22
## ✨ Features
23
 
24
- 📄 Page-aware PDF ingestion
25
- 🧩 Semantic chunking based on document structure
26
- 🔍 FAISS-based vector similarity search
27
- 🤖 Local LLM inference (Phi-2 or similar)
28
- 💬 CLI-based chat interface
29
- 🌐 FastAPI REST API for integration
30
 
31
---
32
 
33
## 🧱 System Architecture
Show less

PDF Documents ↓ Text Extraction & Chunking ↓ Sentence Embeddings (Transformers) ↓ FAISS Vector Index ↓ Top-K Retrieval ↓ Local LLM (Phi-2) ↓ Generated Answer


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



RAG-Chat-Agent/ │── api.py # FastAPI server │── chat.py # CLI chat interface │── ingest.py # PDF ingestion + indexing │── utils.py # Helper functions │── requirements.txt # Dependencies │── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mahmudict/RAG-Chat-Agent.git
cd RAG-Chat-Agent

2️⃣ Create virtual environment (recommended)
Shell
1
python -m venv venv
2
source venv/bin/activate # Linux/Mac
3
venv\Scripts\activate # Windows
Show more lines
3️⃣ Install dependencies
Shell
1
pip install -r requirements.txt
Show more lines
🚀 Usage
🔹 1. Ingest PDF documents
Shell
1
python ingest.py
Show more lines

This:

Extracts text from PDFs
Splits into chunks
Generates embeddings
Builds FAISS index
🔹 2. Run CLI chat interface
Shell
1
python chat.py
Show more lines

Ask questions interactively:

User: What is the main contribution of the paper?
Bot: ...

🔹 3. Start FastAPI server
Shell
1
uvicorn api:app --reload
Show more lines

API runs at:

http://127.0.0.1:8000

📡 Example API Request
Shell
1
curl -X POST "http://127.0.0.1:8000/chat" \
2
-H "Content-Type: application/json" \
3
-d '{"question": "Summarize the document"}'
Show more lines
📊 Key Design Decisions
🧩 Chunking Strategy
Section-based semantic chunking improves retrieval accuracy
Maintains context across document sections
🔍 Vector Search
FAISS enables fast approximate nearest neighbor search
Scales efficiently for large document collections
🤖 LLM Integration
Uses local LLM inference (no external API dependency)
Ensures privacy and offline capability
🧠 Skills Demonstrated
End-to-end AI system design
Retrieval-Augmented Generation (RAG)
Vector databases (FAISS)
NLP and embeddings
API development (FastAPI)
Modular Python engineering
📌 Limitations
Model performance depends on embedding quality
No cloud deployment included (future improvement)
Designed for academic PDFs (generalization possible)
🚀 Future Improvements
🐳 Docker containerization
☁️ Cloud deployment (AWS EC2 / S3)
📊 Retrieval evaluation metrics
🖥 Web UI (Streamlit / React frontend)
⚡ Streaming responses
📄 Important Note
This repository focuses on system design and implementation
No sensitive or proprietary models or datasets are included
Intended for educational and portfolio purposes only
👨‍💻 Author

Md. Mahmudul Hasan

AI / ML Engineer (aspiring)
Research background in medical AI (fMRI, autism detection)
Experience in:
Machine learning
Deep learning
AI system development
📚 Publications & Research
Peer-reviewed conference papers (IEEE, 2019)
Peer-reviewed abstracts (Neurology, 2025; Journal of Neuroimaging, 2026)
Master's thesis:
Autism Spectrum Disorder detection using fMRI with CNNs

👉 Demonstrates strong research and applied AI background

📜 License

This project is licensed under the MIT License.
