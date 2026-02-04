from typing import List, Dict
import faiss
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
from utils import load_pickle

# -------------------------------
# Pre-initialize variables (VS Code safe)
# -------------------------------
chunks: List[Dict] = []
index = None
embedder = None
tokenizer = None
model = None

# -------------------------------
# File paths
# -------------------------------
INDEX_PATH = "index/faiss.index"
CHUNKS_PATH = "index/chunks.pkl"

print("CHAT SCRIPT STARTED")

# -------------------------------
# Load FAISS index & chunks
# -------------------------------
print("Loading FAISS index...")
index = faiss.read_index(INDEX_PATH)
chunks = load_pickle(CHUNKS_PATH)

# -------------------------------
# Load embedding model
# -------------------------------
print("Loading embedding model...")
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# -------------------------------
# Load LLM
# -------------------------------
print("Loading LLM...")
model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# -------------------------------
# Retrieve context
# -------------------------------
def retrieve_context(question: str, k: int = 3) -> str:
    q_embedding = embedder.encode([question])
    _, indices = index.search(q_embedding, k)

    contexts = []
    for i in indices[0]:
        chunk = chunks[i]
        contexts.append(
            f"[Page {chunk['page']} | Section: {chunk['section']}]\n{chunk['text']}"
        )
    return "\n\n".join(contexts)

# -------------------------------
# Generate answer
# -------------------------------
def generate_answer(question: str) -> str:
    context = retrieve_context(question)

    prompt = f"""
You are a helpful assistant.
Answer ONLY from the context.
If the answer is not in the context, say "I don't know".

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
            temperature=0.3,
            do_sample=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# -------------------------------
# Chat loop
# -------------------------------
print("\nChat ready. Type 'exit' to quit.\n")

while True:
    q = input("You: ")
    if q.lower() == "exit":
        break

    ans = generate_answer(q)
    print("\nAssistant:\n", ans)

