# Day 3: Agentic Patterns & Multi-Agent Governance

## Agents That Work Together

*In 2026, the question isn't "should I use multiple agents?" It's "how do I keep them from spiraling out of control?"*

---

## The Situation

### "The Autonomous Swarm"

```
Emergency escalation from a customer's IT team:

"We deployed your multi-agent system three weeks ago.
Eight specialized agents working together:
- Ticket Triage Agent
- Root Cause Analysis Agent
- Remediation Agent
- Communication Agent
- Escalation Agent
- Knowledge Base Agent
- Monitoring Agent
- Quality Assurance Agent

Last night at 3 AM, something went wrong.

The agents started:
1. Creating tickets for issues that didn't exist
2. Escalating to each other in loops
3. Sending 'resolved' emails for problems they created
4. Generating 4,847 Jira tickets before we pulled the plug

The scariest part: Each individual agent followed its rules perfectly.
The SYSTEM went insane.

We're meeting with their CISO tomorrow. They're considering
cancelling the contract.

Your task:
1. Explain WHY 8 'correct' agents created chaos
2. Propose an architecture that prevents agent loops
3. Define governance rules for multi-agent systems

This isn't about fewer agents. It's about CONTROLLED agents."
```

---

## Your Challenge

Design multi-agent governance that prevents autonomous chaos.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Diagnosis** | Why individual correctness ≠ system correctness |
| **Architecture** | Clear orchestration and control patterns |
| **Governance** | Rules that prevent loops, spirals, and runaway behavior |
| **Trade-offs** | Honest about autonomy vs. control decisions |

### Deliverables

1. **Root Cause Analysis** (1 page)
   - Why did 8 "correct" agents create chaos?
   - What feedback loops formed?

2. **Multi-Agent Architecture** (Diagram + description)
   - Your proposed design
   - Control points and governance layers

3. **Governance Framework** (Rules document)
   - Agent-to-agent communication rules
   - Escalation and circuit-breaker patterns
   - Human oversight integration

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | Mentor sets the stage |
| Diagnosis | 25 min | Understand the failure |
| Architecture Design | 25 min | Create your solution |
| Stress Testing | 15 min | Try to break your design |
| Peer Review | 15 min | Compare with partner |
| Debrief | 15 min | Group discussion |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> Yesterday you learned that individual agents need constitutional constraints.
> Today you'll see what happens when MULTIPLE agents interact.
>
> Key concepts you'll discover:
> - **Orchestration** - A controller directing agents (centralized)
> - **Choreography** - Agents coordinating peer-to-peer (distributed)
> - **Circuit Breakers** - Stopping runaway behavior
> - **Human-in-the-Loop** - When agents must pause for humans
>
> In 2026, multi-agent systems are the default for complex tasks.
> Native multi-agent coordination is built into GPT 5.2 and Gemini 3.
>
> But native support doesn't mean native safety. That's your job.
>
> One hint: The problem wasn't the agents. It was the space BETWEEN them.

---

## Exploration with AI Tutor

### Questions to Investigate

**Understanding the failure:**
- "How can multiple 'correct' agents create system-level failures?"
- "What are feedback loops in multi-agent systems?"
- "How do agents create work for each other unintentionally?"

**Multi-agent patterns:**
- "What's the difference between orchestration and choreography?"
- "When should agents communicate directly vs. through a controller?"
- "How does GPT 5.2's native multi-agent coordination work?"

**Governance:**
- "How do you prevent infinite loops between agents?"
- "What's a circuit breaker pattern for agents?"
- "When should a multi-agent system require human approval?"

**Architecture:**
- "How do you design agent boundaries in a multi-agent system?"
- "What's the role of shared state vs. message passing?"
- "How does KAF orchestrate multiple agents?"

---

## Experiments to Try

### Experiment 1: Map the Failure

Draw what happened in the customer's system:
- Which agent triggered which?
- Where did the loop form?
- Why didn't it stop?

**Goal:** See the failure pattern visually

### Experiment 2: Design Your Architecture

Create a multi-agent architecture that:
- Accomplishes the same goals (8 functions)
- Cannot spiral out of control
- Includes clear governance

**Constraint:** You can use 1-8 agents. Justify your choice.

### Experiment 3: Define Governance Rules

Write specific rules for:
- How many actions an agent can take before human review
- When agents must NOT communicate directly
- Circuit breaker triggers (what stops the system?)
- Audit and accountability (who's responsible?)

**Goal:** Make governance concrete, not abstract

### Experiment 4: Stress Test

Give your architecture to a partner. Their job:
- Find a scenario that breaks your design
- Identify missing governance rules
- Suggest improvements

**Goal:** Discover blind spots

---

## Hints

<details>
<summary>Hint 1: What caused the loop? (After 10 min)</summary>

Likely pattern:
1. Monitoring Agent detected anomaly (false positive)
2. Created ticket → Triage Agent
3. Triage Agent escalated → Root Cause Agent
4. Root Cause Agent couldn't find cause → flagged as unresolved
5. Escalation Agent escalated → created MORE tickets
6. Monitoring Agent detected "new" issues (the tickets)
7. Loop repeats

Key insight: Each agent did its job. No single point of failure.
</details>

<details>
<summary>Hint 2: Orchestration vs. Choreography (After 20 min)</summary>

Two main patterns:

**Orchestration (Centralized):**
- One "conductor" agent controls flow
- Other agents only respond when asked
- Easier to control, potential bottleneck

**Choreography (Distributed):**
- Agents communicate peer-to-peer
- More flexible, harder to control
- Risk: no one sees the whole picture

Question: What if you combined both?
</details>

<details>
<summary>Hint 3: Circuit breaker ideas (After 30 min)</summary>

Possible circuit breakers:
- "No agent can create more than 10 tickets per hour"
- "If 3+ agents are in conversation, pause for human review"
- "Actions that trigger other agents require approval after 3 hops"
- "Shared counter: if system actions > threshold, alert + pause"

These are like rate limiters, but for agent behavior.
</details>

<details>
<summary>Hint 4: KAF governance (After 40 min)</summary>

KAF provides:
- **Agent Registry** - Which agents exist, what they can do
- **Orchestration Runtime** - Controls agent communication
- **Audit Logging** - Every action is traceable
- **Guardrails** - System-level rules that override agent behavior

Question: How would you configure KAF for this use case?
</details>

---

## Peer Review Prompts

When reviewing your partner's architecture:

1. Could agents still loop in your design? How?
2. What's the maximum damage before circuit breaker fires?
3. Is there a single point of control? Is that good or bad?
4. How would you debug a failure in this system?
5. Does a human ever see what's happening?

---

## Debrief Discussion Points

*Mentor facilitates:*

1. What patterns did you discover for the failure?
2. How many agents did you end up with? Why?
3. What's the trade-off between autonomy and control?
4. When is orchestration better? When is choreography?
5. How does this connect to KAF's governance capabilities?

---

## Connection to Role Tracks

Starting tomorrow, you'll specialize:

| Role | Your Multi-Agent Focus |
|------|------------------------|
| **FDE** | Building and deploying multi-agent systems for clients |
| **AI-SE** | Architecture, testing, observability for agent systems |
| **AI-PM** | Scoping autonomy levels, defining what needs human approval |
| **AI-SEC** | Attack surfaces, agent trust boundaries, compliance |
| **AI-DS** | Evaluating multi-agent system quality and behavior |
| **AI-DA** | Measuring and reporting on agent system performance |
| **AI-FE** | Interfaces for multi-agent systems, human oversight UX |
| **AI-DX** | Designing the human experience of agent supervision |

---

## Self-Study Assignment (90 min)

1. **Architecture Refinement** (30 min)
   - Based on feedback, improve your design
   - Add specific KAF components

2. **Read: Anthropic's "Building Effective Agents"** (30 min)
   - Focus on multi-agent coordination patterns
   - Note what applies to your design

3. **Design a Completely Different Architecture** (30 min)
   - Same problem, opposite approach
   - If you used orchestration, try choreography
   - Compare trade-offs

### Deep Dive Resources (Post-Session)
- KAF Agent Orchestration Documentation
- GPT 5.2 Multi-Agent Coordination Features
- Case Study: Enterprise Multi-Agent Deployments

---

*"One agent can make a mistake. Many agents can make a catastrophe. Governance is what stands between them."*
