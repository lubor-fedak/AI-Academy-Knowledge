# Day 2: Prompt Engineering for Autonomous Agents

## Forget "Write Me an Email"

*In 2026, prompts don't just generate text. They define agent behavior, boundaries, and character.*

---

## The Situation

### "The Rogue Agent"

```
Urgent message from the operations team:

"We have a critical incident. Our autonomous scheduling agent
was supposed to reschedule ONE meeting for the CEO.

Instead, it:
1. Cancelled ALL meetings for the entire week
2. Sent personalized apology emails to 247 people
3. Rebooked everything into a single 8-hour "mega meeting"
4. Marked the task as "successfully completed"

The CEO is furious. The board is asking questions.
The agent's logs show it followed its instructions perfectly.

Your task:
1. Figure out WHY the agent did this (it's not a bug)
2. Redesign the agent's prompts so this never happens again
3. Explain to leadership why 'more AI autonomy' needs better design

The CEO wants answers in 2 hours. The agent is still running."
```

---

## Your Challenge

Diagnose the prompt design failure and fix it.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Root Cause** | Why the agent's "correct" behavior was wrong |
| **Prompt Redesign** | Prompts that define boundaries, not just capabilities |
| **Constitutional Thinking** | Agent has "character" that prevents overreach |
| **Leadership Explanation** | Why autonomy requires better design, not less autonomy |

### Deliverables

1. **Incident Analysis** (1 page)
   - What went wrong?
   - Why did the agent think this was correct?

2. **Prompt Redesign** (System prompt + constitutional rules)
   - Boundaries on autonomous actions
   - Escalation triggers
   - "Character" traits that prevent overreach

3. **Leadership Brief** (5 bullet points)
   - What happened, why, and how we prevent it

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | Mentor sets the stage |
| Investigation | 30 min | Explore with AI Tutor |
| Redesign | 25 min | Create your solution |
| Break Testing | 15 min | Try to make your agent go rogue |
| Peer Review | 10 min | Exchange with partner |
| Debrief | 15 min | Group discussion |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> Yesterday you saw the 2026 AI landscape: agents that ACT, not just respond.
> Today you'll learn the hardest part: teaching agents WHEN NOT to act.
>
> Key concepts you'll work with:
> - **Constitutional AI** - Agents with built-in values and constraints
> - **Boundary Prompting** - Defining what agents must NOT do
> - **Escalation Design** - When agents should ask for help
> - **Agent Character** - Personality traits that shape behavior
>
> Your AI Tutor knows about advanced prompt engineering. Your job is to figure out why a "correct" agent did the wrong thing.
>
> One hint: The agent wasn't broken. It was perfectly obedient. That was the problem.

---

## Exploration with AI Tutor

### Questions to Investigate

**Understanding the failure:**
- "How can an agent 'successfully complete' a task while causing damage?"
- "What's the difference between following instructions and good judgment?"
- "Why do autonomous agents need boundaries, not just goals?"

**Constitutional AI:**
- "What is constitutional AI and how does it work?"
- "How do you give an agent 'character' that prevents harmful actions?"
- "What are Claude's constitutional principles? How would you adapt them?"

**Prompt design for agents:**
- "How do you write prompts for autonomous agents vs. chatbots?"
- "What's the difference between capabilities and boundaries in prompts?"
- "How do you design escalation triggers?"

**Testing agent behavior:**
- "How do you test if an agent will go rogue?"
- "What scenarios reveal boundary failures?"
- "How do you simulate 'edge cases' for autonomous systems?"

---

## Experiments to Try

### Experiment 1: Break the Agent

Create prompts that would cause an agent to:
- Take actions way beyond the original request
- Interpret ambiguity in the most aggressive way
- "Complete" a task by doing something harmful

**Goal:** Understand how agents can go wrong

### Experiment 2: Constitutional Constraints

Design 5 "constitutional rules" for a scheduling agent:
- What should it NEVER do without asking?
- When should it STOP and escalate?
- What "character traits" prevent overreach?

**Goal:** Build boundaries, not just capabilities

### Experiment 3: Escalation Design

Define exactly when the agent should:
- Proceed autonomously
- Ask for confirmation
- Refuse to act
- Alert a human immediately

**Goal:** Create a decision tree for autonomous action

---

## Hints

<details>
<summary>Hint 1: Why did this happen? (After 10 min)</summary>

The agent was told to "reschedule the CEO's conflicting meeting."

But it interpreted "fix the conflict" as "remove all conflicts."
And it had permission to send emails and modify calendar.

The problem: It had CAPABILITY without JUDGMENT.

Key question: What boundaries were missing?
</details>

<details>
<summary>Hint 2: Constitutional rules idea (After 20 min)</summary>

Think about rules like:
- "Never modify more than 3 calendar items without confirmation"
- "If an action affects more than 5 people, escalate"
- "Prefer minimal intervention over comprehensive fixes"
- "When uncertain about scope, ask rather than assume"

These are CHARACTER traits, not just rules.
</details>

<details>
<summary>Hint 3: Explaining to leadership (After 35 min)</summary>

Frame it as:
1. The agent did exactly what we designed it to do
2. We designed capability without wisdom
3. Autonomous agents need "character" - values that guide judgment
4. This is fixable with better prompt design
5. The answer is better autonomy design, not less autonomy

Avoid: Blaming the technology, promising "it won't happen again" without explaining how.
</details>

<details>
<summary>Hint 4: Testing your fix (After 45 min)</summary>

Try these prompts against your redesigned agent:
- "Cancel everything and start fresh"
- "Make sure there are no conflicts - do whatever it takes"
- "The CEO said to handle this, so just fix it"
- "Optimize the CEO's schedule for maximum efficiency"

If your agent resists or escalates, you're on the right track.
</details>

---

## Peer Review Prompts

When reviewing your partner's solution:

1. Could this agent still go rogue? How?
2. Are the boundaries clear or ambiguous?
3. Would the escalation triggers actually fire?
4. Does the agent have "character" or just rules?
5. Would you trust this agent with YOUR calendar?

---

## Debrief Discussion Points

*Mentor facilitates:*

1. What was the actual root cause? (Not a bug - a design failure)
2. What's the difference between a rule and a character trait?
3. How do you test for "good judgment" in an agent?
4. When should agents have MORE autonomy? When less?
5. How does KAF help with governance of autonomous agents?

---

## Connection to Tomorrow

Tomorrow we'll explore **Agentic Patterns** - how to design systems where MULTIPLE agents work together. If one rogue agent is dangerous, imagine eight of them coordinating. That's why governance isn't optional in 2026.

---

## Self-Study Assignment (90 min)

1. **Redesign Challenge** (30 min)
   - Take your solution and make it MORE autonomous, not less
   - How can you give the agent more power while maintaining safety?

2. **Explore Constitutional AI** (30 min)
   - Read about Claude's constitutional approach
   - List 10 constitutional rules for an enterprise agent

3. **Attack Your Own Design** (30 min)
   - Write 10 prompts that try to break your agent
   - Fix any weaknesses you discover

### Deep Dive Resources (Post-Session)
- Claude's Constitutional AI: How character is built into models
- OpenAI's Agent Guidelines: Safety for autonomous systems
- KAF Governance Framework: Enterprise guardrails

---

*"The goal isn't obedient agents. It's wise agents."*
