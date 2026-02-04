from typing import List, Dict
import os
import faiss
from sentence_transformers import SentenceTransformer
from utils import load_pdf_by_page, chunk_by_section, save_pickle

# -------------------------------
# Pre-initialize variables 
# -------------------------------
chunks: List[Dict] = []
embeddings = None
index = None

# -------------------------------
# File paths
# -------------------------------
PDF_PATH = "data/autism_thesis.pdf"
INDEX_PATH = "index/faiss.index"
CHUNKS_PATH = "index/chunks.pkl"

# Ensure index folder exists
os.makedirs("index", exist_ok=True)

print("INGEST SCRIPT STARTED")

# -------------------------------
# Load PDF
# -------------------------------
print("Loading PDF by page...")
pages = load_pdf_by_page(PDF_PATH)

# -------------------------------
# Chunk text by section + page
# -------------------------------
print("Chunking by section headers...")
chunks = chunk_by_section(pages)

# Extract texts for embeddings
texts = [c["text"] for c in chunks]

# -------------------------------
# Create embeddings
# -------------------------------
print("Loading embedding model...")
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Creating embeddings...")
embeddings = embedder.encode(texts, show_progress_bar=True)

# -------------------------------
# Create FAISS index
# -------------------------------
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# -------------------------------
# Save index and chunks
# -------------------------------
print("Saving index and metadata...")
faiss.write_index(index, INDEX_PATH)
save_pickle(chunks, CHUNKS_PATH)

print("Ingestion complete!")
