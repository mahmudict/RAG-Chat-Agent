from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import faiss
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
from utils import load_pickle

# -------------------------------
# App
# -------------------------------
app = FastAPI(title="RAG Chat API")

# -------------------------------
# Globals (loaded ONCE)
# -------------------------------
INDEX_PATH = "index/faiss.index"
CHUNKS_PATH = "index/chunks.pkl"

index = faiss.read_index(INDEX_PATH)
chunks = load_pickle(CHUNKS_PATH)

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# -------------------------------
# Request schema
# -------------------------------
class ChatRequest(BaseModel):
    question: str
    top_k: int = 3

# -------------------------------
# Retrieval
# -------------------------------
def retrieve_context(question: str, k: int):
    q_emb = embedder.encode([question])
    _, idxs = index.search(q_emb, k)

    contexts = []
    for i in idxs[0]:
        c = chunks[i]
        contexts.append(
            f"[Page {c['page']} | {c['section']}]\n{c['text']}"
        )
    return "\n\n".join(contexts)

# -------------------------------
# Generation
# -------------------------------
def generate_answer(question: str, k: int):
    context = retrieve_context(question, k)

    prompt = f"""
You are a helpful assistant.
Answer ONLY from the context.
If unknown, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.3
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# -------------------------------
# API endpoint
# -------------------------------
@app.post("/chat")
def chat(req: ChatRequest):
    answer = generate_answer(req.question, req.top_k)
    return {"answer": answer}
