# Lab 02: Build a RAG Pipeline

## Overview

RAG (Retrieval-Augmented Generation) is the most common pattern for building AI applications that need to answer questions from your own documents. In this lab, you'll build a complete RAG pipeline from scratch.

## Learning Objectives

By the end of this lab, you will be able to:
- Load and chunk documents for vector storage
- Generate and store embeddings
- Implement semantic search over documents
- Augment LLM prompts with retrieved context
- Evaluate retrieval quality

## Prerequisites

- Completed Lab 01 (First Chatbot)
- Understanding of embeddings concept
- Familiarity with vector similarity

## Time Estimate

**Total: 120 minutes**
- Document processing: 30 minutes
- Embedding & indexing: 30 minutes
- Retrieval implementation: 30 minutes
- RAG integration: 20 minutes
- Testing: 10 minutes

## Target Roles

- **Primary:** FDE, AI-SE, AI-DS
- **Secondary:** All technical roles

## Architecture

```
┌─────────────┐     ┌─────────────┐
│  Documents  │────▶│   Chunker   │
└─────────────┘     └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Embedder   │
                    └──────┬──────┘
                           │
                           ▼
┌─────────────┐     ┌─────────────┐
│    Query    │────▶│Vector Store │
└─────────────┘     └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Retriever  │
                    │  (Top K)    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │     LLM     │
                    │  + Context  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Answer    │
                    └─────────────┘
```

## Success Criteria

- [ ] Documents are loaded and chunked appropriately
- [ ] Embeddings are generated and stored
- [ ] Semantic search returns relevant chunks
- [ ] RAG system answers questions from documents
- [ ] System handles "I don't know" cases appropriately
- [ ] Basic retrieval metrics are measured

## Deliverables

1. **RAG Pipeline** (`rag_pipeline.py`) - complete implementation
2. **Chunking strategy** - documented approach with rationale
3. **Test results** - 10 question-answer pairs with evaluation
4. **Reflection** - what worked, what didn't, improvements

## Tools & Resources

- **Embeddings:** Gemini embedding API or sentence-transformers
- **Vector Store:** ChromaDB (local) or FAISS
- **Documents:** Sample documents provided in `/data/`
