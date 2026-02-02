# Lab 02: Mentor Notes

## Key Concepts to Reinforce

1. **Chunking is critical:** Most RAG problems are chunking problems
2. **Garbage in, garbage out:** Poor retrieval = poor answers
3. **"I don't know" is a feature:** Models should admit uncertainty

## Common Struggles

### "My retrieval returns wrong chunks"
**Causes:**
- Chunk size too large/small
- Poor embedding model choice
- Query doesn't match document vocabulary

**Intervention:** Have them manually inspect retrieved chunks. "Read these chunks - do they contain the answer?"

### "The model ignores my context"
**Causes:**
- Weak system prompt
- Context too long (gets lost)
- Model temperature too high

**Intervention:** Strengthen prompt: "You MUST only use the provided context."

### "It says 'I don't know' for everything"
**Causes:**
- Retrieval threshold too strict
- K too low
- Context not formatted well

**Intervention:** Lower threshold, increase K, check context format

## Debrief Topics

1. **Chunking trade-offs:** What happens with 100-char vs 2000-char chunks?
2. **Embedding quality:** How would you evaluate if embeddings are "good"?
3. **Scaling:** What changes when you have 10,000 documents?
4. **Hybrid approaches:** When would you combine keyword + semantic search?

## What Good Looks Like

- Documented chunking rationale
- Clear retrieval metrics
- Honest "I don't know" handling
- Source attribution in answers

## Connection to Next Labs

- Lab 03 (Multi-Agent): What if different agents handle different document types?
- Lab 05 (Evaluation): How do you measure RAG quality at scale?
