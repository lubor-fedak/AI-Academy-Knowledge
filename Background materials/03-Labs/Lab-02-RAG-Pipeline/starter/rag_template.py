"""
AI Academy - Lab 02: RAG Pipeline
Starter template
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ============================================
# PHASE 1: Document Processing
# ============================================

def load_documents(folder_path: str) -> list[dict]:
    """Load all documents from a folder."""
    documents = []
    # TODO: Load .txt and .md files
    # TODO: Extract text and metadata
    return documents


def chunk_document(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """Split document into overlapping chunks."""
    chunks = []
    # TODO: Implement chunking logic
    return chunks


def process_documents(folder_path: str) -> list[dict]:
    """Load and chunk all documents."""
    # TODO: Combine loading and chunking
    pass


# ============================================
# PHASE 2: Embedding & Indexing
# ============================================

def generate_embedding(text: str) -> list[float]:
    """Generate embedding for text."""
    # TODO: Use Gemini or sentence-transformers
    pass


def create_index(chunks: list[dict]):
    """Create vector index from chunks."""
    # TODO: Set up ChromaDB
    # TODO: Index all chunks
    pass


# ============================================
# PHASE 3: Retrieval
# ============================================

def search(query: str, k: int = 3) -> list[dict]:
    """Search for relevant chunks."""
    # TODO: Embed query
    # TODO: Search vector store
    # TODO: Return top K results
    pass


# ============================================
# PHASE 4: RAG
# ============================================

RAG_PROMPT = """
You are a helpful assistant. Answer the question based ONLY on 
the following context. If the answer is not in the context, 
say "I don't have information about that in the provided documents."

Context:
{context}

Question: {question}

Answer:
"""


def rag_answer(question: str) -> tuple[str, list[dict]]:
    """Generate RAG answer with sources."""
    # TODO: Retrieve relevant chunks
    # TODO: Format context
    # TODO: Generate answer
    # TODO: Return answer and sources
    pass


# ============================================
# Main
# ============================================

def main():
    # 1. Process documents
    print("Processing documents...")
    # chunks = process_documents("./data")
    
    # 2. Create index
    print("Creating index...")
    # create_index(chunks)
    
    # 3. Interactive Q&A
    print("\nRAG System Ready! Ask questions about the documents.")
    print("Type 'quit' to exit.\n")
    
    while True:
        question = input("Question: ")
        if question.lower() == 'quit':
            break
        
        # answer, sources = rag_answer(question)
        # print(f"\nAnswer: {answer}")
        # print(f"Sources: {[s['source'] for s in sources]}\n")


if __name__ == "__main__":
    main()
