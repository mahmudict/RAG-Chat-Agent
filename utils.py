import pickle
import re
from pypdf import PdfReader


# =========================================================
# PDF LOADING 
# =========================================================

def load_pdf_by_page(pdf_path):
    """
    Load PDF and return a list of dicts:
    [
        {"page": 1, "text": "..."},
        {"page": 2, "text": "..."},
        ...
    ]
    """
    reader = PdfReader(pdf_path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages.append({
                "page": i + 1,
                "text": text
            })

    return pages


# =========================================================
# SECTION HEADER DETECTION
# =========================================================

def is_section_header(line):
    """
    Heuristic-based section header detection.
    Works well for academic / technical PDFs.
    """
    line = line.strip()

    if len(line) < 4 or len(line) > 100:
        return False

    # All caps headers
    if line.isupper():
        return True

    # Title Case headers (e.g., "Materials and Methods")
    if re.match(r"^[A-Z][A-Za-z0-9\s\-]{3,}$", line):
        return True

    return False


# =========================================================
# CHUNKING BY SECTION + PAGE + PARAGRAPH
# =========================================================

def chunk_by_section(pages, max_words=200):
    """
    Create chunks with metadata:
    {
        "text": "...",
        "page": page_number,
        "section": section_title
    }
    """
    chunks = []

    for page in pages:
        page_num = page["page"]
        lines = page["text"].split("\n")

        current_section = "Unknown Section"
        current_chunk = []
        current_length = 0

        for line in lines:
            line = line.strip()

            if not line:
                continue

            # Detect section headers
            if is_section_header(line):
                current_section = line
                continue

            words = line.split()

            # If chunk too large, save it
            if current_length + len(words) > max_words and current_chunk:
                chunks.append({
                    "text": " ".join(current_chunk),
                    "page": page_num,
                    "section": current_section
                })
                current_chunk = []
                current_length = 0

            current_chunk.append(line)
            current_length += len(words)

        # Save remaining text
        if current_chunk:
            chunks.append({
                "text": " ".join(current_chunk),
                "page": page_num,
                "section": current_section
            })

    return chunks


# =========================================================
# PICKLE UTILITIES
# =========================================================

def save_pickle(obj, path):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)
