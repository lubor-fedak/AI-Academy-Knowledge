# Lab 02: Instructions

## Phase 1: Document Processing (30 min)

### Step 1.1: Load Documents

Your first task is to load the sample documents from the `/data/` folder.

**Requirements:**
- Support multiple file types (.txt, .md)
- Extract text content
- Preserve document metadata (filename, source)

### Step 1.2: Implement Chunking

Documents need to be split into smaller chunks for effective retrieval.

**Chunking considerations:**
- **Chunk size:** Too small = no context, too large = noise
- **Overlap:** Helps maintain context across boundaries
- **Strategy:** Fixed size, sentence-based, or semantic

**Recommended starting point:**
- Chunk size: 500-1000 characters
- Overlap: 100-200 characters

**Questions to answer:**
- How does chunk size affect retrieval quality?
- What happens with code blocks or tables?
- How do you handle section headers?

### Step 1.3: Create Chunk Metadata

Each chunk should include:
```python
{
    "id": "unique_id",
    "text": "chunk content...",
    "source": "filename.md",
    "chunk_index": 0,
    "total_chunks": 10
}
```

---

## Phase 2: Embedding & Indexing (30 min)

### Step 2.1: Generate Embeddings

Use Gemini's embedding model or sentence-transformers:

```python
# Option A: Gemini
import google.generativeai as genai
result = genai.embed_content(
    model="models/embedding-001",
    content="Your text here"
)
embedding = result['embedding']

# Option B: sentence-transformers
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode("Your text here")
```

### Step 2.2: Set Up Vector Store

Use ChromaDB for local vector storage:

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("my_documents")

# Add documents
collection.add(
    documents=["text1", "text2"],
    metadatas=[{"source": "doc1"}, {"source": "doc2"}],
    ids=["id1", "id2"]
)
```

### Step 2.3: Index All Chunks

Create a function that:
1. Takes all chunks
2. Generates embeddings
3. Stores in vector database
4. Handles batching for large document sets

**Watch for:**
- API rate limits on embedding calls
- Memory usage with large documents
- Duplicate detection

---

## Phase 3: Retrieval Implementation (30 min)

### Step 3.1: Implement Search

Create a search function that:
- Takes a query string
- Embeds the query
- Finds K nearest neighbors
- Returns ranked results

```python
def search(query: str, k: int = 5) -> list[dict]:
    # TODO: Implement
    pass
```

### Step 3.2: Experiment with K

Test different values of K (number of retrieved chunks):
- K=1: Very focused, might miss context
- K=3: Balanced
- K=10: More context, more noise

**Document your findings:**
- Which K works best for your documents?
- How does retrieval time change with K?

### Step 3.3: Add Re-ranking (Optional)

Simple re-ranking strategies:
- Keyword matching boost
- Recency weighting
- Source diversity

---

## Phase 4: RAG Integration (20 min)

### Step 4.1: Create RAG Prompt Template

Design a prompt that:
- Includes retrieved context
- Instructs the model to use only provided information
- Handles cases where answer isn't in context

**Template structure:**
```
You are a helpful assistant. Answer the question based ONLY on 
the following context. If the answer is not in the context, 
say "I don't have information about that."

Context:
{retrieved_chunks}

Question: {user_question}

Answer:
```

### Step 4.2: Implement RAG Function

```python
def rag_answer(question: str) -> str:
    # 1. Retrieve relevant chunks
    chunks = search(question, k=3)
    
    # 2. Format context
    context = format_chunks(chunks)
    
    # 3. Generate answer
    answer = generate_with_context(question, context)
    
    # 4. Return with sources
    return answer, chunks
```

### Step 4.3: Add Source Attribution

For transparency, include which documents were used:
- List source documents
- Optionally show relevant excerpts
- Enable verification

---

## Phase 5: Testing (10 min)

### Test Cases

Create 10 test questions covering:
1. **Direct questions:** Answer is clearly in one chunk
2. **Multi-chunk:** Answer requires combining information
3. **Not found:** Answer is NOT in the documents
4. **Ambiguous:** Question could match multiple topics
5. **Edge cases:** Very short query, very long query

### Evaluation

For each test, record:
- Question
- Retrieved chunks (were they relevant?)
- Answer (was it correct?)
- Time taken

---

## Extension Challenges

1. **Hybrid search:** Combine semantic + keyword search
2. **Query expansion:** Rephrase query for better retrieval
3. **Chunk overlap visualization:** Show how chunks relate
4. **Comparison:** Test different embedding models
5. **Evaluation metrics:** Implement precision@k, recall@k

---

## Submission

Upload to SharePoint `/07-Submissions/Labs/Lab-02/`:
- `rag_pipeline.py` (main code)
- `chunking_strategy.md` (your approach)
- `test_results.csv` (10 Q&A pairs with evaluation)
- `REFLECTION.md`
