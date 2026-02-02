# Day 4: Role Expo - The T-Shape Foundation

## See the Full Picture Before You Specialize

*Before you dive deep into one role, see how all 8 roles work together to deliver AI solutions.*

---

## The Situation

### "The Complete Picture"

```
Message from Academy Leadership:

"Tomorrow, you'll choose your specialization. But first, you need
to understand what everyone else does.

In real projects, AI solutions fail when roles don't understand
each other. The PM scopes something impossible. The engineer builds
something no one can use. The security consultant blocks progress.
The designer solves the wrong problem.

Today, you'll experience ALL 8 roles on ONE use case.

By the end of today, you should be able to:
1. Explain what each role does in 30 seconds
2. Understand how roles hand off to each other
3. Make an informed decision about YOUR specialization

This is your T-shape horizontal bar.
Tomorrow, you go vertical."
```

---

## Your Challenge

Experience all 8 AI delivery roles through rapid-fire mini-challenges.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Breadth** | Can describe all 8 roles clearly |
| **Handoffs** | Understand what each role gives/receives |
| **Self-Awareness** | Know which role fits YOUR strengths |
| **Collaboration** | See how roles depend on each other |

### Deliverable

**Role Reflection Document** (due before Day 5):
1. Rank your top 3 role preferences
2. For each: Why does this role fit you?
3. One thing you learned about a role you WON'T choose
4. How your #1 choice collaborates with other roles

---

## Time Box: The Role Expo

| Time | Role | Mini-Challenge | Duration |
|------|------|----------------|----------|
| 0:00-0:05 | Intro | Context setting | 5 min |
| 0:05-0:15 | **AI-PM** | "Scope this in 3 bullets" | 10 min |
| 0:15-0:25 | **FDE** | "What's your first demo question?" | 10 min |
| 0:25-0:35 | **AI-SE** | "What could break at 3 AM?" | 10 min |
| 0:35-0:45 | **AI-DA** | "What KPI proves success?" | 10 min |
| 0:45-0:55 | **AI-DS** | "How would you test this?" | 10 min |
| 0:55-1:05 | **AI-SEC** | "Name 3 attack vectors" | 10 min |
| 1:05-1:15 | **AI-FE** | "Sketch the user flow" | 10 min |
| 1:15-1:25 | **AI-DX** | "What's the user's frustration?" | 10 min |
| 1:25-1:30 | Reflection | Role selection guidance | 5 min |

---

## The Use Case: Bank Document AI

```
CUSTOMER: Regional Bank (CEE)
SIZE: 2,000 employees, 50 branches
PROBLEM: Employees spend 3 hours/day searching internal documents

REQUEST:
"We want an AI assistant that helps our employees find information
in our internal documents - policies, procedures, product guides.

Budget: €150,000 for POC
Timeline: 3 months
Constraint: No customer data, only internal docs
Risk: Compliance team is skeptical about AI"
```

This single use case will be viewed through all 8 role lenses.

---

## Role Deep Dives

### AI-PM: Product Manager (0:05-0:15)

**Role Summary:**
> "I decide WHAT we build and WHY it matters to the customer."

**What AI-PM Does:**
- Scopes use cases and defines MVP
- Prioritizes features based on business value
- Manages stakeholder expectations
- Defines success metrics

**What AI-PM Hands Off:**
| To | They Receive |
|----|--------------|
| FDE | Clear scope, success criteria |
| AI-SE | Requirements, priority order |
| AI-SEC | Risk assessment scope |

**Mini-Challenge (5 min):**
Write 3 bullets that scope this project for the customer.
- What's IN scope?
- What's OUT of scope?
- What does success look like?

**AI Tutor Prompt:**
> "I'm scoping an AI document assistant for a bank. Help me think about what should be in the MVP vs. future phases."

---

### FDE: Forward Deployed Engineer (0:15-0:25)

**Role Summary:**
> "I build working demos fast and make them production-ready."

**What FDE Does:**
- Builds POCs and demos rapidly (24-48h)
- Deploys solutions to production
- Troubleshoots client environments
- Bridges technical and business stakeholders

**What FDE Hands Off:**
| To | They Receive |
|----|--------------|
| AI-SE | Demo code for productionization |
| AI-DA | Data requirements |
| AI-SEC | Architecture for security review |

**Mini-Challenge (5 min):**
What's the FIRST question you'd ask the customer before building anything?

**AI Tutor Prompt:**
> "A bank wants a document AI assistant. What technical questions should I ask before I start building a demo?"

---

### AI-SE: Software Engineer (0:25-0:35)

**Role Summary:**
> "I make AI systems reliable, scalable, and maintainable."

**What AI-SE Does:**
- Designs production architecture
- Implements CI/CD for AI systems
- Manages model versioning and rollback
- Ensures observability and monitoring

**What AI-SE Hands Off:**
| To | They Receive |
|----|--------------|
| FDE | Production-ready infrastructure |
| AI-SEC | Security-hardened code |
| AI-DA | Performance metrics |

**Mini-Challenge (5 min):**
List 3 things that could break at 3 AM with this system. How would you know?

**AI Tutor Prompt:**
> "What are the biggest reliability risks for an enterprise RAG system? How do I design for them?"

---

### AI-DA: Data & Analytics (0:35-0:45)

**Role Summary:**
> "I turn AI outputs into business insights and prove ROI."

**What AI-DA Does:**
- Designs KPIs and dashboards
- Measures AI system performance
- Creates executive reports
- Tells the value story with data

**What AI-DA Hands Off:**
| To | They Receive |
|----|--------------|
| AI-PM | Success metrics, ROI proof |
| FDE | Dashboard requirements |
| Executives | Business impact reports |

**Mini-Challenge (5 min):**
What single KPI would prove this project is successful? How would you measure it?

**AI Tutor Prompt:**
> "How do I measure the success of an AI document assistant? What metrics matter to a bank CFO?"

---

### AI-DS: Data Scientist (0:45-0:55)

**Role Summary:**
> "I ensure AI quality through rigorous testing and evaluation."

**What AI-DS Does:**
- Designs evaluation frameworks
- Runs experiments and A/B tests
- Validates model performance
- Identifies and fixes quality issues

**What AI-DS Hands Off:**
| To | They Receive |
|----|--------------|
| FDE | Quality benchmarks |
| AI-SE | Model evaluation pipelines |
| AI-PM | Quality reports |

**Mini-Challenge (5 min):**
How would you test if this document assistant actually gives correct answers?

**AI Tutor Prompt:**
> "How do I evaluate a RAG system for accuracy? What test cases should I create for a bank document assistant?"

---

### AI-SEC: Security Consultant (0:55-1:05)

**Role Summary:**
> "I find vulnerabilities before attackers do."

**What AI-SEC Does:**
- Threat modeling for AI systems
- Red teaming and penetration testing
- Compliance assessment (EU AI Act)
- Guardrails and safety design

**What AI-SEC Hands Off:**
| To | They Receive |
|----|--------------|
| AI-SE | Security requirements |
| AI-PM | Risk assessment |
| Compliance | Audit documentation |

**Mini-Challenge (5 min):**
Name 3 ways an attacker could abuse this document assistant.

**AI Tutor Prompt:**
> "What are the OWASP top 10 risks for an enterprise RAG system? How would I attack a bank's AI document assistant?"

---

### AI-FE: Front-End Engineer (1:05-1:15)

**Role Summary:**
> "I build AI interfaces that users actually want to use."

**What AI-FE Does:**
- Designs AI-native user interfaces
- Implements streaming responses
- Handles conversation state
- Ensures accessibility

**What AI-FE Hands Off:**
| To | They Receive |
|----|--------------|
| FDE | UI components |
| AI-DX | Implementation of designs |
| AI-DA | User interaction data |

**Mini-Challenge (5 min):**
Sketch (or describe) the main user flow for this document assistant.

**AI Tutor Prompt:**
> "What makes a good UI for an AI assistant? How should I design the conversation interface for bank employees?"

---

### AI-DX: Design & UX (1:15-1:25)

**Role Summary:**
> "I ensure AI solves real human problems, not imaginary ones."

**What AI-DX Does:**
- User research and journey mapping
- Prototyping and usability testing
- Human-AI interaction design
- Accessibility and inclusion

**What AI-DX Hands Off:**
| To | They Receive |
|----|--------------|
| AI-FE | Design specifications |
| AI-PM | User insights |
| FDE | UX requirements |

**Mini-Challenge (5 min):**
What's the bank employee's biggest frustration with finding documents today?

**AI Tutor Prompt:**
> "How do I research user needs for an AI assistant? What questions should I ask bank employees about their document search pain points?"

---

## Role Collaboration Map

```
                    ┌─────────────┐
                    │    AI-PM    │
                    │   (WHAT)    │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │   AI-DX    │ │    FDE      │ │   AI-SEC    │
    │   (WHO)    │ │   (HOW)     │ │   (SAFE)    │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           ▼               │               │
    ┌─────────────┐        │        ┌──────┴──────┐
    │   AI-FE    │        │        │   AI-SE     │
    │   (LOOK)   │        │        │  (SCALE)    │
    └─────────────┘        │        └─────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐
    │   AI-DS    │ │   AI-DA     │
    │  (QUALITY) │ │   (VALUE)   │
    └─────────────┘ └─────────────┘
```

---

## Reflection: Choosing Your Path

### Questions to Consider

1. **What energizes you?**
   - Talking to customers? → AI-PM, FDE
   - Building things? → FDE, AI-SE, AI-FE
   - Finding problems? → AI-SEC, AI-DS
   - Understanding users? → AI-DX, AI-DA
   - Proving value? → AI-DA, AI-PM

2. **What are you already good at?**
   - Your existing skills transfer to certain roles

3. **What do you want to learn?**
   - The academy is for growth, not comfort

4. **What does the team need?**
   - Consider gaps in your cohort

### Role Selection Process

1. **Today:** Complete Role Reflection Document
2. **Tonight:** Submit top 3 preferences via Dashboard
3. **Tomorrow (Day 5):** Assignments announced, role tracks begin

---

## Self-Study Assignment (90 min)

### Part 1: Role Reflection (30 min)

Complete and submit your Role Reflection Document:
- Top 3 role preferences with justification
- What you learned about a role you won't choose
- How your #1 choice collaborates with others

### Part 2: Explore Your Top Choice (30 min)

- Read the SYLLABUS.md for your top role
- Look at the Week 2 situations
- Identify what excites you and what concerns you

### Part 3: Cross-Role Understanding (30 min)

- Pick a role you'd NEVER choose
- Ask AI Tutor: "What does a great [ROLE] do that others don't?"
- Write 3 things you learned that surprised you

---

## Connection to Tomorrow

Tomorrow you begin your specialization:
- You'll meet your role-specific AI Tutor
- First situation: "The Real Work Begins"
- You'll start building role-specific skills

The horizontal bar of your T is complete.
Now we go deep.

---

*"Specialists who don't understand other specialties build solutions no one can use. Today you became dangerous - you see the whole picture."*
