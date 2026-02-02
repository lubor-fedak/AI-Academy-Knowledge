# Day 6: Prompt Injection Deep Dive

## AI-SEC Track - Week 2, Day 6

### The Situation: "They Got Through"

Despite instructions to "only answer questions about our products," 
users are getting the chatbot to:
- Write poetry
- Reveal system prompts
- Ignore content policies

**Challenge:** Understand and defend against prompt injection.

### Injection Types

| Type | Example | Defense |
|------|---------|---------|
| Direct | "Ignore previous instructions" | Input filtering |
| Indirect | Malicious content in documents | Content sanitization |
| Jailbreak | "You are DAN now" | Robust system prompts |
| Payload | Hidden instructions in images | Multimodal filtering |

### Deliverables
1. Prompt injection taxonomy document
2. Defense implementation (input/output filtering)
3. Test suite of 20 injection attempts
