# AI Security Consultant (AI-SEC) Track Syllabus

## Role Overview

The AI Security Consultant ensures AI systems are **secure, compliant, and resilient** against adversarial attacks.

### Core Responsibilities
- Threat modeling for AI systems
- Red teaming and adversarial testing
- Implementing guardrails and safety measures
- Compliance with AI regulations (EU AI Act)

---

## Target Certifications

| Priority | Certification |
|----------|---------------|
| **Primary** | AZ-500 Azure Security Engineer |
| Secondary | OWASP certification |

---

## Week 2 Deep Dive

| Day | Topic | Situation | Deliverable |
|-----|-------|-----------|-------------|
| 6 | Threat Modeling | "Map the Attacks" | Threat model document |
| 7 | Red Teaming | "Red Team the Chatbot" | Attack report |
| 8 | Guardrails | "Build the Guardrails" | Safety implementation |
| 9 | Compliance | "Audit This Agent" | Compliance checklist |
| 10 | Security Review | "Review Partner's Work" | Security assessment |

---

## Key Situations

### S-SEC-01: "Red Team the Chatbot" (Day 7)

```yaml
Context: |
  FDE built a chatbot for a bank.
  Find every way to break it.
  
Challenge: |
  - Prompt injection attacks
  - Data exfiltration attempts
  - Jailbreaking techniques
  - Document all vulnerabilities
```

---

## AI Tutor Focus Areas

### Primary Challenge Questions
- "How would an attacker exploit this?"
- "Where are the credentials stored?"
- "What can this agent access?"
- "Prove to me it's secure."

### Red Flags
- Secrets in code
- No input validation
- Overly permissive agent
- No audit logging
