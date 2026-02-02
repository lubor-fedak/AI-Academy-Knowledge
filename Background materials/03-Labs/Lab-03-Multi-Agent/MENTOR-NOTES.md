# Lab 03: Mentor Notes

## Key Concepts

1. **Orchestration patterns:** Router, chain, parallel
2. **Agent specialization:** Why split into multiple agents?
3. **State management:** Shared vs. isolated context
4. **Failure handling:** What if an agent fails?

## Common Struggles

### "My router always picks the same agent"
**Cause:** Weak routing prompt or biased training
**Intervention:** Have them test routing in isolation. Print classification reasoning.

### "Agents don't share context"
**Cause:** No state management between agents
**Intervention:** Discuss: Should they share context? When yes/no?

### "Multi-part queries fail"
**Cause:** No query decomposition logic
**Intervention:** Start simple - just handle one agent. Add multi-agent later.

## Architecture Discussion Points

1. **When to use multi-agent:** Complex domains, different data sources, specialized skills
2. **When NOT to:** Simple use cases, adds latency, harder to debug
3. **Orchestration vs. choreography:** Central router vs. agents calling each other

## What Good Looks Like

- Clean separation of concerns
- Good routing accuracy (>85%)
- Clear logging and traceability
- Handles edge cases gracefully

## Connection to Real Projects

"In production systems, you might have:
- Customer support agent
- Sales inquiry agent
- Technical support agent
- Billing agent
All coordinated by an orchestrator."
