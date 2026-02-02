# Day 10: Demo Day

## FDE Track - Week 2, Day 10

---

## The Situation

### "Show Time"

```
It's Week 2 Demo Day. You'll present your work to:
- Academy mentors (playing the role of client stakeholders)
- Peer FDEs (who will ask tough questions)

You need to demonstrate:
1. Working RAG system with improved retrieval
2. Multi-agent (or single-agent with tools) architecture
3. Deployed, monitored production system

This is practice for real client demos. 
Treat it like a €2M deal is on the line.

Because someday, it will be.
```

---

## Your Challenge

Deliver a compelling 10-minute demo that would win a client.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Working Demo** | No crashes, smooth flow |
| **Clear Story** | Problem → Solution → Value |
| **Technical Depth** | Can explain architecture |
| **Handles Questions** | Answers or gracefully defers |
| **Professional** | Confident, clear, concise |

### Demo Structure (10 minutes)

| Section | Time | Content |
|---------|------|---------|
| Hook | 1 min | The business problem |
| Demo | 5 min | Show it working |
| Architecture | 2 min | How it works |
| What's Next | 1 min | Roadmap |
| Q&A | 5 min | Audience questions |

---

## Demo Script Template

### 1. The Hook (1 minute)

Start with the PROBLEM, not the technology.

**Bad:** "I built a RAG system with multi-agent orchestration..."

**Good:** "GlobalBank's compliance team spends 4 hours per day searching policy documents. What if they could just ask a question and get the answer in seconds - with citations to the exact source?"

### 2. The Demo (5 minutes)

Show, don't tell. Follow this flow:

**a) Easy Win (1 min)**
- Upload a document (or show pre-uploaded)
- Ask a straightforward question
- Show accurate answer with citation

**b) Harder Challenge (2 min)**
- Ask something that requires synthesis
- Or multi-agent coordination
- Show it handles complexity

**c) Edge Case (1 min)**
- Ask something NOT in the document
- Show graceful "I don't have information about that"
- This builds trust - it doesn't make things up

**d) Real-World Touch (1 min)**
- Show monitoring dashboard briefly
- "Here's how we know it's working in production"

### 3. Architecture (2 minutes)

Keep it simple: 3-4 boxes maximum.

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│  User    │───▶│  Agent   │───▶│  LLM     │
│Interface │    │ + Tools  │    │ (Gemini) │
└──────────┘    └────┬─────┘    └──────────┘
                     │
              ┌──────┴──────┐
              │  Vector DB  │
              │  (AI Search)│
              └─────────────┘
```

Explain:
- Why these technology choices?
- What was the hardest part?
- What would you do differently?

### 4. What's Next (1 minute)

Show you're thinking ahead:
- "Phase 2 would add multi-language support"
- "We'd need X more weeks for production hardening"
- "Key risk to address: performance at scale"

---

## Handling Questions

### Technical Questions You'll Get

| Question | Good Response |
|----------|---------------|
| "What if the document is 1000 pages?" | "Current chunking handles up to X. For larger docs, we'd implement hierarchical chunking." |
| "What's the latency?" | "P95 is X seconds. We can improve with caching and smaller models for simple queries." |
| "How do you prevent hallucination?" | "Three safeguards: grounding to retrieved docs, confidence thresholds, explicit 'I don't know' handling." |

### Business Questions You'll Get

| Question | Good Response |
|----------|---------------|
| "What does this cost?" | "Current setup costs approximately €X/month for Y users. Scales linearly with usage." |
| "How long to production?" | "With security review and integration, estimate 6-8 weeks for enterprise deployment." |
| "What's the ROI?" | "If it saves 2 hours/day for 50 analysts at €50/hour, that's €X/year in productivity." |

### Questions You Can Defer

It's OK to say:
- "That's a great question. I'd need to research the specific numbers."
- "For that use case, I'd recommend a discovery session to understand requirements."
- "That's on the roadmap for Phase 2."

Never make up an answer.

---

## Week 2 Checkpoint

Submit BEFORE your demo:

### Required Deliverables

1. **Technical Artifacts**
   - [ ] Improved RAG system (code repository)
   - [ ] Test suite with results (10+ test cases)
   - [ ] Deployed application URL
   - [ ] Monitoring dashboard screenshot

2. **Documentation**
   - [ ] Architecture diagram
   - [ ] Deployment runbook
   - [ ] Demo script

3. **Reflection** (300-500 words)
   - What was your biggest challenge this week?
   - What would you do differently with more time?
   - What did you learn about FDE work?

---

## Peer Review Criteria

When watching peer demos, evaluate:

| Criterion | Score 1-5 | Notes |
|-----------|-----------|-------|
| Did the demo work without errors? | | |
| Was the business value clear? | | |
| Could you understand the architecture? | | |
| Did they handle questions well? | | |
| Would you trust them on your project? | | |

Provide constructive written feedback to your assigned peer.

---

## Connection to Team Projects

Next week is spring break. Use it to rest and reflect.

When you return for Week 4, everything changes:
- You'll work in cross-functional teams (1 person per role)
- Real client problems, not exercises
- Collaboration across FDE, AI-SE, AI-PM, and other roles
- Building something that could actually ship

Everything you learned these two weeks - demos, RAG, agents, deployment, monitoring - you'll apply in a team context.

**Rest up. The real work begins in Week 4.**
