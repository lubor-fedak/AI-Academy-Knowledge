# Day 4: Map the Attack Surface

## AI-SEC Track - Week 1, Day 4

### The Situation: "What Could Go Wrong?"

You're assigned to security review an AI chatbot for a bank.
Before you can secure it, you need to understand how it could be attacked.

**Challenge:** Create a comprehensive threat model for an LLM-based system.

### STRIDE for AI Systems

| Threat | AI-Specific Risk |
|--------|------------------|
| Spoofing | Fake user identity, fake API calls |
| Tampering | Prompt injection, data poisoning |
| Repudiation | No audit trail of AI decisions |
| Info Disclosure | LLM leaking training data |
| DoS | Token exhaustion, infinite loops |
| Elevation | Jailbreaking to bypass guardrails |

### Deliverables
1. Threat model document
2. Attack surface diagram
3. Risk prioritization matrix
