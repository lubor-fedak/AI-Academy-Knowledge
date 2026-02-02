# Lab 01: Mentor Notes

## Learning Objectives Recap

Students should emerge understanding:
- API-based LLM interaction patterns
- Importance of conversation history
- System prompt design basics
- Error handling for external services

## Common Struggles & Interventions

### Struggle: "My chatbot forgets everything"
**Cause:** Not implementing conversation history
**Intervention:** Ask "What does the model know about previous messages?" Guide them to realize LLMs are stateless.

### Struggle: "I keep getting rate limited"
**Cause:** Rapid testing without delays
**Intervention:** Discuss API rate limits. Suggest adding `time.sleep(1)` between calls during development.

### Struggle: "The response format is weird"
**Cause:** Not understanding response object structure
**Intervention:** Have them `print(type(response))` and explore the object. Guide to `response.text`.

### Struggle: "My system prompt doesn't work"
**Cause:** Unclear or conflicting instructions
**Intervention:** Review their prompt. Ask "If you were the AI, would you understand these instructions?"

## What Good Looks Like

**Excellent submission includes:**
- Clean, modular code (separate functions)
- Robust error handling
- Meaningful system prompt
- Token tracking
- Thoughtful reflection

**Acceptable submission includes:**
- Working chat loop
- Basic history management
- Some error handling
- Meets minimum requirements

**Needs improvement:**
- Hardcoded values
- No error handling
- Missing conversation history
- Incomplete reflection

## Debrief Talking Points

1. **Token economics:** How do tokens translate to cost? What's the impact of conversation history?

2. **Prompt engineering preview:** How did your system prompt affect behavior? What would you change?

3. **Real-world considerations:** What would you need to add for a production chatbot?

4. **Connection to RAG:** "What if you wanted the chatbot to answer questions about YOUR documents?" (Preview of Lab 02)

## Time Management

- If students finish early: Direct to extension challenges
- If students struggle: Focus on core requirements, skip extensions
- 15 min before end: Ensure everyone has submittable work

## Red Flags

- **Copying code without understanding:** Ask them to explain what each line does
- **Skipping error handling:** "What happens if the API fails?"
- **Ignoring token tracking:** "How much would this cost at scale?"
