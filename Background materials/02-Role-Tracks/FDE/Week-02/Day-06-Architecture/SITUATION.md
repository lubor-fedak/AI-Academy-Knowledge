# Day 6: The Integration Nightmare

## AI Architecture Specialization

*When 5 enterprise systems meet one AI assistant, someone has to make them talk to each other.*

---

## The Situation

```
Email from the client's CTO:

"We've tried this twice before. Two different vendors. Both failed.

Our situation: We need an AI assistant that can answer questions
by pulling data from our 5 core systems:

1. SAP (ERP) - inventory, orders, financials
2. ServiceNow (ITSM) - tickets, incidents, changes
3. Salesforce (CRM) - customers, opportunities, contracts
4. SharePoint (Documents) - policies, procedures, guides
5. Custom ERP (Legacy) - manufacturing data, SOAP API from 2008

The first vendor built a RAG system that only connected to SharePoint.
Useful, but not what we needed.

The second vendor promised to connect everything. After 3 months,
they had partial SAP integration that broke every time SAP updated.
They blamed our IT team. Our IT team blamed them. Everyone quit.

We have a new AI budget. We have executive commitment. But we have
ZERO patience for another failed integration project.

Your task: Design an architecture that ACTUALLY works.

We need a proposal by end of week. Include:
- How you'll connect to each system
- How you'll handle authentication (each system has different auth)
- How you'll deal with the legacy SOAP API
- What happens when one system is down
- How long this will realistically take

I'm done with optimistic promises. Give me a real plan."
```

---

## Your Challenge

Design an enterprise integration architecture that survives reality.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Architecture** | Clear diagram showing all data flows |
| **Integration Patterns** | Appropriate pattern for each system |
| **Auth Strategy** | Unified approach to different auth mechanisms |
| **Resilience** | System works when individual components fail |
| **Realism** | Honest timeline with identified risks |

### Deliverables

1. **Architecture Diagram**
   - All 5 systems + AI components
   - Data flows clearly marked
   - Auth boundaries identified

2. **Integration Specification** (per system)
   - Connection method
   - Authentication approach
   - Data transformation needs
   - Failure handling

3. **Risk Assessment**
   - Top 5 integration risks
   - Mitigation strategies
   - Contingency plans

4. **Timeline Proposal**
   - Phased approach (what connects first?)
   - Realistic duration estimates
   - Dependencies and blockers

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | Why integrations fail |
| System Analysis | 20 min | Understand each system's constraints |
| Architecture Design | 30 min | Create your integration architecture |
| Risk Assessment | 15 min | Identify what will go wrong |
| Peer Review | 15 min | Challenge each other's designs |
| Debrief | 15 min | Best practices discussion |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> Integration is where AI projects die.
>
> Not because integration is hard. It IS hard. But because teams
> underestimate it, promise too much, and then drown in edge cases.
>
> The key insight: Every enterprise system was built by a different
> team, in a different decade, with different assumptions. They were
> never meant to work together.
>
> Your job as an architect: Make them work together anyway.
>
> Common integration patterns you'll explore:
> - **API Gateway** - Unified access point
> - **Event-Driven** - Pub/sub for loose coupling
> - **ETL Pipeline** - Batch data synchronization
> - **Adapter Pattern** - Normalize different interfaces
>
> The legacy SOAP API is a gift. If you can handle that, you can
> handle anything.

---

## Exploration with AI Tutor

### Questions to Investigate

**System-specific:**
- "What are best practices for SAP integration with AI systems?"
- "How do I connect to ServiceNow's API securely?"
- "What are the challenges of legacy SOAP API integration?"

**Architecture patterns:**
- "When should I use an API gateway vs. direct integration?"
- "How do I design for graceful degradation when one system is down?"
- "What's the best way to handle different authentication mechanisms?"

**Enterprise considerations:**
- "How do I manage credentials securely across 5 systems?"
- "What's the right caching strategy for enterprise data?"
- "How do I handle data freshness vs. performance trade-offs?"

---

## System Constraints Reference

### SAP
- **API:** REST (S/4HANA) or RFC (older)
- **Auth:** OAuth 2.0 or SAML
- **Challenge:** Complex data model, frequent updates
- **Latency:** 500ms - 2s typical

### ServiceNow
- **API:** REST
- **Auth:** OAuth 2.0
- **Challenge:** Rate limits, table access permissions
- **Latency:** 200ms - 500ms typical

### Salesforce
- **API:** REST or SOAP
- **Auth:** OAuth 2.0 (connected app)
- **Challenge:** Governor limits, complex relationships
- **Latency:** 100ms - 300ms typical

### SharePoint
- **API:** Microsoft Graph or REST
- **Auth:** Azure AD / OAuth 2.0
- **Challenge:** Document parsing, versioning
- **Latency:** 200ms - 1s typical

### Legacy ERP (SOAP)
- **API:** SOAP/WSDL
- **Auth:** Basic auth or WS-Security
- **Challenge:** No documentation, brittle contracts
- **Latency:** 1s - 5s typical

---

## Hints

<details>
<summary>Hint 1: Architecture Pattern (After 15 min)</summary>

Consider a **unified integration layer**:

```
[AI Assistant]
     ↓
[Integration Hub / API Gateway]
     ↓
[Adapters: SAP | SNOW | SFDC | SPO | Legacy]
     ↓
[Enterprise Systems]
```

Benefits:
- AI doesn't know about system complexity
- Each adapter handles its own auth
- Failures are isolated
- Can swap systems without changing AI

</details>

<details>
<summary>Hint 2: Auth Strategy (After 25 min)</summary>

**Credential management options:**
1. **Azure Key Vault** - Centralized secrets management
2. **Managed Identities** - For Azure-native services
3. **Service Accounts** - Dedicated accounts per system
4. **Token Refresh** - Background process for OAuth tokens

**Anti-pattern:** Storing credentials in config files

</details>

<details>
<summary>Hint 3: Handling Failures (After 35 min)</summary>

**Graceful degradation strategy:**

```
If SAP is down:
  → Return cached data if < 1 hour old
  → Show "inventory data temporarily unavailable"
  → Continue answering questions from other sources
  → Log for alerting
```

**Circuit breaker pattern:**
- After 5 failures → open circuit
- Stop calling failing system for 5 minutes
- Test with single request before closing circuit

</details>

<details>
<summary>Hint 4: Timeline Reality (After 45 min)</summary>

**Typical integration timeline:**
- SharePoint: 2 weeks (well-documented API)
- ServiceNow: 3 weeks (good API, permission complexity)
- Salesforce: 3-4 weeks (data model complexity)
- SAP: 4-6 weeks (most complex)
- Legacy SOAP: 4-8 weeks (discovery + reverse engineering)

**Total realistic estimate:** 4-6 months for full integration

**Phased approach:**
1. Phase 1 (Month 1-2): SharePoint + ServiceNow
2. Phase 2 (Month 2-3): Salesforce
3. Phase 3 (Month 3-5): SAP
4. Phase 4 (Month 4-6): Legacy ERP

</details>

---

## Peer Review Prompts

When reviewing your partner's architecture:

1. What happens when SAP is down for maintenance?
2. How are credentials rotated without downtime?
3. Can you add a 6th system without redesigning?
4. What's the latency budget for end-to-end queries?
5. How do you know when integration is broken?

---

## Connection to Tomorrow

Tomorrow you'll design a **multi-agent architecture** where agents
need to coordinate with each other. If you thought system integration
was complex, wait until you add autonomous agents to the mix.

---

*"Enterprise integration is where architectural dreams meet operational reality. Design for the reality."*
