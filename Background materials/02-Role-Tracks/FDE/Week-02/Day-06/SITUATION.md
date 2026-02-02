# Day 6: Documents Won't Load

## FDE Track - Week 2, Day 6

---

## The Situation

### "It Worked Yesterday"

```
GlobalBank signed the contract. You're building the real system now.

But there's a problem. The pilot users are complaining:

"We uploaded our 200-page compliance manual. The AI 
can't find anything in it. We ask 'What's the policy 
on data retention?' and it says 'I don't have 
information about that.' But it's RIGHT THERE on page 47!"

You check the logs. The document was processed. 
Chunks were created. Embeddings were generated.
But retrieval is returning irrelevant chunks.

The pilot review is in 3 days. 
You need to figure out why RAG isn't working.
```

---

## Your Challenge

Diagnose and fix the RAG pipeline to improve retrieval accuracy.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Diagnosis** | Root cause identified with evidence |
| **Fix** | Measurable improvement in retrieval |
| **Testing** | Test suite that catches similar issues |
| **Documentation** | Clear explanation of what went wrong |

### Deliverables

1. **Diagnosis Report** (1 page)
   - What's the actual problem?
   - How did you identify it?
   - Root cause analysis

2. **Fixed Pipeline** (working code)
   - Improved chunking strategy
   - Better retrieval configuration
   - Measurable improvement

3. **Test Suite** (5-10 test cases)
   - Known questions with expected answers
   - Edge cases that were failing

---

## Micro-Context (5 minutes)

> RAG looks simple but fails in subtle ways. Today you'll learn where RAG pipelines break and how to fix them.
>
> Common RAG failure modes:
> - **Bad chunking** - Splitting in wrong places, losing context
> - **Bad embeddings** - Semantic mismatch between query and content
> - **Bad retrieval** - Wrong K, wrong similarity threshold
> - **Bad prompting** - Context not used effectively by LLM
>
> Your AI Tutor knows RAG debugging patterns. But YOU need to figure out which failure mode you're hitting.
>
> Hint: The problem is almost never "the AI is broken." It's usually data or configuration.

---

## Debugging Framework

### Step 1: Isolate the Problem

```
Question: "What's the policy on data retention?"
Expected: Chunk from page 47 about data retention
Actual: Chunks about [something else]

Is the problem:
□ Chunking? (Is the right content in a chunk?)
□ Embedding? (Is the chunk findable by semantic search?)
□ Retrieval? (Is the chunk in top-K results?)
□ Generation? (Is the LLM using the chunk correctly?)
```

### Step 2: Check Each Layer

**Chunking check:**
- Find the source text in the original document
- Find which chunk(s) contain that text
- Is the context preserved? Is it split awkwardly?

**Embedding check:**
- What's the embedding of the query?
- What's the embedding of the expected chunk?
- What's the similarity score?

**Retrieval check:**
- What are the top-5 chunks returned?
- Where does the expected chunk rank?
- What chunks are beating it?

**Generation check:**
- If you manually add the right chunk to context, does LLM answer correctly?

---

## Common Problems & Fixes

### Problem: Chunks Split Mid-Sentence

```
Bad: "...data retention policy requires all records to be"
     [CHUNK BREAK]
     "kept for 7 years according to regulation..."

Good: "Data retention policy requires all records to be 
      kept for 7 years according to regulation XYZ."
```

**Fix:** Chunk by paragraphs/sections, not fixed character count.

### Problem: Query-Document Mismatch

```
Query: "What's the policy on data retention?"
Chunk: "Records must be maintained for the legally 
       mandated duration as per compliance requirements."

Same meaning, different words → Low similarity score
```

**Fix:** Use hypothetical document embedding (HyDE) or query expansion.

### Problem: Wrong K Value

```
K=3: Misses relevant chunk ranked #4
K=20: Too much noise dilutes the signal
```

**Fix:** Test different K values. Consider reranking.

### Problem: Table/List Formatting

```
Original: Clean table with headers and rows
After chunking: Jumbled text, headers separated from data
```

**Fix:** Preserve structure in preprocessing, use table-aware chunking.

---

## Hints

<details>
<summary>Hint 1: Quick diagnosis (Click after 10 min)</summary>

Start here:
1. Pick one failing question
2. Find where the answer is in the original doc
3. Find which chunk contains that text
4. Check if that chunk appears in retrieval results

If the chunk doesn't exist → Chunking problem
If the chunk exists but isn't retrieved → Embedding/retrieval problem
If the chunk is retrieved but answer is wrong → Generation problem
</details>

<details>
<summary>Hint 2: Chunking improvements (Click after 20 min)</summary>

Better chunking strategies:
- **Semantic chunking:** Split at paragraph/section boundaries
- **Overlap:** 10-20% overlap between chunks preserves context
- **Metadata:** Keep page numbers, section headers with chunks
- **Hierarchical:** Parent chunk for context, child chunks for retrieval

For compliance documents: Try chunking by section headers.
</details>

<details>
<summary>Hint 3: Retrieval tuning (Click after 35 min)</summary>

Retrieval improvements:
- **Hybrid search:** Combine semantic + keyword search
- **Reranking:** Use a cross-encoder to rerank top results
- **Query expansion:** Add synonyms or rephrase query
- **Metadata filtering:** Filter by section before semantic search

For this case: Try adding keyword search for "data retention" alongside semantic search.
</details>

---

## Testing Strategy

### Create a Test Suite

```python
test_cases = [
    {
        "question": "What's the policy on data retention?",
        "expected_source": "page 47, section 3.2",
        "expected_keywords": ["7 years", "records", "retention"]
    },
    {
        "question": "Who approves access requests?",
        "expected_source": "page 12, section 1.4",
        "expected_keywords": ["manager", "approval", "access"]
    },
    # ... more cases
]
```

### Metrics to Track

| Metric | What It Measures | Target |
|--------|------------------|--------|
| Retrieval Precision@5 | % of top-5 chunks that are relevant | >60% |
| Retrieval Recall | % of relevant chunks in top-K | >80% |
| Answer Accuracy | % of correct answers | >85% |
| Source Attribution | % with correct citation | >90% |

---

## Self-Study Assignment (90 min)

1. **Fix your pipeline** - Implement at least 2 improvements (45 min)
2. **Build test suite** - 10 question-answer pairs (30 min)
3. **Document changes** - What you changed and why (15 min)

### Stretch Goals
- Implement hybrid search (keyword + semantic)
- Add chunk metadata (page number, section)
- Build a retrieval evaluation dashboard
