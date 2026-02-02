# Team Project 1: SmartTicket AI

## Intelligent IT Service Desk Automation

---

## Project Overview

| Item | Details |
|------|---------|
| **Project Name** | SmartTicket AI |
| **Duration** | Days 11-22 (2 weeks) |
| **Team Size** | 8-10 people (cross-functional) |
| **Pilot Client** | Global Manufacturing Company |
| **Budget** | €200,000 simulation |

---

## The Brief

```
CLIENT REQUEST:

"Our IT service desk handles 2,000 tickets per day. 60% are routine:
password resets, software requests, VPN issues. Our analysts spend
80% of their time on these routine tasks instead of complex problems.

We want an AI system that:
1. Automatically triages incoming tickets
2. Resolves routine tickets without human intervention
3. Routes complex tickets to the right specialist
4. Provides 24/7 coverage (we're global, 5 time zones)

Current pain points:
- Average resolution time: 4 hours for routine, 2 days for complex
- 30% of tickets are misrouted
- Night shift has skeleton crew → 8+ hour response time
- Analysts are frustrated with repetitive work

Success metrics:
- 50% reduction in routine ticket handling time
- 90% correct routing for complex tickets
- 24/7 response within 15 minutes
- Analyst satisfaction improvement

Constraints:
- Must integrate with ServiceNow (our ITSM)
- Cannot have access to production systems (governance requirement)
- Must be auditable for compliance
- EU data residency required"
```

---

## Required Deliverables

### Week 1 (Days 11-15): Build Phase

| Day | Deliverable | Owner Roles |
|-----|-------------|-------------|
| 11 | Architecture design + ServiceNow integration plan | FDE, AI-SE |
| 12 | Ticket classification model + triage logic | AI-DS, FDE |
| 13 | Automation workflows for top 5 routine tickets | FDE, AI-SE |
| 14 | Human escalation and routing logic | AI-PM, FDE |
| 15 | Security review + governance framework | AI-SEC, AI-SE |

**Week 1 Checkpoint:** Working prototype handling 3 ticket types

### Week 2 (Days 16-22): Polish Phase

| Day | Deliverable | Owner Roles |
|-----|-------------|-------------|
| 16-17 | UI for analyst dashboard + ticket monitoring | AI-FE, AI-DX |
| 18-19 | Analytics dashboard + KPI tracking | AI-DA, AI-FE |
| 20 | Performance testing + optimization | AI-SE, AI-DS |
| 21 | Documentation + runbook creation | All roles |
| 22 | Client demo preparation + final polish | All roles |

**Week 2 Checkpoint:** Production-ready system with documentation

---

## Technical Requirements

### Must Have
- [ ] ServiceNow API integration (mock or sandbox)
- [ ] Ticket classification (>85% accuracy on test set)
- [ ] At least 5 automated resolution workflows
- [ ] Human escalation triggers
- [ ] Audit logging for all AI decisions
- [ ] Response time < 30 seconds for triage

### Should Have
- [ ] Real-time dashboard for ticket monitoring
- [ ] Analyst feedback loop for model improvement
- [ ] Multi-language support (English + German)
- [ ] SLA tracking and alerting

### Nice to Have
- [ ] Predictive analytics (ticket volume forecasting)
- [ ] Sentiment analysis for escalation priority
- [ ] Knowledge base auto-suggestion

---

## Role Responsibilities

| Role | Primary Responsibilities |
|------|-------------------------|
| **AI-PM** | Scope management, stakeholder communication, success metrics |
| **FDE** | Core implementation, ServiceNow integration, demo |
| **AI-SE** | Architecture, deployment, monitoring, CI/CD |
| **AI-DS** | Classification model, evaluation, quality metrics |
| **AI-DA** | KPI dashboard, ROI calculations, analytics |
| **AI-SEC** | Security review, access controls, compliance |
| **AI-FE** | Analyst dashboard UI, real-time updates |
| **AI-DX** | User research, UX design, analyst workflow |

---

## Evaluation Criteria

| Criterion | Weight | Excellent | Good | Developing |
|-----------|--------|-----------|------|------------|
| **Working Solution** | 30% | All must-haves + should-haves | All must-haves | Partial must-haves |
| **Technical Quality** | 25% | Production-ready, well-tested | Functional, some tests | Works but fragile |
| **Business Value** | 20% | Clear ROI, metrics tracked | Value articulated | Vague value |
| **Governance** | 15% | Comprehensive audit trail | Basic logging | Minimal |
| **Team Collaboration** | 10% | All roles contributed visibly | Most roles active | Siloed work |

---

## Resources Provided

- ServiceNow sandbox instance (credentials in SharePoint)
- Sample ticket dataset (10,000 historical tickets, anonymized)
- KAF documentation and starter templates
- Azure subscription with €500 credit
- Weekly mentor office hours

---

## Milestones

| Milestone | Due | Deliverable |
|-----------|-----|-------------|
| M1: Architecture Approved | Day 12 | Architecture diagram signed off |
| M2: Prototype Demo | Day 15 | 3 ticket types working |
| M3: Integration Complete | Day 18 | ServiceNow connected |
| M4: Dashboard Ready | Day 20 | Analytics visible |
| M5: Final Demo | Day 22 | Client presentation |

---

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| ServiceNow API complexity | High | Use sandbox, mock if needed |
| Classification accuracy low | High | Start with simple rules, ML later |
| Team coordination issues | Medium | Daily standups, clear ownership |
| Scope creep | Medium | PM enforces must-have focus |
| Security concerns | High | AI-SEC involved from Day 1 |

---

*"The best IT support is the support users never have to wait for."*
