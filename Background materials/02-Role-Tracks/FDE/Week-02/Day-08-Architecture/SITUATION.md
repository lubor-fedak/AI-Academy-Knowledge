# Day 8: The Compliance Blueprint

## AI Architecture Specialization

*High-risk AI in healthcare. EU AI Act compliance. No room for error.*

---

## The Situation

```
Meeting request from Healthcare Client:

Subject: URGENT - AI Compliance Architecture Review
From: Chief Medical Officer, Regional Hospital Group

"We're deploying an AI system that assists radiologists with
preliminary scan analysis. It highlights potential areas of concern
in X-rays, MRIs, and CT scans.

We KNOW this falls under EU AI Act as high-risk AI (Annex III,
healthcare devices). We KNOW we need compliance. We just don't
know HOW.

Our compliance team sent 47 questions. Our IT team has no answers.
Our vendor says 'compliance is your responsibility.' Our lawyers
are billing €500/hour to tell us they don't understand AI.

We go live in 6 months. The system is already built. We need an
architecture that wraps compliance around it.

Key requirements from EU AI Act (as we understand them):
1. Human oversight - Doctors must remain in control
2. Transparency - Explain why AI flagged something
3. Data governance - Training data must be documented
4. Accuracy & robustness - Must prove it works
5. Audit trail - Every decision must be traceable
6. Risk management - Ongoing monitoring required

Please review our current architecture and propose changes.
Budget is not the blocker. Compliance failure is.

Current architecture attached. Meeting tomorrow."

ATTACHMENT: current-architecture.pdf
- AI model runs on Azure
- Results displayed in existing radiology software
- No logging beyond "model was called"
- No explainability layer
- Doctors can "accept" or "reject" AI suggestions
- No audit trail of decisions
```

---

## Your Challenge

Design an EU AI Act compliant architecture for high-risk healthcare AI.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Compliance Mapping** | Each AI Act requirement mapped to architecture |
| **Human Oversight** | Clear design for meaningful human control |
| **Transparency** | Explainability built into the system |
| **Audit Trail** | Complete traceability of all AI actions |
| **Risk Management** | Ongoing monitoring and quality assurance |

### Deliverables

1. **EU AI Act Compliance Architecture**
   - Diagram showing all compliance components
   - How each requirement is addressed
   - Integration with existing system

2. **Human Oversight Design**
   - When AI can act autonomously
   - When human approval required
   - How to ensure oversight is meaningful

3. **Audit & Logging Specification**
   - What gets logged
   - How long it's retained
   - How it can be queried

4. **Risk Management Framework**
   - Ongoing monitoring approach
   - Quality metrics and thresholds
   - Incident response process

---

## Time Box

| Phase | Duration | Activity |
|-------|----------|----------|
| Micro-Context | 5 min | EU AI Act essentials |
| Requirement Analysis | 20 min | Map AI Act to architecture |
| Architecture Design | 30 min | Design compliant system |
| Documentation | 15 min | Create compliance artifacts |
| Peer Review | 15 min | Legal stress test |
| Debrief | 15 min | Best practices |

---

## Micro-Context (5 minutes)

*Mentor delivers:*

> The EU AI Act came into full force in 2025. High-risk AI systems
> now have legal requirements, not just best practices.
>
> Healthcare AI that assists diagnosis is explicitly high-risk
> (Annex III). This means:
>
> **Mandatory requirements:**
> 1. Risk management system (Article 9)
> 2. Data governance (Article 10)
> 3. Technical documentation (Article 11)
> 4. Record-keeping (Article 12)
> 5. Transparency & information (Article 13)
> 6. Human oversight (Article 14)
> 7. Accuracy, robustness, security (Article 15)
>
> **Non-compliance penalties:** Up to €35 million or 7% global revenue.
>
> Your job: Design an architecture that makes compliance possible.
> Not a legal document - an actual technical system.
>
> Remember: Compliance is not a checkbox. It's a continuous process
> that must be built into the architecture.

---

## EU AI Act Requirements Reference

### Article 9: Risk Management System

**Requirement:** Continuous, iterative risk management throughout AI lifecycle

**Architecture implication:**
- Risk registry integrated with system
- Automated risk monitoring
- Escalation paths for new risks

### Article 10: Data Governance

**Requirement:** Training data must be relevant, representative, free of errors

**Architecture implication:**
- Data lineage tracking
- Training data documentation
- Bias monitoring

### Article 11: Technical Documentation

**Requirement:** Documentation sufficient for authorities to assess compliance

**Architecture implication:**
- Auto-generated documentation from system
- Version control for all components
- Change tracking

### Article 12: Record-Keeping

**Requirement:** Automatic logging of events throughout system lifetime

**Architecture implication:**
- Comprehensive audit logging
- Log retention policies
- Query capabilities for investigations

### Article 13: Transparency

**Requirement:** Users must understand AI capabilities and limitations

**Architecture implication:**
- Explainability layer
- Confidence scores
- Clear communication of AI role

### Article 14: Human Oversight

**Requirement:** Humans can understand, oversee, and intervene

**Architecture implication:**
- Human-in-the-loop design
- Override capabilities
- Meaningful information for decisions

### Article 15: Accuracy & Robustness

**Requirement:** Appropriate levels of accuracy, robustness, cybersecurity

**Architecture implication:**
- Performance monitoring
- Regular evaluation
- Security controls

---

## Current Architecture (What Needs to Change)

```
┌─────────────────────────────────────────────────────────────────┐
│                    CURRENT ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                  │
│  │   Scan   │───▶│ AI Model │───▶│ Results  │                  │
│  │  Upload  │    │ (Azure)  │    │ Display  │                  │
│  └──────────┘    └──────────┘    └──────────┘                  │
│                       │                │                        │
│                       │                │                        │
│                  [No logging]    [Accept/Reject]               │
│                  [No explainability]  [No audit]               │
│                                                                 │
│  COMPLIANCE GAPS:                                               │
│  ✗ No risk management system                                   │
│  ✗ No data governance/lineage                                  │
│  ✗ No technical documentation                                  │
│  ✗ Minimal logging                                             │
│  ✗ No explainability                                           │
│  ✗ Human oversight is superficial                              │
│  ✗ No ongoing monitoring                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Exploration with AI Tutor

### Questions to Investigate

**EU AI Act specifics:**
- "What are the exact requirements for human oversight in EU AI Act?"
- "How do I implement Article 12 logging requirements technically?"
- "What documentation is required for high-risk AI systems?"

**Architecture patterns:**
- "How do I add explainability to an existing AI model?"
- "What's the best architecture for comprehensive audit logging?"
- "How do I design meaningful human oversight, not checkbox oversight?"

**Healthcare specific:**
- "What are specific compliance requirements for medical AI?"
- "How do I balance AI assistance with doctor autonomy?"
- "What's considered sufficient logging for medical AI decisions?"

---

## Hints

<details>
<summary>Hint 1: Compliance Layer Architecture (After 15 min)</summary>

Add a **compliance wrapper** around existing AI:

```
[Existing AI Model]
        │
        ▼
┌─────────────────────────────────────┐
│      COMPLIANCE LAYER               │
├─────────────────────────────────────┤
│  • Explainability Service           │
│  • Audit Logger                     │
│  • Risk Monitor                     │
│  • Human Oversight Interface        │
│  • Documentation Generator          │
└─────────────────────────────────────┘
        │
        ▼
[Compliant Output to Doctor]
```

This approach wraps compliance around existing AI without rebuilding.

</details>

<details>
<summary>Hint 2: Meaningful Human Oversight (After 25 min)</summary>

**Bad oversight (checkbox):**
- Doctor clicks "Approve" without reading
- No context for decision
- Time pressure forces rubber-stamping

**Good oversight (meaningful):**
- AI shows: What it found, why, confidence level
- AI shows: Similar cases, disagreement history
- Doctor has time to review
- Doctor can easily reject with feedback
- Rejections improve the system

**Architecture for meaningful oversight:**
- Confidence threshold: High confidence → show result
- Low confidence → force detailed review
- Track time spent reviewing (are doctors actually reviewing?)
- Track rejection rates and reasons

</details>

<details>
<summary>Hint 3: Audit Logging Specification (After 35 min)</summary>

**What to log (minimum):**
```json
{
  "timestamp": "2026-02-08T14:32:15Z",
  "scan_id": "uuid",
  "patient_id_hash": "anonymized",
  "model_version": "v2.3.1",
  "input_metadata": {
    "scan_type": "CT",
    "body_region": "chest",
    "image_quality_score": 0.94
  },
  "output": {
    "findings": ["nodule_detected"],
    "confidence": 0.87,
    "explanation": "...",
    "highlighted_regions": [...]
  },
  "human_oversight": {
    "doctor_id": "anonymized",
    "review_duration_seconds": 45,
    "decision": "accepted",
    "modifications": null,
    "feedback": null
  }
}
```

**Retention:** 10 years (medical records requirement)
**Query:** Must support investigation queries within 72 hours

</details>

<details>
<summary>Hint 4: Risk Management Integration (After 45 min)</summary>

**Continuous risk monitoring:**

1. **Performance drift detection:**
   - Track accuracy over time
   - Alert if accuracy drops > 5%

2. **Bias monitoring:**
   - Track outcomes by demographic
   - Alert if disparities detected

3. **Usage pattern anomalies:**
   - Track rejection rates by doctor
   - Alert if patterns suggest misuse

4. **Incident response:**
   - Clear escalation path
   - Root cause analysis template
   - Regulatory notification process

**Risk registry integration:**
- New risks logged automatically
- Regular risk review process
- Risk mitigation tracking

</details>

---

## Peer Review Prompts

Stress test your partner's compliance architecture:

1. An auditor asks to see all AI decisions for Patient X. Can you provide them?
2. The AI model is updated. How does documentation stay current?
3. A doctor claims they weren't given enough information to decide. Can you prove otherwise?
4. The system detects its own accuracy dropping. What happens?
5. A patient requests an explanation of why AI flagged their scan. Can you provide it?

---

## Connection to Tomorrow

Tomorrow: **Scale Architecture**. You'll take a POC with 50 users and
design for 10,000 users across 20 countries. Compliance at scale
adds another dimension of complexity.

---

*"Compliance is not about checking boxes. It's about building systems worthy of trust. In healthcare AI, that trust is literally life and death."*
