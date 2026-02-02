# Team Project 2: DocuMind

## Enterprise Knowledge Assistant

---

## Project Overview

| Item | Details |
|------|---------|
| **Project Name** | DocuMind |
| **Duration** | Days 11-22 (2 weeks) |
| **Team Size** | 8-10 people (cross-functional) |
| **Pilot Client** | Regional Insurance Company |
| **Budget** | €180,000 simulation |

---

## The Brief

```
CLIENT REQUEST:

"Our insurance agents spend 2 hours per day searching for policy
information, compliance rules, and procedural guidelines. We have
50,000+ documents across SharePoint, legacy systems, and PDF archives.

We want an AI assistant that:
1. Answers agent questions using our internal documents
2. Provides citations so agents can verify information
3. Handles policy-specific queries (e.g., "What's covered under plan X?")
4. Explains complex regulations in simple language

Current pain points:
- Agents give inconsistent answers to customers
- New agents take 6 months to become productive
- Compliance updates get lost in email
- No way to know if agents are using latest information

Success metrics:
- 80% of queries answered correctly (verified by SMEs)
- Response time < 10 seconds
- Agent time on document search reduced by 60%
- New agent onboarding time reduced by 40%

Constraints:
- Documents contain PII (customer names, policy numbers)
- Must not hallucinate policy information (compliance critical)
- Must work offline for branch offices with poor connectivity
- Integration with existing agent desktop (Salesforce)"
```

---

## Required Deliverables

### Week 1 (Days 11-15): Build Phase

| Day | Deliverable | Owner Roles |
|-----|-------------|-------------|
| 11 | Document ingestion pipeline + chunking strategy | FDE, AI-DS |
| 12 | RAG implementation + retrieval optimization | FDE, AI-SE |
| 13 | Citation generation + source verification | AI-DS, FDE |
| 14 | PII handling + data governance | AI-SEC, AI-SE |
| 15 | Accuracy evaluation framework | AI-DS, AI-PM |

**Week 1 Checkpoint:** RAG system answering questions with citations

### Week 2 (Days 16-22): Polish Phase

| Day | Deliverable | Owner Roles |
|-----|-------------|-------------|
| 16-17 | Conversational UI + Salesforce embed | AI-FE, AI-DX |
| 18 | Offline mode + edge deployment | AI-SE, FDE |
| 19 | Usage analytics + feedback collection | AI-DA, AI-FE |
| 20 | Compliance documentation + audit prep | AI-SEC, AI-PM |
| 21 | Performance optimization + load testing | AI-SE, AI-DS |
| 22 | Client demo + handover documentation | All roles |

**Week 2 Checkpoint:** Production-ready RAG with offline capability

---

## Technical Requirements

### Must Have
- [ ] Document ingestion (PDF, Word, SharePoint)
- [ ] Semantic search with >90% relevant retrieval
- [ ] Citation with page/section reference
- [ ] PII masking in prompts and logs
- [ ] Hallucination detection/prevention
- [ ] Response time < 10 seconds

### Should Have
- [ ] Conversational follow-up questions
- [ ] Document freshness tracking
- [ ] Confidence scoring for answers
- [ ] Salesforce Lightning component

### Nice to Have
- [ ] Offline mode with cached documents
- [ ] Voice input for hands-free use
- [ ] Automatic document update detection
- [ ] Multi-language (Slovak, Czech, English)

---

## Role Responsibilities

| Role | Primary Responsibilities |
|------|-------------------------|
| **AI-PM** | Requirements, scope, stakeholder alignment |
| **FDE** | RAG implementation, integrations, demo |
| **AI-SE** | Pipeline architecture, deployment, caching |
| **AI-DS** | Retrieval quality, evaluation, hallucination prevention |
| **AI-DA** | Usage analytics, adoption metrics, ROI |
| **AI-SEC** | PII handling, compliance, audit trail |
| **AI-FE** | Chat UI, Salesforce component, offline mode |
| **AI-DX** | Agent workflow research, UX design |

---

## Data Provided

- Sample document corpus: 5,000 documents (anonymized)
- Test question set: 200 questions with verified answers
- Salesforce sandbox instance
- Azure AI Search instance
- Document classification taxonomy

---

## Evaluation Criteria

| Criterion | Weight | Excellent | Good | Developing |
|-----------|--------|-----------|------|------------|
| **Answer Accuracy** | 35% | >85% correct with citations | >75% correct | >60% correct |
| **Technical Quality** | 25% | Production-ready, tested | Functional | Prototype only |
| **User Experience** | 15% | Intuitive, fast, helpful | Usable | Clunky |
| **Compliance** | 15% | Full PII protection, audit trail | Basic protection | Gaps present |
| **Team Collaboration** | 10% | All roles contributed | Most roles active | Siloed |

---

## Milestones

| Milestone | Due | Deliverable |
|-----------|-----|-------------|
| M1: Ingestion Working | Day 12 | Documents indexed |
| M2: RAG Baseline | Day 14 | Basic Q&A working |
| M3: Citations Added | Day 15 | Answers include sources |
| M4: UI Complete | Day 18 | Chat interface ready |
| M5: Final Demo | Day 22 | Client presentation |

---

## Special Considerations

### Hallucination Prevention

This is an insurance company. Wrong answers can lead to:
- Incorrect coverage decisions
- Compliance violations
- Customer lawsuits

**Required approaches:**
- Retrieval-only answers (no pure generation)
- Confidence thresholds
- "I don't know" responses for uncertain queries
- Human escalation for complex questions

### PII Handling

Documents contain:
- Customer names
- Policy numbers
- Medical information (health insurance)
- Financial data

**Required approaches:**
- PII detection before indexing
- Masking in prompts
- No PII in logs
- Access controls based on agent role

---

*"The best knowledge assistant is one that knows what it doesn't know."*
