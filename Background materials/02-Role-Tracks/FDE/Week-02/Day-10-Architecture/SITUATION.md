# Day 10: The KAF Deep Dive

## AI Architecture Specialization

*They bought the vision. Now deliver the framework.*

---

## The Situation

```
Email from Engagement Manager:

Subject: KAF Implementation - Financial Services Client
From: Program Director

"Congratulations on closing the KAF deal. Now we need to deliver.

Background:
- Client: Regional financial services firm (€5B AUM)
- Existing state: 3 custom AI agents (built with LangChain)
- Problem: No governance, no observability, frequent failures
- Ask: Full KAF implementation + migration of existing agents

What they bought (as per SOW):
1. KAF Agent Builder deployment
2. KAF AI Core configuration
3. Agent Registry & Catalog setup
4. Memory Management implementation
5. Connectors to their systems (ServiceNow, Salesforce, Bloomberg)
6. Governance layer (security, audit, compliance)

Timeline: 4 months to full production
Team: You + 2 developers + 1 security specialist

Their existing agents:
1. Client Inquiry Agent - Answers questions about portfolios
2. Compliance Check Agent - Validates trades against rules
3. Report Generation Agent - Creates client reports

Current state of their agents:
- Running in Kubernetes (self-managed)
- Using GPT-4 directly (no abstraction layer)
- Logging: stdout only
- Security: API key in environment variable
- Testing: Manual
- Monitoring: None

Your task: Create the implementation architecture and migration plan.
First milestone review is in 2 weeks."
```

---

## Your Challenge

Design and plan a complete KAF implementation for an enterprise client.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Architecture** | Complete KAF deployment architecture |
| **Migration** | Clear path for 3 existing agents to KAF |
| **Governance** | Security, audit, compliance built-in |
| **Integration** | Connectors for all required systems |
| **Timeline** | Realistic 4-month implementation plan |

### Deliverables

1. **KAF Implementation Architecture**
   - All KAF components mapped
   - Infrastructure requirements
   - Integration points

2. **Agent Migration Plan**
   - Per-agent migration approach
   - Testing strategy
   - Rollback procedures

3. **Governance Design**
   - Security architecture
   - Audit logging specification
   - Compliance controls

4. **Implementation Timeline**
   - 4-month milestone plan
   - Resource allocation
   - Dependencies and risks

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | KAF architecture overview |
| Component Design | 30 min | Map KAF to client needs |
| Migration Planning | 25 min | Plan agent migration |
| Governance Design | 15 min | Security and compliance |
| Timeline Creation | 10 min | Build implementation plan |
| Debrief | 15 min | Lessons learned |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> This is your capstone for the Architecture specialization.
> Everything you've learned comes together in KAF implementation.
>
> KAF (Kyndryl Agentic AI Framework) is our answer to enterprise AI.
> It's not just a framework - it's a complete platform for building,
> deploying, and governing AI agents.
>
> **KAF Components:**
> - **Agent Builder** - Low-code/no-code agent creation
> - **AI Core** - LLM abstraction, prompt management
> - **Agent Registry & Catalog** - Agent inventory, versioning
> - **Memory Management** - Conversation state, long-term memory
> - **Connectors** - Pre-built enterprise integrations
> - **Governance** - Security, audit, compliance
>
> The client has existing agents. Your job is NOT to rebuild them.
> Your job is to wrap them in KAF governance and give the client
> enterprise-grade control.
>
> This is what FDE architects do: Make AI enterprise-ready.

---

## KAF Architecture Reference

```
┌─────────────────────────────────────────────────────────────────┐
│                  KYNDRYL AGENTIC AI FRAMEWORK                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                    GOVERNANCE LAYER                         ││
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐   ││
│  │  │ Security │ │  Audit   │ │Compliance│ │ Access       │   ││
│  │  │ Controls │ │ Logging  │ │ Rules    │ │ Control      │   ││
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────┘   ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   AGENT     │  │     AI      │  │    AGENT REGISTRY       │ │
│  │   BUILDER   │  │    CORE     │  │    & CATALOG            │ │
│  │             │  │             │  │                         │ │
│  │ • Templates │  │ • LLM APIs  │  │ • Version control       │ │
│  │ • Designer  │  │ • Prompts   │  │ • Discovery             │ │
│  │ • Testing   │  │ • Routing   │  │ • Dependencies          │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
│                                                                 │
│  ┌─────────────┐  ┌─────────────────────────────────────────┐  │
│  │   MEMORY    │  │           CONNECTORS                    │  │
│  │ MANAGEMENT  │  │                                         │  │
│  │             │  │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐│  │
│  │ • Session   │  │ │ SAP │ │SNOW │ │SFDC │ │O365 │ │Custom││  │
│  │ • Long-term │  │ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘│  │
│  │ • Context   │  │                                         │  │
│  └─────────────┘  └─────────────────────────────────────────┘  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                 ORCHESTRATION RUNTIME                       ││
│  │  Agent execution • Workflow management • Circuit breakers   ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Client's Existing Agents

### Agent 1: Client Inquiry Agent

**Current state:**
```python
# Simplified current implementation
def client_inquiry_agent(query, client_id):
    portfolio = get_portfolio(client_id)  # Direct API call
    prompt = f"Answer this about portfolio: {query}"
    response = openai.chat(prompt + str(portfolio))  # Direct LLM call
    return response  # No logging, no validation
```

**Issues:**
- No input validation
- No output filtering
- Direct LLM access
- No audit trail

### Agent 2: Compliance Check Agent

**Current state:**
```python
# Simplified current implementation
def compliance_agent(trade_request):
    rules = load_rules()  # From local file
    prompt = f"Check if this trade complies: {trade_request}"
    result = openai.chat(prompt + str(rules))
    return "APPROVED" if "approved" in result.lower() else "REJECTED"
```

**Issues:**
- Compliance decision by string matching
- No explanation of decisions
- No human oversight for edge cases
- Rules not version controlled

### Agent 3: Report Generation Agent

**Current state:**
```python
# Simplified current implementation
def report_agent(client_id, report_type):
    data = get_client_data(client_id)  # Multiple API calls
    prompt = f"Generate {report_type} report"
    report = openai.chat(prompt + str(data))
    return format_pdf(report)  # Unvalidated content to PDF
```

**Issues:**
- Sensitive data in prompts
- No content validation
- No branding compliance
- No approval workflow

---

## Exploration with AI Tutor

### Questions to Investigate

**KAF Components:**
- "How does KAF Agent Builder work for migrating existing agents?"
- "What does KAF AI Core provide beyond direct LLM access?"
- "How does KAF Memory Management handle conversation state?"

**Migration:**
- "How do I migrate a LangChain agent to KAF?"
- "What's the best approach for migrating with zero downtime?"
- "How do I test that migrated agents behave identically?"

**Governance:**
- "How does KAF implement audit logging for financial services?"
- "What compliance controls does KAF provide out of the box?"
- "How do I add human-in-the-loop for compliance decisions?"

---

## Hints

<details>
<summary>Hint 1: Migration Strategy (After 15 min)</summary>

**Wrapper approach for existing agents:**

```
┌─────────────────────────────────────────────┐
│           KAF AGENT WRAPPER                 │
├─────────────────────────────────────────────┤
│  INPUT VALIDATION                           │
│  ├── Schema validation                     │
│  ├── PII detection                         │
│  └── Rate limiting                         │
├─────────────────────────────────────────────┤
│  [EXISTING AGENT CODE]                      │
│  (Unchanged initially)                      │
├─────────────────────────────────────────────┤
│  OUTPUT PROCESSING                          │
│  ├── Content filtering                     │
│  ├── Format validation                     │
│  └── Audit logging                         │
└─────────────────────────────────────────────┘
```

**Migration phases:**
1. Wrap existing agent (no code changes)
2. Add KAF governance (logging, security)
3. Migrate to KAF AI Core (LLM abstraction)
4. Add KAF Memory Management
5. Full KAF native (optional, based on ROI)

</details>

<details>
<summary>Hint 2: Governance for Financial Services (After 25 min)</summary>

**Required controls:**

1. **Audit trail:**
   - Every agent invocation logged
   - Input, output, duration, user
   - Immutable storage (7 years for financial)

2. **Access control:**
   - Role-based agent access
   - Client data segregation
   - MFA for sensitive agents

3. **Compliance checks:**
   - Pre-execution rule validation
   - Post-execution content scanning
   - Human approval for high-risk actions

4. **Security:**
   - PII masking in logs
   - Encryption at rest and in transit
   - Secret management via Key Vault

**For Compliance Agent specifically:**
- All decisions must be explainable
- Edge cases route to human
- Decision audit trail for regulators

</details>

<details>
<summary>Hint 3: Connector Implementation (After 35 min)</summary>

**Required connectors:**

1. **ServiceNow:**
   - Purpose: Incident management, change tracking
   - Auth: OAuth 2.0
   - KAF provides: Pre-built connector

2. **Salesforce:**
   - Purpose: Client data, opportunities
   - Auth: OAuth 2.0 (connected app)
   - KAF provides: Pre-built connector

3. **Bloomberg:**
   - Purpose: Market data, pricing
   - Auth: Bloomberg API key
   - KAF provides: Custom connector needed

**Connector architecture:**
```
[Agent] → [KAF Connector Layer] → [External System]
              │
              ├── Authentication handling
              ├── Rate limiting
              ├── Error handling
              ├── Response caching
              └── Audit logging
```

</details>

<details>
<summary>Hint 4: Implementation Timeline (After 45 min)</summary>

**4-Month Implementation Plan:**

**Month 1: Foundation**
- Week 1-2: KAF infrastructure deployment
- Week 3: Governance layer configuration
- Week 4: Security hardening, access control
- Milestone: KAF platform operational

**Month 2: Migration Phase 1**
- Week 5-6: Client Inquiry Agent migration
- Week 7-8: Testing and validation
- Milestone: First agent in KAF production

**Month 3: Migration Phase 2**
- Week 9-10: Compliance Agent migration + human-in-loop
- Week 11-12: Report Agent migration
- Milestone: All agents migrated

**Month 4: Integration & Polish**
- Week 13: Connector integrations (ServiceNow, SFDC)
- Week 14: Bloomberg custom connector
- Week 15: Performance tuning, documentation
- Week 16: Training, handover, go-live
- Milestone: Full production deployment

**Risk buffer:** 2 weeks built into Month 4

</details>

---

## Peer Review Prompts

Challenge your partner's KAF implementation:

1. A regulator asks for all compliance decisions for 2025. How fast can you produce them?
2. The Bloomberg API changes. What's the impact?
3. An agent starts producing incorrect reports. How do you diagnose?
4. A new agent needs to be added. How long does it take?
5. The client wants to use Claude instead of GPT. What changes?

---

## Week 2 Architecture Completion

Congratulations! You've completed the AI Architecture specialization track.

**This week you learned:**
- Day 6: Enterprise integration architecture
- Day 7: Multi-agent orchestration and governance
- Day 8: EU AI Act compliance architecture
- Day 9: Scaling from POC to production
- Day 10: KAF implementation and delivery

**You can now:**
- [ ] Design end-to-end AI architectures
- [ ] Implement multi-agent systems with governance
- [ ] Ensure regulatory compliance
- [ ] Scale AI systems for enterprise
- [ ] Lead KAF implementation projects

---

*"The best architects don't just design systems. They design systems that can evolve, scale, and be trusted. Welcome to enterprise AI."*
