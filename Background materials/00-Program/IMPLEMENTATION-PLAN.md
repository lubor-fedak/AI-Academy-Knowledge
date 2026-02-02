# AI Academy - Implementation Plan & Content Checklist

## Executive Summary

Complete overview of everything that needs to be prepared for AI Academy (February 2 - March 15, 2026).

**Timeline:** 80 participants, Forward Deployed Engineer capability with related specializations, 5 weeks (+ spring break February 16-22)

---

## 1. MATERIALS STRUCTURE (SharePoint)

```
📁 AI Academy 2026/
│
├── 📁 00-Program/
│   ├── 📄 README.md                      # Academy overview
│   ├── 📄 CALENDAR.md                    # Daily schedule
│   ├── 📄 ASSESSMENT-CRITERIA.md         # How we evaluate
│   ├── 📄 TOOLS-ACCESS.md                # Access and links
│   └── 📄 FAQ.md                         # Frequently asked questions
│
├── 📁 01-Common-Foundations/             # Days 1-3 (all together)
│   ├── 📁 Day-01-AI-Landscape/
│   │   ├── 📄 SITUATION.md
│   │   ├── 📄 RESOURCES.md
│   │   └── 📄 MENTOR-NOTES.md
│   ├── 📁 Day-02-Prompt-Engineering/
│   │   ├── 📄 SITUATION.md
│   │   ├── 📄 RESOURCES.md
│   │   └── 📄 MENTOR-NOTES.md
│   └── 📁 Day-03-Agentic-Patterns/
│       ├── 📄 SITUATION.md
│       ├── 📄 RESOURCES.md
│       └── 📄 MENTOR-NOTES.md
│
├── 📁 02-Role-Tracks/                    # Role-specific content
│   ├── 📁 FDE/
│   │   ├── 📄 SYLLABUS.md
│   │   ├── 📁 Week-02/
│   │   │   ├── 📁 Day-04/
│   │   │   ├── 📁 Day-05/
│   │   │   └── ...
│   │   ├── 📁 Week-04/
│   │   └── 📁 Week-05/
│   ├── 📁 AI-SE/
│   ├── 📁 AI-PM/
│   ├── 📁 AI-FE/
│   ├── 📁 AI-SEC/
│   ├── 📁 AI-DX/
│   ├── 📁 AI-DA/
│   └── 📁 AI-DS/
│
├── 📁 03-Labs/                           # Hands-on exercises
│   ├── 📁 Lab-01-First-Chatbot/
│   ├── 📁 Lab-02-RAG-Pipeline/
│   ├── 📁 Lab-03-Multi-Agent/
│   ├── 📁 Lab-04-Deployment/
│   └── 📁 Lab-05-Evaluation/
│
├── 📁 04-Team-Projects/                  # Week 4-5
│   ├── 📄 PROJECT-BRIEF-TEMPLATE.md
│   ├── 📄 TEAM-FORMATION.md
│   └── 📁 Teams/
│       ├── 📁 Team-Alpha/
│       └── ... (8 teams)
│
├── 📁 05-Hackathon/                      # March 15
│   ├── 📄 HACKATHON-RULES.md
│   ├── 📄 EVALUATION-CRITERIA.md
│   ├── 📄 CLIENT-BRIEF.md
│   └── 📄 PRESENTATION-TEMPLATE.pptx
│
├── 📁 06-Reference/                      # Always available
│   ├── 📁 KAF-Documentation/
│   ├── 📁 AI-Innovation-Lab-Method/
│   ├── 📄 PROMPT-LIBRARY.md
│   ├── 📄 TROUBLESHOOTING.md
│   └── 📄 GLOSSARY.md
│
├── 📁 07-Submissions/                    # Student submissions
│   ├── 📁 Weekly-Checkpoints/
│   │   ├── 📁 Week-01/
│   │   ├── 📁 Week-02/
│   │   ├── 📁 Week-04/
│   │   └── 📁 Week-05/
│   └── 📁 Final-Projects/
│
└── 📁 08-Mentor-Zone/                    # Mentors only
    ├── 📄 MENTOR-GUIDE.md
    ├── 📄 MENTOR-QUICK-REFERENCE.md
    ├── 📄 INTERVENTION-FRAMEWORK.md
    ├── 📄 ASSESSMENT-RUBRICS.md
    └── 📁 Solutions/                     # Solutions to situations
```

---

## 2. PROGRAM-LEVEL DOCUMENTS

### 2.1 README.md (Academy Overview)
**Content:**
- [ ] Vision and goals of the academy
- [ ] Timeline (5 weeks + break)
- [ ] 8 roles and their purpose
- [ ] Expectations from participants
- [ ] Daily format (90 min live + 90 min self-study)
- [ ] AI-Native learning philosophy
- [ ] Mentor and support contacts

### 2.2 CALENDAR.md (Master Schedule)
**Content:**

| Week | Dates | Content |
|------|-------|---------|
| Week 1 | Feb 2-8 | Common Foundations (Days 1-3) + Role Intro (Days 4-5) |
| Week 2 | Feb 9-15 | Role-Specific Deep Dive |
| BREAK | Feb 16-22 | Spring Break (self-paced assignments) |
| Week 4 | Feb 23 - Mar 1 | Team Projects - Build Phase |
| Week 5 | Mar 2-14 | Team Projects - Polish + Certification Prep |
| Hackathon | Mar 15 | Client Hackathon + Graduation |

**Daily detail:**
- [ ] For each day: topic, learning objectives, deliverables
- [ ] Session times (e.g., 9:00-10:30 live, self-study flexible)
- [ ] Checkpoint deadlines

### 2.3 ASSESSMENT-CRITERIA.md
**Content:**
- [ ] What we evaluate (quality of AI questions, artifacts, reflection)
- [ ] What we DON'T evaluate (memorization, speed)
- [ ] Weekly checkpoint structure
- [ ] Rubric for each checkpoint
- [ ] Final assessment criteria
- [ ] "Client-ready" definition

### 2.4 TOOLS-ACCESS.md
**Content:**
- [ ] ChatGPT Enterprise - link, login instructions
- [ ] Antigravity - workspace access
- [ ] Azure Portal - resource groups
- [ ] SharePoint - navigation guide
- [ ] Azure DevOps - repo access
- [ ] Troubleshooting common issues

---

## 3. COMMON FOUNDATIONS (DAYS 1-3)

### 3.1 Day 1: AI Landscape
**SITUATION.md:**
```
Challenge: "The CEO Asks"
Your CEO calls you: "I hear about AI agents everywhere. 
What is it exactly? What should we know? 
Prepare a 5-minute briefing for me by tomorrow."

Success Looks Like:
- Clear explanation of what LLM, agent, RAG are
- Distinction between hype vs. reality
- Concrete use cases for enterprise
- Limitations and risks

Time: 60 min exploration + AI Tutor
```

**RESOURCES.md:**
- [ ] Link to Anthropic Claude documentation
- [ ] Link to OpenAI documentation
- [ ] KAF Overview slides
- [ ] Recommended readings (3-4 articles)

**MENTOR-NOTES.md:**
- [ ] What students should discover
- [ ] Typical misconceptions
- [ ] When to intervene
- [ ] Debrief talking points

### 3.2 Day 2: Prompt Engineering
**SITUATION.md:**
```
Challenge: "The Lying Bot"
A customer complains: "Your chatbot told me 
we have 500 items in stock. We don't have a single one."

Your task: Figure out why the LLM "hallucination" occurred
and propose how to fix it.

Success Looks Like:
- Understanding why LLMs "lie"
- System prompt best practices
- Grounding techniques
- Testing and evaluation mindset
```

### 3.3 Day 3: Agentic Patterns
**SITUATION.md:**
```
Challenge: "Too Many Agents"
An architect proposed a system with 12 agents. 
The customer asks: "Why so many? Isn't one enough?"

Your task: Explain when to use single-agent 
vs. multi-agent and propose simplification.

Success Looks Like:
- Understands agent patterns (ReAct, Tool Use, Planning)
- Knows when multi-agent makes sense
- Understands orchestration vs. choreography
- Practical architecture proposal
```

---

## 4. ROLE-SPECIFIC SYLLABI (FDE CAPABILITY + OTHER ROLES)

### 4.1 Template for each syllabus:

```markdown
# [ROLE] Track Syllabus

## Role Overview
- What [ROLE] does in an AI project
- How they collaborate with other roles
- Typical deliverable

## Target Certifications
- Primary: [cert name]
- Secondary: [cert name]

## Week-by-Week Breakdown

### Week 1 (Days 4-5): Role Introduction
| Day | Topic | Situation | Deliverable |
|-----|-------|-----------|-------------|
| Day 4 | [topic] | [situation name] | [output] |
| Day 5 | [topic] | [situation name] | [output] |

### Week 2 (Days 6-10): Deep Dive
[similar structure]

### Week 4-5: Team Project
- Role responsibilities in cross-functional team
- Expected contributions
- Integration points with other roles

## Assessment Checkpoints
- Week 1: [checkpoint description]
- Week 2: [checkpoint description]
- Week 4: [checkpoint description]
- Week 5: [checkpoint description]

## AI Tutor Focus Areas
- Primary challenge questions
- Knowledge base topics
- Red flags to watch for
```

### 4.2 Role-Specific Content Overview (aligned with Consult taxonomy):

| Capability / Role | Week 2 Focus | Key Situations | Primary Cert / Outcome |
|-------------------|--------------|----------------|------------------------|
| **FDE (Forward Deployed Engineer capability)** | End-to-end delivery, client demos, productionization | "Customer wants a demo", "Agent crashed in production" | Azure AI Engineer + Consult delivery practices |
| ├─ **AI-SE (within FDE)** | Platform patterns, CI/CD, LLMOps | "Refactor the monolith", "Test this agent" | Azure DevOps Engineer |
| ├─ **AI-FE (within FDE)** | AI-native UI, Streaming, Error states | "User waits 30 seconds", "Make it accessible" | - (front-end specialization inside FDE) |
| └─ **AI-DA (within FDE)** | Data pipelines, KPIs, Dashboards | "Where's the baseline?", "Prove the ROI" | Power BI Data Analyst |
| **AI-DS** | Model evaluation, Experiments, Bias | "Model performance dropped", "Compare these models" | Azure Data Scientist |
| **AI-PM** | Use-case framing, Prioritization, Roadmap | "Scope is too big", "Customer wants everything" | Google PM Certificate |
| **AI-SEC** | Threat modeling, Red teaming, Guardrails | "Red team the chatbot", "Audit this agent" | AZ-500 |
| **AI-DX (Design & UX track)** | Journey mapping, Prototyping, UX research | "Users hate the bot", "Design the happy path" | Cross-cutting UX capability for FDE/AI-FE/AI-PM (no standalone job role) |

---

## 5. AI TUTORS (ChatGPT Enterprise)

### 5.1 Create Custom GPT for each role:

**Name:** `AI Academy - [ROLE] Tutor`

**System prompt structure:**
```
# [ROLE] AI Tutor System Prompt

## Identity
You are an AI Tutor for [ROLE] in Kyndryl AI Academy.

## Personality
[2-3 characteristics]

## Behavioral Rules

### Always do:
- [5 rules]

### Never do:
- [5 prohibitions]

### Challenge patterns:
- "[typical question 1]"
- "[typical question 2]"
- "[typical question 3]"

## Knowledge Base
[Upload KAF docs, role playbook, methodology]
```

### 5.2 Knowledge Base for each tutor:
- [ ] KAF Architecture Overview
- [ ] AI Innovation Lab Method
- [ ] Role-specific playbook
- [ ] Kyndryl case studies (sanitized)
- [ ] Certification exam objectives

---

## 6. MENTOR MATERIALS

### 6.1 Mentor Training Guide
**Content:**
- [ ] AI-Native philosophy explanation
- [ ] 4 mentor functions (designer, observer, intervener, facilitator)
- [ ] Intervention framework (when and how to intervene)
- [ ] Session facilitation walkthrough
- [ ] Assessment and feedback

### 6.2 Mentor Quick Reference Card (1-pager)
**Content:**
- [ ] Daily checklist
- [ ] Intervention triggers
- [ ] Phrases to use / avoid
- [ ] Debrief structure
- [ ] Emergency contacts

### 6.3 Assessment Rubrics
**For each checkpoint:**
- [ ] Artifact quality rubric
- [ ] AI Tutor conversation quality rubric
- [ ] Peer review guidelines
- [ ] "Client-ready" criteria

---

## 7. LABS (Hands-on Exercises)

### 7.1 Lab Structure Template:
```
📁 Lab-XX-[Name]/
├── 📄 README.md           # Overview, learning objectives
├── 📄 INSTRUCTIONS.md     # Step-by-step (but not solution!)
├── 📁 starter/            # Starter code/templates
├── 📁 data/               # Sample data if needed
└── 📁 solution/           # Hidden until after session
```

### 7.2 Lab List:

| Lab | Topic | Roles | Tools |
|-----|-------|-------|-------|
| Lab 01 | First Chatbot | All | Antigravity + Gemini |
| Lab 02 | RAG Pipeline | FDE, AI-SE, AI-DS | Azure AI Search + Gemini |
| Lab 03 | Multi-Agent System | FDE, AI-SE | Antigravity |
| Lab 04 | Deployment to Azure | AI-SE, FDE | Azure Container Apps |
| Lab 05 | Evaluation Framework | AI-DS, FDE | Custom metrics |
| Lab 06 | Security Audit | AI-SEC, AI-SE | OWASP checklist |
| Lab 07 | Dashboard & KPIs | AI-DA, AI-PM | Power BI |
| Lab 08 | UI Prototyping | AI-FE, AI-DX | Figma + React |

---

## 8. TEAM PROJECTS (Week 4-5)

### 8.1 Team Formation
- [ ] 8 teams (1 person per role)
- [ ] Team leads (FDE or AI-PM)
- [ ] Azure DevOps repos pre-created
- [ ] Azure resource groups assigned

### 8.2 Project Brief Template
```markdown
# Team [Name] Project Brief

## Problem Statement
[What we're solving, for whom]

## Success Criteria
[Measurable outcomes]

## Scope
### In Scope:
- [item]
### Out of Scope:
- [item]

## Architecture
[Diagram link]

## Role Responsibilities
| Role | Primary Deliverable |
|------|---------------------|
| FDE | [deliverable] |
| AI-SE | [deliverable] |
| ... | ... |

## Milestones
| Day | Milestone | Owner |
|-----|-----------|-------|
| Day 1 | Problem framing | AI-PM |
| Day 3 | Architecture | FDE |
| Day 5 | MVP | All |
| Day 7 | Peer review | All |
| Day 10 | Final | All |
```

---

## 9. HACKATHON (March 15)

### 9.1 Hackathon Materials
- [ ] Rules & timeline document
- [ ] Evaluation criteria (5 dimensions, weights)
- [ ] Client brief template
- [ ] Presentation template (10 slides max)
- [ ] Demo checklist

### 9.2 Judging Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Business Value | 25% | Does it solve the problem? ROI? |
| Technical Excellence | 25% | Quality of AI implementation |
| Innovation | 20% | Creative use of agentic patterns |
| Presentation | 15% | Clear communication, demo |
| Feasibility | 15% | Can this be productionized? |

---

## 10. IMPLEMENTATION CHECKLIST

### Week of January 20-24 (This Week!)

**Infrastructure:**
- [ ] Confirm Gemini API quota with Google Partner
- [ ] Verify ChatGPT Enterprise seats (80+)
- [ ] Create Azure resource groups for teams
- [ ] Set up Azure DevOps project

**Content - Program Level:**
- [ ] README.md
- [ ] CALENDAR.md
- [ ] ASSESSMENT-CRITERIA.md
- [ ] TOOLS-ACCESS.md

### Week of January 27-31

**ChatGPT Enterprise:**
- [ ] Create 8 AI Tutor GPTs
- [ ] Upload knowledge bases to each
- [ ] Test with pilot users

**Content - Common Foundations:**
- [ ] Day 1 complete (SITUATION, RESOURCES, MENTOR-NOTES)
- [ ] Day 2 complete
- [ ] Day 3 complete

**Content - Role Syllabi:**
- [ ] FDE Syllabus (including how AI-SE / AI-FE / AI-DA specializations roll up into FDE capability)
- [ ] AI-SE Syllabus
- [ ] AI-PM Syllabus
- [ ] AI-FE Syllabus
- [ ] AI-SEC Syllabus
- [ ] AI-DX Syllabus (design & UX skills, not a standalone Consult job role)
- [ ] AI-DA Syllabus
- [ ] AI-DS Syllabus

**Mentor Materials:**
- [ ] Mentor Training Guide
- [ ] Mentor Quick Reference
- [ ] Assessment Rubrics

**Labs:**
- [ ] Lab 01 ready
- [ ] Lab 02 ready

### February 1 (Day Before Launch)

- [ ] All 80 participants have access
- [ ] Welcome email sent
- [ ] Mentor briefing completed
- [ ] Final environment check

---

## 11. INFORMATION NEEDED

1. **KAF Documentation** - any internal docs to integrate into AI Tutors?

2. **Case Studies** - real Kyndryl AI projects (sanitized) for situations?

3. **Existing Content** - materials from partner bootcamps (Microsoft, Google, AWS)?

4. **Hackathon Client** - do you have a customer identified?

5. **Mentor Roster** - how many mentors and what's their background?

---

## 12. NEXT STEPS

Recommended order of work:

1. ✅ Ecosystem document (done)
2. ✅ Implementation plan (done)
3. **NOW:** Program-level documents (README, CALENDAR)
4. **THEN:** Common Foundations (Days 1-3)
5. **THEN:** 8x Role Syllabi (outline + Week 2 detail)
6. **THEN:** 8x AI Tutor System Prompts
7. **THEN:** Labs 1-2
8. **THEN:** Mentor materials

---

## DOCUMENT SUMMARY

| Category | Number of Documents |
|----------|---------------------|
| Program-level | 5 documents |
| Common Foundations (Days 1-3) | 9 documents (3 × SITUATION, RESOURCES, MENTOR-NOTES) |
| Role Syllabi | 8 documents |
| AI Tutor System Prompts | 8 GPT configurations |
| Labs | 8 lab packages |
| Mentor materials | 4 documents |
| Team/Hackathon | 5 documents |
| **TOTAL** | ~50 documents |

---

*Document Version: 1.0*  
*Created: January 25, 2026*  
*For: Kyndryl AI Academy*
