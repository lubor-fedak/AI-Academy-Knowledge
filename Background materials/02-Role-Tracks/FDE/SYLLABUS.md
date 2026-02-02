# Forward Deployed Engineer (FDE) Track Syllabus

## Role Overview

The Forward Deployed Engineer is the **client-facing technical expert** who turns AI concepts into working demos and production solutions. FDEs are the bridge between what's technically possible and what the client actually needs.

This syllabus describes the Forward Deployed Engineer capability in the Consult role model. AI-SE, AI-FE, AI-DA, and **AI-ARCH** represent specializations within this capability.

### Core Responsibilities
- Lead technical discovery with clients
- Build demos and proof-of-concepts rapidly
- Deploy and troubleshoot AI solutions in production
- Translate between technical teams and business stakeholders

### FDE Specializations

| Specialization | Code | Focus |
|----------------|------|-------|
| **AI Architecture** | AI-ARCH | End-to-end system design, multi-agent orchestration, enterprise governance |
| AI Software Engineering | AI-SE | Platform development, CI/CD, LLMOps, reliability |
| Front-End Engineering | AI-FE | AI-native UI, streaming, accessibility |
| Data & Analytics | AI-DA | Data pipelines, KPIs, dashboards, ROI |

> **AI Architecture (AI-ARCH)** is a senior FDE specialization for those who want to focus on system-level design, multi-agent coordination, and enterprise governance. It combines technical depth with architectural breadth.

### Collaboration Points
| With | You Provide | You Receive |
|------|-------------|-------------|
| AI-PM | Technical feasibility, estimates | Requirements, priorities |
| AI-SE | Demo code, deployment needs | Production architecture |
| AI-DS | Use case requirements | Model recommendations |
| AI-SEC | System architecture | Security review |

### Typical Deliverables
- Working demos (24-48 hour turnaround)
- Technical architecture proposals
- Deployment runbooks
- Client-facing technical documentation

---

## Target Certifications

| Priority | Certification | Provider |
|----------|---------------|----------|
| **Primary** | Azure AI Engineer Associate | Microsoft |
| Secondary | Google Cloud Professional ML Engineer | Google |

---

## Week-by-Week Breakdown

### Week 1 (Days 1-5): Foundations + Role Introduction

| Day | Topic | Situation | Deliverable |
|-----|-------|-----------|-------------|
| 1 | AI Landscape | "The CEO Asks" | Executive briefing |
| 2 | Prompt Engineering | "The Lying Bot" | Hallucination fix |
| 3 | Agentic Patterns | "Too Many Agents" | Simplified architecture |
| 4 | FDE Mindset | "Customer Wants a Demo" | 24-hour demo plan |
| 5 | Rapid Prototyping | "Scope Creep Alert" | Scoped demo + backlog |

**Week 1 Checkpoint:** Working chatbot demo + technical brief

---

### Week 2 (Days 6-10): Deep Dive

| Day | Topic | Situation | Deliverable |
|-----|-------|-----------|-------------|
| 6 | RAG Pipelines | "Documents Won't Load" | Working RAG system |
| 7 | Multi-Agent Systems | "Agents Won't Cooperate" | Orchestrated workflow |
| 8 | Deployment Basics | "Works on My Machine" | Containerized solution |
| 9 | Production Hardening | "Agent Crashed at 2AM" | Monitoring + alerting |
| 10 | Client Demo Day | "Final Presentation" | Live demo + Q&A |

**Week 2 Checkpoint:** Production-ready RAG demo + deployment guide

---

### Spring Break (Week 3)

**Self-Paced Assignments:**
- [ ] Complete Azure AI Engineer learning path (modules 1-4)
- [ ] Build personal project using KAF
- [ ] Review peer feedback from Week 2

---

### Week 4-5: Team Project + Certification

**Your Role in Team:**
- Technical lead for implementation
- Own the architecture decisions
- Build the demo flow
- Lead technical troubleshooting

**Expected Contributions:**
| Week | Contribution |
|------|--------------|
| Week 4 | Architecture design, core implementation |
| Week 5 | Polish, deployment, demo preparation |

---

## Key Situations

### S-FDE-01: "Customer Wants a Demo" (Day 4)

```yaml
Context: |
  A potential client wants to see an AI agent that can 
  answer questions about their internal documents.
  You have 24 hours.
  
Challenge: |
  - Build a working RAG demo
  - Make it look professional
  - Handle the "what if" questions
  
Success: |
  - Demo works reliably
  - Can handle basic edge cases
  - Technical approach is defensible
```

### S-FDE-02: "Agent Crashed in Production" (Day 9)

```yaml
Context: |
  It's 2AM. The client's AI agent stopped responding.
  You have access to logs but no documentation.
  The client is escalating.
  
Challenge: |
  - Diagnose the issue systematically
  - Communicate with the client professionally
  - Fix it and prevent recurrence
  
Success: |
  - Root cause identified
  - Fix implemented
  - Post-mortem documented
```

---

## AI Tutor Focus Areas

### Primary Challenge Questions
- "What will the customer say when they see this?"
- "How fast can you build a working demo?"
- "What breaks first in production?"
- "Can you explain this to a non-technical stakeholder?"

### Knowledge Base Topics
- KAF Architecture and Services
- Azure AI Services (OpenAI, Search, Cosmos DB)
- RAG implementation patterns
- Demo best practices
- Production debugging

### Red Flags to Watch
- Over-engineering for a demo
- Ignoring client constraints
- Building without deployment plan
- Promising features you can't deliver

---

## Assessment Checkpoints

### Week 1 Checkpoint
| Criterion | Weight |
|-----------|--------|
| Working demo | 40% |
| Technical documentation | 30% |
| AI Tutor conversation quality | 20% |
| Peer review contribution | 10% |

### Week 2 Checkpoint
| Criterion | Weight |
|-----------|--------|
| Production-ready code | 40% |
| Deployment automation | 25% |
| Monitoring/alerting | 20% |
| Client-ready documentation | 15% |

### Final Assessment (Hackathon)
| Criterion | Weight |
|-----------|--------|
| Working solution | 35% |
| Technical excellence | 25% |
| Demo quality | 20% |
| Team collaboration | 20% |

---

## Tools & Resources

### Primary Tools
- **IDE:** Google Antigravity (Gemini integration)
- **AI API:** Gemini API (primary), Azure OpenAI (secondary)
- **Search:** Azure AI Search
- **Database:** Azure Cosmos DB
- **Deployment:** Azure Container Apps

### Reference Documentation
- KAF Documentation (SharePoint)
- Azure AI Services Docs
- Gemini API Reference

---

## Daily Schedule Template

| Time | Activity |
|------|----------|
| 09:00-09:05 | Micro-context |
| 09:05-09:10 | Situation briefing |
| 09:10-10:00 | Build + AI Tutor |
| 10:00-10:15 | Debrief |
| 10:15-10:30 | Peer exchange |
| Flexible | 90 min self-study |

---

## Success Profile

By end of academy, an FDE graduate can:

- [ ] Build a working AI demo in 24 hours
- [ ] Deploy to production with monitoring
- [ ] Troubleshoot AI systems systematically
- [ ] Communicate technically with clients
- [ ] Collaborate effectively with all AI roles
- [ ] Pass Azure AI Engineer certification exam

---

## AI Architecture Specialization (AI-ARCH)

> **For FDEs who want to focus on system-level design and enterprise governance.**

### AI-ARCH Overview

The AI Architect specialization is for experienced FDEs who focus on:
- **End-to-end AI system design** across multiple components
- **Multi-agent orchestration** and coordination patterns
- **Enterprise governance** including EU AI Act compliance
- **KAF deep implementation** and customization
- **Scaling strategies** from POC to production at scale

### Who Should Choose AI-ARCH

Ideal for participants who:
- Have 5+ years of system design experience
- Enjoy big-picture thinking over implementation details
- Want to lead technical architecture discussions with clients
- Are interested in AI governance and compliance
- See themselves as technical leads on large AI programs

### AI-ARCH Week 2 Situations

| Day | Topic | Situation | Deliverable |
|-----|-------|-----------|-------------|
| 6 | Integration Design | "The Integration Nightmare" | Enterprise integration architecture |
| 7 | Multi-Agent Architecture | "The Agent Swarm" | 8-agent orchestration design |
| 8 | Governance Architecture | "The Compliance Blueprint" | EU AI Act compliant architecture |
| 9 | Scale Architecture | "Scale or Fail" | POC to 10,000 users migration plan |
| 10 | KAF Implementation | "The KAF Deep Dive" | Full KAF deployment architecture |

---

### S-ARCH-01: "The Integration Nightmare" (Day 6)

```yaml
Context: |
  A global manufacturing company wants to connect their AI assistant
  to 5 enterprise systems: SAP, ServiceNow, Salesforce, SharePoint,
  and their custom ERP. Each system has different auth, APIs, and
  data formats.

  The previous vendor gave up after 3 months.

Challenge: |
  - Design an integration architecture that works
  - Handle authentication across systems
  - Manage data transformation and consistency
  - Plan for system failures and fallbacks

Success: |
  - Architecture diagram with clear data flows
  - Integration patterns for each system
  - Error handling and fallback strategy
  - Timeline and risk assessment
```

---

### S-ARCH-02: "The Agent Swarm" (Day 7)

```yaml
Context: |
  You're designing a multi-agent system for a logistics company.
  They need 8 specialized agents:
  - Route Optimization Agent
  - Inventory Management Agent
  - Customer Communication Agent
  - Pricing Agent
  - Compliance Agent
  - Analytics Agent
  - Alert Agent
  - Coordination Agent

  Last time someone built this, the agents created an infinite loop
  that sent 10,000 customer notifications in one hour.

Challenge: |
  - Design the orchestration architecture
  - Define agent-to-agent communication protocols
  - Implement governance to prevent loops
  - Build in human oversight at key points

Success: |
  - Multi-agent architecture diagram
  - Communication protocol specification
  - Circuit breaker and governance rules
  - Human-in-the-loop design
```

---

### S-ARCH-03: "The Compliance Blueprint" (Day 8)

```yaml
Context: |
  A healthcare company in the EU wants to deploy AI agents that
  help doctors with diagnosis suggestions. This falls under EU AI Act
  as high-risk AI.

  They need to go live in 6 months. The compliance team has 47
  questions and no one knows how to answer them.

Challenge: |
  - Design an architecture that meets EU AI Act requirements
  - Build in transparency and explainability
  - Implement human oversight for high-risk decisions
  - Create audit trail for all AI actions

Success: |
  - EU AI Act compliance architecture
  - Risk classification and mitigation
  - Audit and logging design
  - Human oversight workflow
```

---

### S-ARCH-04: "Scale or Fail" (Day 9)

```yaml
Context: |
  Your POC for a retail client was wildly successful. 50 pilot users
  love it. Now they want to roll out to 10,000 employees across
  20 countries in 3 months.

  The POC runs on a single Azure instance. Latency is already
  creeping up with 50 users. No one documented the architecture.

Challenge: |
  - Design a scaled architecture for 10,000+ users
  - Plan for multi-region deployment
  - Ensure consistent performance under load
  - Create a migration path from POC to production

Success: |
  - Scalable architecture design
  - Multi-region deployment plan
  - Performance benchmarks and targets
  - Migration runbook with rollback
```

---

### S-ARCH-05: "The KAF Deep Dive" (Day 10)

```yaml
Context: |
  A financial services client bought into the Kyndryl Agentic
  Framework vision. Now they want you to implement it fully.

  They have existing infrastructure (Azure), existing agents
  (3 custom-built), and existing governance (minimal). They want
  the full KAF experience: Agent Builder, Registry, Memory
  Management, Connectors, and Governance.

Challenge: |
  - Design full KAF implementation architecture
  - Plan migration of existing agents to KAF
  - Implement all KAF components
  - Train client team on KAF operations

Success: |
  - Complete KAF architecture design
  - Agent migration plan
  - Implementation timeline
  - Operations and maintenance guide
```

---

### AI-ARCH Assessment Criteria

| Criterion | Weight |
|-----------|--------|
| Architecture quality | 35% |
| Governance integration | 25% |
| Scalability design | 20% |
| Documentation quality | 20% |

### AI-ARCH Success Profile

By end of academy, an AI-ARCH graduate can:

- [ ] Design end-to-end AI architectures for enterprise
- [ ] Implement multi-agent orchestration with governance
- [ ] Ensure EU AI Act compliance in architecture
- [ ] Scale AI systems from POC to production
- [ ] Lead KAF implementation projects
- [ ] Advise C-level on AI architecture decisions
