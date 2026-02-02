# Day 9: Scale or Fail

## AI Architecture Specialization

*Your POC was too successful. Now you have 3 months to scale 200x.*

---

## The Situation

```
Slack message from Account Executive:

"🎉 HUGE WIN! The retail client LOVED the POC!

Quick recap:
- 50 pilot users in 2 stores
- AI assistant for inventory questions
- Response time: ~2 seconds
- User satisfaction: 94%

Here's the thing... they want to roll out to ALL stores.
- 10,000 employees
- 200 stores
- 20 countries
- 3 months

I know the POC was running on a single Azure instance.
I know there's no documentation.
I know you built it in 3 weeks.

But the deal is €2.4M ARR. We can't say no.

Can you put together a scale-up plan by tomorrow?
The CTO wants to see architecture + timeline + risks.

Please tell me this is possible. 🙏"

ATTACHMENT: poc-architecture.txt
```

**POC Architecture (current state):**
```
- 1x Azure Container App (4 vCPU, 16GB RAM)
- 1x Azure OpenAI endpoint (GPT-4o)
- 1x Azure AI Search index (5000 documents)
- 1x Cosmos DB (10GB, 400 RU/s)
- No load balancer
- No caching
- No monitoring (besides Azure defaults)
- Deployment: Manual via Azure Portal
- Secrets: In environment variables
- Logs: Azure default (7 days retention)
```

---

## Your Challenge

Design a scalable architecture that grows from 50 to 10,000 users across 20 countries.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Scalability** | Architecture handles 200x load increase |
| **Performance** | Response time < 3 seconds at scale |
| **Reliability** | 99.9% availability across regions |
| **Migration Path** | Clear transition from POC to production |
| **Risk Assessment** | Honest about challenges and timelines |

### Deliverables

1. **Scaled Architecture Design**
   - Multi-region deployment
   - Load balancing and auto-scaling
   - Caching strategy
   - Database scaling

2. **Migration Runbook**
   - Phase-by-phase transition
   - Rollback procedures
   - Data migration approach

3. **Performance Model**
   - Expected load calculations
   - Resource requirements
   - Cost projections

4. **Risk Assessment**
   - Top 5 scaling risks
   - Mitigation strategies
   - What could delay the timeline

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | Scaling fundamentals |
| Load Analysis | 15 min | Calculate actual requirements |
| Architecture Design | 35 min | Design scaled system |
| Migration Planning | 15 min | Plan the transition |
| Risk Assessment | 15 min | What will go wrong |
| Debrief | 15 min | Best practices |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> Scaling is not about adding more servers. It's about understanding
> where your system breaks and designing around those limits.
>
> Common scaling bottlenecks for AI systems:
> - **LLM API limits** - Token limits, rate limits, latency
> - **Vector database** - Query latency at scale
> - **Network** - Multi-region latency
> - **Cost** - LLM calls get expensive fast
>
> The 3-month timeline is aggressive but possible IF you:
> - Start with the hardest problems (multi-region, data residency)
> - Build scaling into the architecture, not as an afterthought
> - Automate everything from Day 1
>
> The POC worked because it was small. Production will expose every
> shortcut you took. Today you'll find those shortcuts before they
> find you.

---

## Load Analysis

### Current POC Metrics

| Metric | POC Value | Notes |
|--------|-----------|-------|
| Users | 50 | 2 stores |
| Queries/day | ~200 | ~4 per user |
| Avg response time | 2.1 seconds | Acceptable |
| Peak concurrent | ~10 | Small peaks |
| Index size | 5,000 docs | Single region |
| LLM calls/day | ~200 | GPT-4o |

### Scaled Requirements (Your Task: Calculate)

| Metric | Scaled Value | Calculation |
|--------|--------------|-------------|
| Users | 10,000 | Given |
| Queries/day | ? | Calculate based on POC |
| Peak concurrent | ? | Assume peak = 10% of users |
| Index size | ? | 200 stores × docs/store |
| LLM calls/day | ? | Based on queries |
| Regions | 20 | Given |

### Questions to Answer

1. What's the peak queries per second (QPS)?
2. How many LLM tokens per day?
3. What's the storage requirement?
4. What's the estimated monthly cost?

---

## Exploration with AI Tutor

### Questions to Investigate

**Load and capacity:**
- "How do I calculate peak QPS from daily query volume?"
- "What are Azure OpenAI rate limits and how do I work around them?"
- "How do I estimate LLM costs at scale?"

**Multi-region:**
- "How do I design multi-region AI applications on Azure?"
- "What are data residency requirements for retail in EU?"
- "How do I handle Azure AI Search across regions?"

**Performance:**
- "What caching strategies work for LLM applications?"
- "How do I reduce LLM latency at scale?"
- "When should I use streaming vs. batch responses?"

**Migration:**
- "How do I migrate from single instance to multi-region?"
- "What's the safest way to migrate a database with zero downtime?"
- "How do I do gradual rollout across 200 stores?"

---

## Hints

<details>
<summary>Hint 1: Load Calculations (After 10 min)</summary>

**Scaled load estimate:**
```
Users: 10,000
Queries/user/day: 4 (from POC)
Total queries/day: 40,000
Peak hour: 20% of daily = 8,000/hour = 133/minute = 2.2 QPS

Peak concurrent (10% rule): 1,000 users
Worst case burst: 100 QPS for 10 seconds

LLM tokens/day:
- Avg query: ~500 tokens (input + output)
- 40,000 queries × 500 = 20M tokens/day
- GPT-4o cost: ~$0.015 per 1K tokens
- Daily LLM cost: ~$300
- Monthly LLM cost: ~$9,000
```

This doesn't include caching - caching can reduce LLM calls by 40-60%.

</details>

<details>
<summary>Hint 2: Multi-Region Architecture (After 20 min)</summary>

**Regional deployment pattern:**

```
┌─────────────────────────────────────────────────────────┐
│                   GLOBAL LAYER                          │
├─────────────────────────────────────────────────────────┤
│  Azure Front Door (Global Load Balancer)                │
│  ├── Geo-routing to nearest region                     │
│  ├── Health checks & failover                          │
│  └── CDN for static content                            │
└─────────────────────────────────────────────────────────┘
              │                    │
              ▼                    ▼
┌─────────────────────┐  ┌─────────────────────┐
│   EUROPE REGION     │  │   ASIA REGION       │
├─────────────────────┤  ├─────────────────────┤
│ • Container Apps    │  │ • Container Apps    │
│ • AI Search replica │  │ • AI Search replica │
│ • Redis Cache       │  │ • Redis Cache       │
│ • Cosmos DB replica │  │ • Cosmos DB replica │
└─────────────────────┘  └─────────────────────┘
              │                    │
              └──────────┬─────────┘
                         ▼
            ┌─────────────────────┐
            │   GLOBAL SERVICES   │
            ├─────────────────────┤
            │ • Azure OpenAI      │
            │   (multi-region)    │
            │ • Cosmos DB (write) │
            │ • Key Vault         │
            │ • Monitor/Logs      │
            └─────────────────────┘
```

</details>

<details>
<summary>Hint 3: Caching Strategy (After 30 min)</summary>

**Multi-level caching:**

1. **Response cache (Redis)**
   - Cache common questions + answers
   - TTL: 1 hour
   - Expected hit rate: 40-50%
   - Reduces LLM calls and latency

2. **Embedding cache**
   - Cache query embeddings
   - Saves embedding API calls
   - TTL: 24 hours

3. **Search results cache**
   - Cache vector search results
   - TTL: 15 minutes (fresher data)
   - Reduces AI Search load

4. **Semantic cache (advanced)**
   - Match semantically similar questions
   - Use embedding similarity
   - Higher hit rate than exact match

**Cost impact:**
- Without caching: ~$9,000/month LLM
- With 50% cache hit: ~$4,500/month LLM
- Caching cost: ~$200/month Redis

</details>

<details>
<summary>Hint 4: Migration Phases (After 45 min)</summary>

**Phased rollout:**

**Phase 1 (Month 1): Foundation**
- Set up multi-region infrastructure
- Implement CI/CD pipeline
- Add monitoring and alerting
- Migrate to managed secrets
- Rollout: 0 additional stores (infra only)

**Phase 2 (Month 2): Regional Pilots**
- Deploy to 3 regions (EU, US, APAC)
- Add caching layer
- Add load testing
- Rollout: 20 stores (10%)

**Phase 3 (Month 3): Full Scale**
- Performance tuning based on Phase 2
- Gradual rollout: 20 stores/week
- Full monitoring and alerting
- Complete documentation

**Rollback triggers:**
- Response time > 5 seconds for > 5 minutes
- Error rate > 1%
- LLM costs > 150% of projection

</details>

---

## Peer Review Prompts

Try to break your partner's scale architecture:

1. What happens if Azure OpenAI has an outage?
2. A region's AI Search index gets corrupted. Impact?
3. Black Friday: 10x normal traffic for 2 hours. Does it survive?
4. New regulation requires data to stay in-country. How hard to adapt?
5. LLM costs are 3x your estimate. What's the backup plan?

---

## Connection to Tomorrow

Tomorrow: **KAF Implementation**. You'll take everything you've learned
about multi-agent systems, compliance, and scale, and implement it
using Kyndryl's Agentic Framework.

---

*"Anyone can build a demo. The gap between demo and production is where careers are made or broken."*
