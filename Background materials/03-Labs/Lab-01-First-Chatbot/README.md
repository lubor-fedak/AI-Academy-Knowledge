# Lab 01: Build Your First AI Chatbot

## Overview

In this lab, you'll build a functional AI chatbot from scratch using Gemini API. This is the foundation for all future AI work - understanding how to interact with LLMs programmatically.

## Learning Objectives

By the end of this lab, you will be able to:
- Set up a development environment for AI applications
- Make API calls to Gemini (or other LLM providers)
- Implement basic conversation flow with message history
- Handle errors and edge cases gracefully
- Understand token usage and cost implications

## Prerequisites

- Python 3.10+ installed
- Antigravity IDE access configured
- Gemini API key (from Google Partner credits)
- Basic Python knowledge

## Time Estimate

**Total: 90 minutes**
- Setup: 15 minutes
- Core implementation: 45 minutes
- Testing & polish: 20 minutes
- Reflection: 10 minutes

## Target Roles

- **Primary:** All roles (common foundation)
- This lab is required for everyone before role-specific tracks

## Architecture

```
┌─────────────────┐
│   User Input    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Chat Handler   │
│  - Validate     │
│  - Format       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Gemini API    │
│  - System Prompt│
│  - History      │
│  - Generation   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Response     │
│  - Parse        │
│  - Display      │
└─────────────────┘
```

## Success Criteria

- [ ] Chatbot responds to user queries
- [ ] Conversation history is maintained across turns
- [ ] System prompt defines chatbot personality/behavior
- [ ] Errors are handled gracefully (API failures, invalid input)
- [ ] Token usage is logged for each interaction
- [ ] Code is clean and documented

## Deliverables

1. **Working chatbot** (`chatbot.py`) - functional implementation
2. **Configuration file** (`config.py`) - API keys, model settings
3. **Test conversation** - screenshot or log of 5+ turn conversation
4. **Reflection** - brief notes on what you learned

## Tools & Resources

- **IDE:** Antigravity (recommended) or VS Code
- **API:** Gemini API via `google-generativeai` package
- **Docs:** https://ai.google.dev/docs

## Getting Started

1. Clone the starter code from `/starter/`
2. Configure your API key in `.env`
3. Follow instructions in `INSTRUCTIONS.md`
4. Test with provided sample queries
5. Extend with your own improvements

## Common Pitfalls

- Forgetting to handle API rate limits
- Not managing conversation history properly
- Exposing API keys in code (use environment variables!)
- Ignoring error handling until it's too late
