# Day 7: Agents Won't Cooperate

## FDE Track - Week 2, Day 7

---

## The Situation

### "The Left Hand Doesn't Know..."

```
GlobalBank wants to expand the system. Now it needs to:
1. Answer questions about policy documents (existing)
2. Look up customer account status (new)
3. Create support tickets (new)

You built a multi-agent system:
- DocumentAgent: Handles policy questions
- AccountAgent: Looks up customer data
- TicketAgent: Creates support tickets
- OrchestratorAgent: Routes requests

But it's chaos. The orchestrator sends document questions 
to AccountAgent. When users ask complex questions that 
need multiple agents, it freezes or gives partial answers.

"I asked about the refund policy for account #12345 
and it just told me the account balance. It didn't 
mention the refund policy at all!"

Demo is tomorrow. You need agents that actually cooperate.
```

---

## Your Challenge

Fix the multi-agent orchestration to handle complex queries.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Routing** | Questions go to the right agent |
| **Composition** | Multi-part queries get complete answers |
| **Fallback** | Graceful handling when agents fail |
| **Transparency** | User knows what's happening |

### Deliverables

1. **Fixed Orchestration** (working code)
   - Correct routing logic
   - Multi-agent composition for complex queries
   
2. **Agent Contracts** (1 page)
   - Clear capability definition for each agent
   - Input/output specifications
   
3. **Test Cases** (10 queries)
   - Single-agent scenarios
   - Multi-agent scenarios
   - Failure scenarios

---

## Micro-Context (5 minutes)

> Multi-agent systems fail when agents don't know their boundaries. Key patterns:
> - **Clear contracts** - Each agent has explicit capabilities
> - **Explicit routing** - Don't rely on LLM to figure out routing
> - **Sequential composition** - Break complex queries into steps
> - **Error boundaries** - One agent failing shouldn't crash everything
>
> Hint: Often a single well-prompted agent with tools beats multiple poorly-coordinated agents.

---

## Architecture Options

### Option A: Orchestrator Routes Everything
```
User → Orchestrator → [DocumentAgent | AccountAgent | TicketAgent]
                   ↓
             Combine results → User
```
**Pros:** Central control, easy to understand
**Cons:** Orchestrator becomes complex, single point of failure

### Option B: Single Agent with Tools
```
User → MainAgent → [doc_search() | account_lookup() | create_ticket()]
                ↓
              User
```
**Pros:** Simpler, LLM handles composition naturally
**Cons:** Harder to test individual capabilities

### Option C: Chain of Responsibility
```
User → DocumentAgent → "Can I handle this?"
                     ↓ No
       AccountAgent → "Can I handle this?"
                     ↓ Yes
                   Response
```
**Pros:** Each agent is independent
**Cons:** Doesn't handle multi-agent queries well

**Question:** Which pattern fits GlobalBank's needs best?

---

## Common Multi-Agent Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Wrong routing | Doc questions go to AccountAgent | Vague agent descriptions | Explicit capability lists |
| Partial answers | Only one part of query answered | No composition logic | Plan-then-execute |
| Deadlocks | System hangs | Circular dependencies | Clear hierarchy |
| Slow response | 30+ second latency | Sequential when parallel possible | Identify parallel steps |
| Inconsistent | Same query, different routing | Non-deterministic prompt | Structured routing logic |

---

## Routing Strategies

### Strategy 1: Keyword-Based (Simple)
```python
def route(query):
    if "account" in query.lower() or "balance" in query.lower():
        return "account_agent"
    elif "policy" in query.lower() or "document" in query.lower():
        return "document_agent"
    elif "ticket" in query.lower() or "issue" in query.lower():
        return "ticket_agent"
    else:
        return "document_agent"  # default
```
**Problem:** Misses nuance, fails on complex queries.

### Strategy 2: LLM-Based Classification
```python
def route(query):
    classification = llm.classify(
        query,
        categories=["document", "account", "ticket", "multiple"]
    )
    return classification
```
**Problem:** Non-deterministic, slow, expensive.

### Strategy 3: Intent Detection + Decomposition
```python
def route(query):
    intents = detect_intents(query)  # Returns list
    if len(intents) == 1:
        return agents[intents[0]]
    else:
        return compose_agents(intents)
```
**Best for:** Complex queries that need multiple agents.

---

## Hints

<details>
<summary>Hint 1: The GlobalBank query (Click after 10 min)</summary>

"Refund policy for account #12345" needs TWO things:
1. DocumentAgent: Look up refund policy
2. AccountAgent: Get account context (status, history)

Your orchestrator needs to:
1. Detect this is a multi-part query
2. Call both agents
3. Combine their responses coherently
</details>

<details>
<summary>Hint 2: Simplification (Click after 20 min)</summary>

Consider: Do you actually NEED multiple agents?

A single agent with these tools might be simpler:
- `search_documents(query)` → Returns relevant policy text
- `get_account(account_id)` → Returns account info
- `create_ticket(summary, priority)` → Creates ticket

The LLM can decide which tools to use and in what order.
</details>

<details>
<summary>Hint 3: Testing multi-agent (Click after 35 min)</summary>

Test categories you need:
1. **Single-agent:** "What's the refund policy?"
2. **Multi-agent:** "Refund policy for account #12345"
3. **Ambiguous:** "Help with my refund" (needs clarification)
4. **Failure:** "Transfer $1M to account X" (should refuse)
5. **Fallback:** What if DocumentAgent times out?
</details>

---

## Self-Study Assignment (90 min)

1. **Refactor architecture** - Choose and implement one of the patterns (45 min)
2. **Write agent contracts** - Define clear capabilities for each (15 min)
3. **Create test suite** - 15 queries covering all scenarios (30 min)

### Stretch Goals
- Implement parallel agent calls for multi-agent queries
- Add conversation memory across agent calls
- Build a routing evaluation dashboard
