# Day 3: Agentic Patterns - Mentor Notes

> **CONFIDENTIAL - For Mentors Only**

## Session Overview

| Item | Details |
|------|---------|
| **Duration** | 90 minutes |
| **Participants** | All 80 (combined session) |
| **Deliverable** | Architecture critique + Simplified proposal |
| **Key Learning** | Agent patterns, when multi-agent makes sense |

---

## What Students Should Discover

| Concept | Key Insight |
|---------|-------------|
| **Agent definition** | LLM + tools + goals, not just multiple LLM calls |
| **Tool vs Agent** | Simple functions don't need agents |
| **Complexity cost** | Each agent adds latency, cost, failure points |
| **When multi-agent** | Different reasoning styles, adversarial needs |
| **Simplicity wins** | One good agent usually beats many mediocre ones |

---

## Typical Misconceptions

| Misconception | Reality | How to Address |
|---------------|---------|----------------|
| "More agents = smarter" | More agents = more complexity | "What's the coordination overhead?" |
| "Each task needs an agent" | Most tasks need tools | "Does this need reasoning or just execution?" |
| "Agents are autonomous" | They need guardrails | "What if the agent decides wrong?" |
| "Multi-agent is always better" | Usually overkill | "What's the simplest thing that works?" |

---

## Sample Good Architecture Critique

```
CRITIQUE OF 12-AGENT SYSTEM:

1. OVERKILL:
- Query Understanding + Intent Classification → One LLM call
- Entity Extraction → Tool, not agent
- Sentiment Analysis → Tool, not agent

2. LATENCY:
- 12 sequential/parallel agents = 12x API calls
- User waits for all to complete
- Any failure breaks chain

3. COST:
- Each agent = separate LLM call
- 12x token costs per request
- Debugging 12 components vs 1

SIMPLIFIED PROPOSAL:
- 1 Main Agent with good system prompt
- 3-4 Tools (Search, Sentiment, Translation, API)
- Optional: Reviewer agent for critical domains only
```

---

## Debrief Points

1. What makes something an agent vs. a tool?
2. When would you actually need 12 agents?
3. How do you decide between single and multi-agent?
4. What role does your specialization play in agent design?
5. How will this week's learnings apply to your role track?

---

## Transition to Role Tracks

End the session with:

> "These three days gave you the foundation: LLMs, prompting, and agents. Starting tomorrow, you'll apply these concepts through the lens of your specific role. FDEs will build agents for clients, AI-SEs will architect and test them, AI-PMs will scope and prioritize them. Same concepts, different perspectives."
