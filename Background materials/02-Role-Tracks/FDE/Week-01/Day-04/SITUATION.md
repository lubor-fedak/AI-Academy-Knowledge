# Day 4: Customer Wants a Demo

## FDE Track - Week 1, Day 4

---

## The Situation

### "The Impossible Demo"

```
It's 4 PM on Thursday. Your manager calls.

"Great news! The VP of Digital at GlobalBank loved our 
pitch. They want to see a working demo of an AI assistant 
that can answer questions about their internal policies.

They're flying in Monday morning. 9 AM.

I know it's tight, but this is a €2M opportunity. 
We need to show them something real, not slides.

They'll bring 3 sample policy documents. The assistant 
needs to answer questions about those documents accurately.

Can you make this happen?"

You have until Monday 9 AM. That's roughly 60 working hours.
```

---

## Your Challenge

Build a working RAG demo that can answer questions about uploaded documents.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Works** | Demo answers questions about provided documents |
| **Accurate** | Answers are grounded in document content |
| **Professional** | Looks like a product, not a prototype |
| **Resilient** | Handles edge cases gracefully |
| **Explainable** | You can explain how it works to a VP |

### Deliverables

1. **Working Demo** (accessible via URL)
   - Document upload capability
   - Question-answering interface
   - Source citation for answers

2. **Demo Script** (1 page)
   - What you'll show
   - What questions you'll ask
   - How you'll handle "what if" questions

3. **Technical Brief** (1 page)
   - Architecture overview
   - Technology choices and rationale
   - Known limitations

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | Mentor introduction |
| Planning | 15 min | Architecture decisions |
| Building | 45 min | Core implementation |
| Testing | 15 min | Break your own demo |
| Documentation | 10 min | Demo script |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> FDEs live in the world of "yes, and..." You said yes to the demo. Now you need to deliver.
>
> Key concepts for today:
> - **RAG** - Retrieval-Augmented Generation: search documents, feed context to LLM
> - **Chunking** - Breaking documents into searchable pieces
> - **Embedding** - Converting text to vectors for similarity search
> - **Grounding** - Making sure answers come from actual documents
>
> Your AI Tutor knows RAG patterns. Your job is to build something that works by Monday.
>
> Hint: Start with the simplest thing that could possibly work. You can make it fancy later.

---

## Architecture Decision

Before coding, decide:

### Option A: All-in-One (Fastest)
```
Antigravity + Gemini API
├── Simple chunking (split by paragraphs)
├── In-memory vector search
└── Single prompt with retrieved context
```
**Pros:** Fast to build, minimal infrastructure  
**Cons:** Won't scale, no persistence

### Option B: Production-Lite
```
Antigravity + Gemini API + Azure AI Search
├── Proper chunking with overlap
├── Persistent vector index
└── Structured retrieval pipeline
```
**Pros:** More robust, closer to production  
**Cons:** More setup time

**For a Monday demo:** Option A is probably right. But know its limitations.

---

## Technical Starting Points

### Minimal RAG Flow

```
1. INGEST
   Document → Chunks → Embeddings → Store

2. QUERY
   Question → Embedding → Search → Top-K chunks

3. GENERATE
   Question + Retrieved Chunks → LLM → Answer with citations
```

### Key Questions to Answer

- How do you chunk documents? (by page? paragraph? fixed size?)
- How many chunks do you retrieve? (3? 5? 10?)
- How do you format the prompt with context?
- How do you cite sources in the answer?

---

## Hints

<details>
<summary>Hint 1: Chunking strategy (Click after 10 min)</summary>

Start simple:
- Split by paragraphs or sections
- Keep chunks 200-500 tokens
- Include some overlap (50-100 tokens)

Don't over-engineer chunking for a demo. Get something working first.
</details>

<details>
<summary>Hint 2: Prompt structure (Click after 20 min)</summary>

```
System: You are a helpful assistant that answers questions 
based ONLY on the provided context. If the answer is not 
in the context, say "I don't have information about that 
in the provided documents."

Context:
[Retrieved chunks here]

User: [Question]
```

Key: Tell the LLM to only use provided context.
</details>

<details>
<summary>Hint 3: Making it look professional (Click after 35 min)</summary>

Quick wins for demo polish:
- Clean, simple UI (white background, clear fonts)
- Loading indicator while processing
- Show source document for each answer
- Handle empty/error states gracefully

The VP won't see your code. They'll see the experience.
</details>

---

## Demo Day Preparation

### What GlobalBank Will Ask

Prepare for these questions:
1. "What if the document is 500 pages?"
2. "How do we know the answer is accurate?"
3. "Can it handle multiple documents?"
4. "What about confidentiality?"
5. "How long to go to production?"

### Demo Script Template

```
1. INTRO (2 min)
   "Let me show you what we've built..."

2. UPLOAD (1 min)
   Upload their sample document
   Show processing confirmation

3. EASY QUESTION (2 min)
   Ask something clearly in the document
   Show answer with citation

4. HARDER QUESTION (2 min)
   Ask something requiring synthesis
   Show how it handles complexity

5. EDGE CASE (2 min)
   Ask something NOT in the document
   Show graceful "I don't know"

6. Q&A (remaining time)
   Handle their questions
```

---

## Peer Review Focus

When reviewing your partner's demo:

1. Does it actually answer questions correctly?
2. What happens when you ask something not in the document?
3. Is the UI clear enough for a VP to use?
4. Could you explain the architecture in 2 minutes?
5. What's the biggest risk for Monday?

---

## Connection to Tomorrow

Tomorrow you'll tackle **scope creep** - what happens when the customer says "great demo, but can it also..." You'll learn to protect scope while keeping customers happy.

---

## Self-Study Assignment (90 min)

1. **Finish your demo** - Make it actually work (60 min)
2. **Write the demo script** - Practice it out loud (15 min)
3. **Break your demo** - Find the edge cases (15 min)

### Stretch Goal
Add source citations that show which document section the answer came from.
