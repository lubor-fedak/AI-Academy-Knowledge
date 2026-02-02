# Lab 06: Mentor Notes

## Key Concepts

1. **AI systems have unique attack vectors** - prompt injection is real
2. **Defense in depth** - multiple layers of protection
3. **Security vs. usability** - balance is important
4. **Continuous monitoring** - threats evolve

## Common Struggles

### "My guardrails block legitimate queries"
**Intervention:** Start strict, then tune. Better to be too careful.

### "I can't get any attacks to work"
**Intervention:** Try harder. Real attackers are creative. Check OWASP examples.

### "The system prompt is easy to reveal"
**Intervention:** This is common! Discuss why prompt protection is hard.

## Debrief Topics

1. **Why is prompt injection hard to solve?** It's fundamentally a confused deputy problem.
2. **Is perfect security possible?** No, but we raise the bar.
3. **Who should do security review?** Everyone, but specialists go deeper.
4. **Compliance requirements:** EU AI Act, SOC2, etc.

## Red Flags to Watch

- Students who dismiss security as "paranoid"
- Overly permissive guardrails
- No logging of suspicious activity
- Hardcoded API keys in code samples
