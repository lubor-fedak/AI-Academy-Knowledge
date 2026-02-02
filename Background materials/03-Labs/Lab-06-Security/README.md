# Lab 06: AI Security Audit & Guardrails

## Overview

AI systems introduce unique security challenges - prompt injection, data leakage, hallucination risks, and more. In this lab, you'll conduct a security assessment of an AI system and implement defensive guardrails.

## Learning Objectives

By the end of this lab, you will be able to:
- Identify AI-specific security vulnerabilities
- Conduct red team testing on AI systems
- Implement input/output guardrails
- Configure rate limiting and abuse prevention
- Document security findings professionally

## Prerequisites

- Completed Labs 01-03
- Understanding of OWASP Top 10
- Familiarity with common attack patterns

## Time Estimate

**Total: 90 minutes**
- Threat modeling: 20 minutes
- Red team testing: 30 minutes
- Guardrail implementation: 30 minutes
- Documentation: 10 minutes

## Target Roles

- **Primary:** AI-SEC, AI-SE
- **Secondary:** All roles (security awareness)

## OWASP Top 10 for LLM Applications

1. Prompt Injection
2. Insecure Output Handling
3. Training Data Poisoning
4. Model Denial of Service
5. Supply Chain Vulnerabilities
6. Sensitive Information Disclosure
7. Insecure Plugin Design
8. Excessive Agency
9. Overreliance
10. Model Theft

## Success Criteria

- [ ] Threat model documented (STRIDE)
- [ ] 20+ prompt injection attempts tested
- [ ] Input guardrails implemented
- [ ] Output guardrails implemented
- [ ] Rate limiting configured
- [ ] Security assessment report completed
- [ ] Remediation recommendations provided

## Deliverables

1. **Threat model** (`threat_model.md`)
2. **Red team results** (`red_team_results.csv`)
3. **Guardrails code** (`guardrails.py`)
4. **Security report** (`security_assessment.md`)
5. **Reflection**
