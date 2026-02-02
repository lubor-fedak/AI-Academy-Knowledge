# AI Software Engineer (AI-SE) Track Syllabus

## Role Overview

The AI Software Engineer builds the **production-grade platform** that powers AI solutions. AI-SEs focus on code quality, testing, CI/CD, and operational excellence.

This track describes a specialization within the Forward Deployed Engineer capability in the Consult role model.

### Core Responsibilities
- Build scalable, maintainable AI service architecture
- Implement CI/CD pipelines for AI systems
- Design testing strategies for non-deterministic systems
- Ensure observability and operational excellence

### Collaboration Points
| With | You Provide | You Receive |
|------|-------------|-------------|
| FDE | Production architecture, APIs | Demo code, requirements |
| AI-DS | Evaluation infrastructure | Model artifacts, metrics |
| AI-SEC | Secure code practices | Security requirements |
| AI-PM | Technical estimates, constraints | Priorities, timelines |

---

## Target Certifications

| Priority | Certification | Provider |
|----------|---------------|----------|
| **Primary** | Azure DevOps Engineer Expert | Microsoft |
| Secondary | AWS DevOps Engineer Professional | AWS |

---

## Week 2 Deep Dive

| Day | Topic | Situation | Deliverable |
|-----|-------|-----------|-------------|
| 6 | Clean Architecture | "Refactor the Monolith" | Service decomposition |
| 7 | Testing AI Systems | "Test This Agent" | Test suite |
| 8 | CI/CD for LLMs | "Pipeline is Broken" | Working pipeline |
| 9 | LLMOps & Monitoring | "Model Drift Detected" | Observability dashboard |
| 10 | Code Review | "PR Review Day" | Reviewed + reviewed by |

---

## Key Situations

### S-SE-01: "Test This Agent" (Day 7)

```yaml
Context: |
  FDE built an agent that "works". You need to prove it.
  The agent has non-deterministic outputs.
  How do you test something that gives different answers?
  
Challenge: |
  - Design test strategy for AI systems
  - Handle non-determinism
  - Create meaningful assertions
```

### S-SE-02: "Model Drift Detected" (Day 9)

```yaml
Context: |
  Production metrics show response quality dropping.
  Same prompts, worse outputs. What changed?
  
Challenge: |
  - Diagnose drift vs. other issues
  - Implement monitoring
  - Create alerting strategy
```

---

## AI Tutor Focus Areas

### Primary Challenge Questions
- "How will you test this?"
- "What happens when the API changes?"
- "How do you debug this in production?"
- "Where is the tight coupling?"

### Red Flags
- No tests
- Hardcoded secrets
- Ignoring error handling
- Monolithic design
