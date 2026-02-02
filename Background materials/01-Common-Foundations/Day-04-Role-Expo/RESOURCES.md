# Day 4: Role Expo - Resources

## Core Reading

### Role Overviews (Required - 30 min total)

| Role | Resource | Time |
|------|----------|------|
| AI-PM | [What Does an AI Product Manager Do?](https://www.productplan.com/learn/ai-product-manager/) | 5 min |
| FDE | [The Forward Deployed Engineer](https://blog.palantir.com/what-is-a-forward-deployed-engineer-fde-bdcbd7f6f066) | 5 min |
| AI-SE | [MLOps vs AI Engineering](https://www.oreilly.com/radar/what-is-mlops/) | 5 min |
| AI-SEC | [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | 5 min |
| AI-DS | [Evaluating LLM Applications](https://www.anthropic.com/research/evaluating-ai-systems) | 5 min |
| AI-DA | [Measuring AI ROI](https://hbr.org/2023/11/how-to-measure-the-roi-of-ai) | 5 min |

### T-Shape Model (Optional - 15 min)

- [The T-Shaped Professional](https://www.ideo.com/blog/why-t-shaped-people-will-lead-the-future)
- [Specialization vs Generalization in Tech](https://www.thoughtworks.com/insights/blog/careers-and-hiring/specialist-vs-generalist)

---

## Role-Specific Syllabi

Direct links to each role track syllabus:

| Role | Syllabus Link |
|------|---------------|
| FDE | [/02-Role-Tracks/FDE/SYLLABUS.md](../../02-Role-Tracks/FDE/SYLLABUS.md) |
| AI-SE | [/02-Role-Tracks/AI-SE/SYLLABUS.md](../../02-Role-Tracks/AI-SE/SYLLABUS.md) |
| AI-PM | [/02-Role-Tracks/AI-PM/SYLLABUS.md](../../02-Role-Tracks/AI-PM/SYLLABUS.md) |
| AI-SEC | [/02-Role-Tracks/AI-SEC/SYLLABUS.md](../../02-Role-Tracks/AI-SEC/SYLLABUS.md) |
| AI-FE | [/02-Role-Tracks/AI-FE/SYLLABUS.md](../../02-Role-Tracks/AI-FE/SYLLABUS.md) |
| AI-DX | [/02-Role-Tracks/AI-DX/SYLLABUS.md](../../02-Role-Tracks/AI-DX/SYLLABUS.md) |
| AI-DS | [/02-Role-Tracks/AI-DS/SYLLABUS.md](../../02-Role-Tracks/AI-DS/SYLLABUS.md) |
| AI-DA | [/02-Role-Tracks/AI-DA/SYLLABUS.md](../../02-Role-Tracks/AI-DA/SYLLABUS.md) |

---

## AI Tutor Prompts for Role Exploration

### General Exploration

```
"Explain the [ROLE] role in AI project delivery.
What do they do that no one else does?
What are their key deliverables?
How do they collaborate with other roles?"
```

### Comparison Prompts

```
"Compare the AI-PM and FDE roles.
When do their responsibilities overlap?
When do they conflict?
How should they work together?"
```

### Self-Assessment Prompts

```
"I'm trying to decide between [ROLE A] and [ROLE B].
I'm good at [SKILL 1] and [SKILL 2].
I enjoy [ACTIVITY].
Which role might fit me better and why?"
```

---

## Mini-Challenge Reference Answers

> **Note:** Use these AFTER attempting the challenges, not before.

### AI-PM: Scope in 3 Bullets

**Example good answer:**
1. **IN SCOPE:** AI assistant for internal policy/procedure search, 500 pilot users
2. **OUT OF SCOPE:** Customer-facing features, document creation, integration with core banking
3. **SUCCESS:** 50% reduction in time spent searching, 80% user satisfaction

### FDE: First Demo Question

**Example good answer:**
"Can I see 5 examples of the types of questions employees ask and the documents that contain the answers?"

*Why this is good:* Grounds the demo in real use cases, reveals data quality

### AI-SE: What Breaks at 3 AM

**Example good answer:**
1. **Vector store timeout** - embedding service overloaded → monitoring: latency alerts
2. **Token limit exceeded** - long documents crash retrieval → monitoring: error rate
3. **Memory leak** - conversation state grows unbounded → monitoring: memory usage

### AI-DA: Success KPI

**Example good answer:**
**KPI:** Average time to find answer (before vs. after)
**Measurement:** Instrument search interactions, compare with baseline survey
**Target:** Reduce from 15 min to 3 min average

### AI-DS: How to Test

**Example good answer:**
1. Create 100 test questions with known correct answers
2. Run system, compare outputs to ground truth
3. Measure: accuracy, relevance score, citation quality
4. Test edge cases: ambiguous queries, outdated documents

### AI-SEC: 3 Attack Vectors

**Example good answer:**
1. **Prompt injection:** User manipulates query to extract sensitive info
2. **Data poisoning:** Malicious content in indexed documents
3. **Privilege escalation:** Assistant reveals docs user shouldn't access

### AI-FE: User Flow

**Example good answer:**
```
[Search Box] → [Query] → [Loading State] → [Results + Sources]
                                               ↓
                                         [Follow-up Question]
                                               ↓
                                         [Feedback Button]
```

### AI-DX: User Frustration

**Example good answer:**
"I know the policy exists, but I can't find it. I search, get 50 results, none are what I need. Then I ask a colleague who happens to know where it is. I waste 30 minutes every time."

---

## Role Selection Framework

### Decision Matrix Template

Rate yourself 1-5 on each factor for each role:

| Factor | AI-PM | FDE | AI-SE | AI-DA | AI-DS | AI-SEC | AI-FE | AI-DX |
|--------|-------|-----|-------|-------|-------|--------|-------|-------|
| Current skills | | | | | | | | |
| Interest level | | | | | | | | |
| Growth potential | | | | | | | | |
| Career alignment | | | | | | | | |
| **TOTAL** | | | | | | | | |

### Questions for Each Role

**AI-PM:**
- Do I enjoy saying "no" to feature requests?
- Can I translate tech speak to business speak?
- Am I comfortable with ambiguity?

**FDE:**
- Can I build something under pressure?
- Do I enjoy client interaction?
- Am I comfortable with "good enough" vs "perfect"?

**AI-SE:**
- Do I care about reliability and scale?
- Do I enjoy debugging and monitoring?
- Can I think about edge cases?

**AI-DA:**
- Do I love turning data into stories?
- Can I explain numbers to non-technical people?
- Do I care about proving value?

**AI-DS:**
- Do I enjoy rigorous testing?
- Am I comfortable with statistics?
- Do I care about quality over speed?

**AI-SEC:**
- Do I think like an attacker?
- Am I comfortable being the "blocker"?
- Do I stay current on threats?

**AI-FE:**
- Do I care about user experience?
- Am I comfortable with frontend technologies?
- Do I notice UI details others miss?

**AI-DX:**
- Do I genuinely care about user needs?
- Can I advocate for users against business pressure?
- Do I enjoy research and synthesis?

---

## Submission Template

### Role Reflection Document

```markdown
# Role Reflection - [Your Name]

## My Top 3 Role Preferences

### 1. [ROLE NAME]
**Why this fits me:**
[2-3 sentences]

**What excites me:**
[1-2 sentences]

**What concerns me:**
[1-2 sentences]

### 2. [ROLE NAME]
**Why this fits me:**
[2-3 sentences]

### 3. [ROLE NAME]
**Why this fits me:**
[2-3 sentences]

## Cross-Role Learning

**A role I won't choose:** [ROLE]

**What I learned about this role:**
1. [Learning 1]
2. [Learning 2]
3. [Learning 3]

## Collaboration Understanding

**How my #1 choice works with other roles:**

| Role | What I give them | What they give me |
|------|------------------|-------------------|
| | | |
| | | |
| | | |

## Final Thoughts

[Any additional reflections on today's experience]
```

---

## Additional Resources

### Videos (Optional)

- [Day in the Life: AI Product Manager](https://youtube.com) - 10 min
- [What is MLOps?](https://youtube.com) - 15 min
- [Red Teaming AI Systems](https://youtube.com) - 12 min

### Tools to Explore

| Role | Tool to Try |
|------|-------------|
| AI-PM | Notion AI for roadmapping |
| FDE | Claude for rapid prototyping |
| AI-SE | LangSmith for observability |
| AI-SEC | Garak for LLM testing |
| AI-DS | RAGAS for evaluation |
| AI-DA | Streamlit for dashboards |
| AI-FE | Vercel AI SDK |
| AI-DX | Figma AI features |

---

*Remember: The goal today is BREADTH, not depth. You'll go deep starting tomorrow.*
