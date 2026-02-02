# Day 4: The Spaghetti Agent

## AI-SE Track - Week 1, Day 4

### The Situation: "Untangle This Mess"

You've inherited an AI agent codebase from a contractor. It "works" but:
- 2000 lines in a single file
- API keys hardcoded in 3 places  
- No tests
- Logging prints user data to console
- Try/catch blocks swallow all errors

**Challenge:** Create a refactoring plan that balances cleanup with delivery.

### Deliverables
1. Code Review Document - What's wrong and why it matters
2. Refactoring Roadmap - Prioritized cleanup tasks
3. Quick Wins - What can be fixed in 2 hours
4. Proposal - How to pitch refactoring to PM

### Code Smell Prioritization

| Smell | Risk | Fix Effort | Priority |
|-------|------|------------|----------|
| Hardcoded secrets | 🔴 Critical | Low | NOW |
| User data in logs | 🔴 Critical | Low | NOW |
| No error handling | 🟠 High | Medium | Week 1 |
| No tests | 🟠 High | High | Week 1-2 |
| Monolithic file | 🟡 Medium | High | Week 2+ |
