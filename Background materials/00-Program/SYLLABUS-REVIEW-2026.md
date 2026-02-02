# Syllabus Review: 2026 AI Reality & Pedagogical Approach

## Executive Summary

This review analyzes the AI Academy syllabus from two perspectives:
1. **2026 AI Evolution** - What content is obsolete or needs updating?
2. **Pedagogical Approach** - What's "old school" (frontal teaching) vs. experimental learning?

---

## Part 1: 2026 AI Reality Check

### What's Changed Since 2024

| Aspect | 2024 Reality | 2026 Reality |
|--------|--------------|--------------|
| **Primary challenge** | Hallucinations, accuracy | Autonomy vs. control, agent coordination |
| **Architecture** | Single LLM calls, basic RAG | Multi-agent systems as default, agent-to-agent protocols |
| **Context windows** | 128K tokens (impressive) | 2M+ tokens (standard), unlimited for some models |
| **Agent coordination** | Custom orchestration (LangChain) | Native multi-agent in models (GPT 5.2, Gemini 3) |
| **Governance** | Optional add-on | Required by EU AI Act, built into platforms |
| **Human role** | Operator (writes prompts) | Architect & supervisor (designs systems) |

---

### Day-by-Day Obsolescence Analysis

#### Day 1: AI Landscape ✅ UPDATED
- Already reflects 2026 reality (Moltbook, ClawdBot, GPT 5.2, Claude 4.5)
- KAF integrated
- No changes needed

#### Day 2: Prompt Engineering ⚠️ NEEDS UPDATE

**Obsolete elements:**
| Current Content | Problem | 2026 Update |
|-----------------|---------|-------------|
| Focus on "hallucinations" as main issue | Grounding is now standard | Focus on agent behavior, constitutional AI |
| Basic system prompts | Too simple for agents | Multi-agent prompt coordination |
| "Testing for hallucinations" | Automated in 2026 | Testing for agent safety, autonomy boundaries |

**Missing for 2026:**
- Constitutional AI (Claude's "character")
- Agent persona design
- Memory and context management for agents
- Prompt chains for multi-agent coordination
- MCP (Model Context Protocol) awareness

**Recommended new situation:**
```
"The Rogue Agent"
Your agent was supposed to book a meeting. Instead, it cancelled
all meetings for the week and sent apology emails to 200 people.
The prompts look correct. Why did this happen?
```

#### Day 3: Agentic Patterns ⚠️ NEEDS UPDATE

**Obsolete elements:**
| Current Content | Problem | 2026 Update |
|-----------------|---------|-------------|
| ReAct pattern explanation | 2023 terminology, now built-in | Focus on when to use native vs. custom orchestration |
| "12 agents is overkill" premise | Multi-agent is normal in 2026 | "12 agents without governance is overkill" |
| Single agent + tools as "best" | Outdated advice | Depends on use case, multi-agent often better now |
| No mention of agent memory | Critical gap | Agent state, memory patterns, context handoff |

**Missing for 2026:**
- Native multi-agent coordination (GPT 5.2 features)
- Agent-to-agent communication protocols
- Autonomous vs. supervised agent patterns
- Human-in-the-loop design for autonomous systems
- KAF Agent Registry and orchestration patterns

**Recommended new situation:**
```
"The Autonomous Swarm"
Customer deployed 8 agents that work together autonomously.
At 3 AM, they started creating tickets, escalating to each other,
and generated 5,000 Jira issues before anyone noticed.
How do you design agent systems that don't spiral out of control?
```

---

### Role Track Updates Needed

#### FDE Track
| Current | Issue | Update |
|---------|-------|--------|
| "24-hour demo" focus | Still valid | Add: "24-hour demo WITH governance" |
| Azure AI Engineer cert | Check if 2026 version exists | Update cert names |
| RAG as main technique | RAG is baseline now | Add: Agent orchestration, KAF deployment |

#### AI-SE Track
| Current | Issue | Update |
|---------|-------|--------|
| "Model Drift Detected" | Automated in 2026 LLMOps | Change to: "Agent Behavior Drift" - more relevant |
| CI/CD for LLMs | Good but basic | Add: Agent versioning, rollback patterns |
| Testing non-determinism | Valid | Add: Testing agent autonomy boundaries |

#### AI-SEC Track
| Current | Issue | Update |
|---------|-------|--------|
| Prompt injection focus | Still relevant but expanded | Add: Agent action boundaries, autonomous system risks |
| "Red Team the Chatbot" | Too simple | Change to: "Red Team the Autonomous Agent Swarm" |
| Generic compliance | Vague | Specific EU AI Act requirements for 2026 |

#### AI-PM Track
| Current | Issue | Update |
|---------|-------|--------|
| Scope/ROI focus | Still valid | Add: Agent capability boundaries, autonomy levels |
| "Customer wants everything" | Good | Add: "Customer wants full automation" - autonomy scoping |

---

## Part 2: Pedagogical Approach Analysis

### Scoring System
- **Experiment**: Students discover through doing, AI Tutor guides
- **Frontal**: Instructor/content explains, students receive

### Day-by-Day Analysis

#### Day 1: AI Landscape
| Section | Current Approach | Score |
|---------|------------------|-------|
| Opening | Mentor delivers quote | Frontal (5 min - acceptable) |
| Part 1: The Shock | Students observe live systems | **Experiment** ✅ |
| Part 2: Live Demo | Mentor runs demo, students observe | Mixed (should they run it?) |
| Part 2.5: KAF | Content explains KAF | **Frontal** ⚠️ |
| Part 3: AI Tutor | Students interact with AI Tutor | **Experiment** ✅ |
| Part 4: Chaos vs Structure | Live experiment with groups | **Experiment** ✅ |
| Part 5: Assignment | Students create agent | **Experiment** ✅ |

**Day 1 Verdict:** 70% Experiment, 30% Frontal - GOOD

#### Day 2: Prompt Engineering
| Section | Current Approach | Score |
|---------|------------------|-------|
| Situation: "The Lying Bot" | Problem-based | **Experiment** ✅ |
| Micro-Context | Mentor explains concepts | Frontal (acceptable intro) |
| Technical Background | **Content explains why hallucinations happen** | **Frontal** ⚠️ |
| Fix Options table | **Content lists solutions** | **Frontal** ⚠️ |
| Sample System Prompt | **Gives away the answer** | **Frontal** ❌ |
| Hints in <details> | Progressive revelation | **Experiment** ✅ |
| Testing Your Solution | Students break their fix | **Experiment** ✅ |
| Peer Review | Students exchange | **Experiment** ✅ |

**Day 2 Verdict:** 55% Experiment, 45% Frontal - NEEDS IMPROVEMENT

**Problems:**
1. "Technical Background" section explains too much
2. "Fix Options" table gives away solutions
3. "Sample System Prompt" is literally the answer

#### Day 3: Agentic Patterns
| Section | Current Approach | Score |
|---------|------------------|-------|
| Situation: "Too Many Agents" | Problem-based | **Experiment** ✅ |
| Key Agent Patterns | **Content explains patterns with diagrams** | **Frontal** ❌ |
| Single Agent + Tools | **Content states "Usually Best"** | **Frontal** ❌ |
| Sample Simplified Architecture | **Gives away the solution** | **Frontal** ❌ |
| Hints in <details> | Progressive revelation | **Experiment** ✅ |
| Questions for AI Tutor | Guides exploration | **Experiment** ✅ |

**Day 3 Verdict:** 40% Experiment, 60% Frontal - NEEDS SIGNIFICANT REWORK

**Problems:**
1. "Key Agent Patterns" section is a lecture
2. Stating "Single Agent + Tools is Usually Best" removes discovery
3. Sample architecture gives the answer before students try

---

### Role Track Syllabi Analysis

| Track | Approach | Issues |
|-------|----------|--------|
| FDE | Situation-based, good | Some hints too explicit |
| AI-SE | Situation-based, good | "Model Drift" is explained, not discovered |
| AI-PM | Strong on business scenarios | Good balance |
| AI-SEC | Red teaming is experimental | Need more hands-on attack exercises |
| AI-FE | Not reviewed | - |
| AI-DX | Not reviewed | - |
| AI-DA | Not reviewed | - |
| AI-DS | Not reviewed | - |

---

## Part 3: Recommendations

### Immediate Fixes (High Impact)

#### 1. Day 2: Remove "answers" from main content

**Remove or hide:**
- "Technical Background" section → Move to MENTOR-NOTES.md
- "Fix Options" table → Make it a hint (Hint 4)
- "Sample System Prompt" → Remove entirely (or post-session resource)

**Replace with:**
- "What to investigate" prompts
- AI Tutor guided discovery
- Post-session "reference" document

#### 2. Day 3: Remove lecture content

**Remove or hide:**
- "Key Agent Patterns" diagrams → Students should draw these
- "Single Agent + Tools (Usually Best)" statement → Let them discover
- "Sample Simplified Architecture" → Remove (or Hint 5)

**Replace with:**
- Challenge: "Draw what you think is the simplest architecture"
- AI Tutor prompts for pattern discovery
- Peer comparison: "How does your architecture differ from your partner's?"

#### 3. Update all days for 2026 reality

- Add agent autonomy considerations
- Add governance as core requirement, not afterthought
- Update terminology (ReAct → native coordination)
- Add KAF references where relevant

### Content Structure Template (2026 + Experimental)

```markdown
# Day X: [Topic]

## The Situation (Problem-based)
[Real-world scenario with tension]

## Your Challenge
[Clear outcomes, no solutions]

## Time Box
[Activities with time allocation]

## Exploration with AI Tutor
[Questions to ask, not answers to find]

## Experiments to Try
[Hands-on activities that reveal concepts]

## Peer Exchange
[Compare discoveries with partner]

## Hints (Progressive)
<details>Hint 1 (after 10 min)</details>
<details>Hint 2 (after 20 min)</details>
<details>Hint 3 (after 30 min)</details>

## Self-Study
[Active tasks, not passive reading]

---
## POST-SESSION REFERENCE (separate document)
[Technical details, best practices, examples]
[Available AFTER the session, not during]
```

---

## Action Items

### Priority 1: Update for 2026 (This Week)
- [ ] Day 2: Update situation for agent behavior, not just hallucinations
- [ ] Day 3: Update for native multi-agent, add governance focus
- [ ] Add new situations reflecting autonomous agent challenges

### Priority 2: Remove Frontal Content (This Week)
- [ ] Day 2: Move Technical Background, Fix Options, Sample Prompt to post-session
- [ ] Day 3: Remove Key Agent Patterns lecture, Sample Architecture
- [ ] Create separate "Reference Documents" folder for post-session content

### Priority 3: Role Track Updates (Next Week)
- [ ] Update all situations for 2026 agent reality
- [ ] Review certifications for 2026 versions
- [ ] Add KAF references throughout

---

*Review Date: January 31, 2026*
*Status: Analysis Complete, Updates Pending*
