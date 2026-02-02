# AI Academy Troubleshooting Guide

## Common Issues and Solutions

---

## Environment Issues

### "Can't access Antigravity"
**Symptom:** Login fails or workspace won't load

**Solutions:**
1. Clear browser cache and cookies
2. Try incognito/private window
3. Check VPN is connected
4. Contact IT if persists

### "API key not working"
**Symptom:** 401 Unauthorized errors

**Solutions:**
1. Check key is correctly copied (no extra spaces)
2. Verify key hasn't expired
3. Check quota hasn't been exceeded
4. Regenerate key if needed

### "Azure deployment fails"
**Symptom:** Container won't start

**Solutions:**
1. Check Azure CLI is logged in: `az account show`
2. Verify resource group permissions
3. Check container logs: `az containerapp logs show`
4. Ensure secrets are in Key Vault

---

## Code Issues

### "RAG returns wrong chunks"
**Symptom:** Retrieved content doesn't match query

**Solutions:**
1. Check embedding model matches between index and query
2. Verify chunks contain expected content
3. Try different chunking strategy
4. Increase number of retrieved chunks (K)

### "Agent loops forever"
**Symptom:** Agent keeps calling tools without finishing

**Solutions:**
1. Add maximum iteration limit
2. Check stop conditions in orchestrator
3. Add timeout to tool calls
4. Review agent prompt for clear termination criteria

### "LLM hallucinating"
**Symptom:** Answers not grounded in provided context

**Solutions:**
1. Strengthen system prompt: "ONLY use provided context"
2. Add explicit "I don't know" instructions
3. Implement fact-checking layer
4. Reduce temperature parameter

---

## Performance Issues

### "Responses too slow"
**Symptom:** >10 second response time

**Solutions:**
1. Use streaming responses
2. Cache frequent queries
3. Optimize chunk retrieval (fewer, better chunks)
4. Use faster model for simple queries

### "Hitting rate limits"
**Symptom:** 429 Too Many Requests

**Solutions:**
1. Implement exponential backoff
2. Add request queuing
3. Cache repeated queries
4. Request quota increase

---

## Getting Help

1. **AI Tutor:** First stop for conceptual questions
2. **Teams Channel:** #ai-academy-help for quick questions
3. **Mentor Office Hours:** For complex issues
4. **This Guide:** For common technical problems

When asking for help, include:
- What you're trying to do
- What you tried
- Error message (exact text)
- Code snippet (if relevant)
