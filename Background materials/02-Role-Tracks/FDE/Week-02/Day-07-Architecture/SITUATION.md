# Day 7: The Agent Swarm

## AI Architecture Specialization

*8 agents working together. What could possibly go wrong?*

---

## The Situation

```
Incident Report from Customer Operations:

SEVERITY: Critical
SYSTEM: Multi-Agent Logistics Platform
TIME: 03:47 AM - 04:52 AM (1 hour 5 minutes)
IMPACT: 10,247 erroneous customer notifications sent

TIMELINE:
03:47 - Monitoring Agent detected "unusual pattern" in delivery times
03:48 - Monitoring Agent created alert, routed to Analytics Agent
03:49 - Analytics Agent analyzed pattern, flagged as "potential delay"
03:50 - Analytics Agent notified Pricing Agent (price protection trigger)
03:50 - Pricing Agent recalculated 847 orders, flagged for customer notification
03:51 - Customer Communication Agent began sending "delay" notifications
03:52 - Alert Agent detected high notification volume
03:52 - Alert Agent created incident ticket
03:53 - Incident routed to... Analytics Agent (it's the "data expert")
03:54 - Analytics Agent analyzed notifications as "expected volume"
03:55 - Alert Agent escalated to Coordination Agent
03:56 - Coordination Agent requested status from all agents
03:57 - All agents reported "operating normally"
03:58 - Coordination Agent logged "false alarm" and closed incident
04:00 - Customer Communication Agent finished batch 1 (2,000 notifications)
04:01 - Customers started replying "What delay? My package arrived yesterday"
...
04:52 - Human operator noticed Twitter complaints, killed the system

ROOT CAUSE: The "unusual pattern" was daylight saving time adjustment.
Monitoring Agent compared timestamps incorrectly.

DAMAGE:
- 10,247 incorrect notifications
- 847 price adjustments (refund liability: ~€42,000)
- Customer trust impact (Twitter trending)
- 3 enterprise customers demanding explanation

Your task: You're the architect who designed this system.
Redesign it so this NEVER happens again.
```

---

## Your Challenge

Design a multi-agent architecture with governance that prevents autonomous chaos.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Root Cause Analysis** | Why 8 "correct" agents created chaos |
| **Architecture Redesign** | Clear orchestration with control points |
| **Governance Rules** | Specific rules that would have prevented this |
| **Human Oversight** | Clear escalation and intervention points |

### Deliverables

1. **Failure Analysis** (1 page)
   - What feedback loop formed?
   - Why did self-checking fail?
   - Where were the missing circuit breakers?

2. **Redesigned Architecture** (Diagram + specification)
   - Agent roles and boundaries
   - Communication protocols
   - Orchestration pattern (central vs. distributed)
   - Control and governance layers

3. **Governance Framework**
   - Agent-to-agent communication rules
   - Action limits and thresholds
   - Circuit breaker specifications
   - Human escalation triggers

4. **Monitoring & Alerting Design**
   - What to monitor
   - Alert thresholds
   - Who gets alerted when

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | Multi-agent failure patterns |
| Failure Analysis | 20 min | Understand what went wrong |
| Architecture Design | 30 min | Redesign the system |
| Governance Rules | 15 min | Define specific rules |
| Stress Testing | 15 min | Try to break your design |
| Debrief | 15 min | Best practices |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> In 2026, multi-agent systems are the default. GPT 5.2 and Gemini 3
> have native multi-agent coordination. Building them is easy.
>
> Controlling them is the hard part.
>
> The fundamental problem: Each agent can be 100% correct in isolation
> and still create system-level failures. This is called **emergent
> misbehavior** - the system does things no individual component intended.
>
> Key patterns you'll explore:
> - **Orchestration** - Central controller directs agents
> - **Choreography** - Agents coordinate peer-to-peer
> - **Hybrid** - Mix of both approaches
> - **Circuit Breakers** - Automatic stops when things go wrong
> - **Human-in-the-Loop** - When to involve humans
>
> The incident you're analyzing is real (names changed). It happened
> to a Fortune 500 company in 2025. Don't let it happen to your clients.

---

## Exploration with AI Tutor

### Questions to Investigate

**Understanding the failure:**
- "How do multi-agent systems create emergent misbehavior?"
- "What are feedback loops in agent systems and how do they form?"
- "Why did the agents think they were operating normally?"

**Architecture patterns:**
- "When should I use orchestration vs choreography for agents?"
- "How does GPT 5.2's native multi-agent coordination work?"
- "What's the role of a coordination agent vs. a human supervisor?"

**Governance:**
- "How do I implement circuit breakers for agent systems?"
- "What metrics indicate an agent system is spiraling?"
- "How do I design human escalation that actually works?"

---

## The Original Architecture (What Failed)

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORIGINAL ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│  │Monitoring│───▶│Analytics │───▶│ Pricing  │───▶│ Customer │ │
│  │  Agent   │    │  Agent   │    │  Agent   │    │  Comms   │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│       │              │                │               │        │
│       │              │                │               │        │
│       ▼              ▼                ▼               ▼        │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│  │  Alert   │◀───│Inventory │    │ Routing  │    │Knowledge │ │
│  │  Agent   │    │  Agent   │    │  Agent   │    │  Agent   │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│       │                                                        │
│       ▼                                                        │
│  ┌──────────────────┐                                          │
│  │ Coordination     │  (Can query all agents)                  │
│  │ Agent            │  (No authority to STOP anything)         │
│  └──────────────────┘                                          │
│                                                                 │
│  PROBLEMS:                                                      │
│  • No central control / kill switch                            │
│  • Agents can trigger each other indefinitely                  │
│  • "Coordination" Agent has no real authority                  │
│  • No rate limits on customer-facing actions                   │
│  • Human oversight is reactive, not proactive                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Hints

<details>
<summary>Hint 1: The Core Problem (After 10 min)</summary>

The system had **no single point of truth** about "is this normal?"

Each agent evaluated from its own perspective:
- Monitoring: "I detected something, my job is to alert"
- Analytics: "I see data, my job is to analyze"
- Pricing: "I got a trigger, my job is to adjust"
- Comms: "I have updates, my job is to notify"
- Alert: "I see volume, but Analytics says it's fine"
- Coordination: "Everyone says they're fine, must be fine"

**Missing:** A system-level view of "what's actually happening"

</details>

<details>
<summary>Hint 2: Orchestration vs Choreography (After 20 min)</summary>

**Orchestration approach:**
```
[Human Supervisor]
       │
       ▼
[Orchestrator Agent] ──────── "Single brain"
       │
       ├── Monitoring Agent (reports only)
       ├── Analytics Agent (analyzes on request)
       ├── Pricing Agent (proposes, doesn't execute)
       └── Customer Comms (executes only with approval)
```

**Hybrid approach:**
```
[Human Supervisor]
       │
       ▼
[Orchestrator] ─── High-stakes decisions
       │
       ├── [Ops Cluster] ─── Low-stakes, autonomous
       │     ├── Monitoring
       │     ├── Analytics
       │     └── Inventory
       │
       └── [Customer Cluster] ─── Requires approval
             ├── Pricing
             └── Communications
```

</details>

<details>
<summary>Hint 3: Concrete Governance Rules (After 35 min)</summary>

**Action limits:**
- "No agent can create > 10 tickets per hour without orchestrator approval"
- "Customer notifications > 100 require human approval"
- "Price changes > €1000 total require human approval"
- "Any action affecting > 50 customers requires approval"

**Circuit breakers:**
- "If any agent loops (same output 3x in 5 min) → pause + alert"
- "If customer complaints spike > 200% baseline → pause all customer comms"
- "If agent-to-agent traffic > 10x normal → pause + alert human"

**Escalation:**
- Level 1: Orchestrator handles autonomously
- Level 2: Orchestrator pauses system, alerts on-call
- Level 3: System stops, requires human restart

</details>

<details>
<summary>Hint 4: What Would Have Stopped This (After 45 min)</summary>

**Rules that would have prevented the incident:**

1. "Customer notification volume > 100/hour requires approval"
   - Would have stopped at 100 notifications

2. "Price adjustments > 50 orders require manual review"
   - Would have caught the 847 orders

3. "If Monitoring + Analytics + Action all happen in < 10 min, pause for review"
   - Would have caught the rapid cascade

4. "Human must approve any action based on 'anomaly detection'"
   - Would have caught the DST false positive

5. "Coordination Agent has kill-switch authority"
   - Would have stopped the system when queried

</details>

---

## Peer Review Prompts

Try to break your partner's design:

1. What if the orchestrator agent hallucinates?
2. What if the human supervisor is asleep at 3 AM?
3. What if two agents send conflicting signals simultaneously?
4. What if the circuit breaker itself malfunctions?
5. How do you test that governance actually works?

---

## Connection to Tomorrow

Tomorrow: **Compliance Architecture**. You'll design systems that meet
EU AI Act requirements for high-risk AI. Multi-agent governance isn't
just good practice - it's becoming law.

---

*"The scariest AI failures aren't from broken agents. They're from perfectly functioning agents doing exactly what they were designed to do."*
