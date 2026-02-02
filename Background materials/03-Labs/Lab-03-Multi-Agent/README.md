# Lab 03: Build a Multi-Agent System

## Overview

Multi-agent systems allow complex tasks to be broken down and handled by specialized agents. In this lab, you'll build an orchestrated multi-agent system where different agents handle different types of requests.

## Learning Objectives

By the end of this lab, you will be able to:
- Design agent architectures for complex workflows
- Implement agent-to-agent communication
- Build an orchestrator that routes requests
- Handle state management across agents
- Debug multi-agent interactions

## Prerequisites

- Completed Lab 01 and Lab 02
- Understanding of tool-use patterns
- Basic async Python knowledge

## Time Estimate

**Total: 120 minutes**
- Architecture design: 20 minutes
- Agent implementation: 40 minutes
- Orchestrator: 30 minutes
- Testing & debugging: 30 minutes

## Target Roles

- **Primary:** FDE, AI-SE
- **Secondary:** AI-PM (for understanding)

## Architecture

```
                    ┌─────────────────┐
                    │   User Query    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Orchestrator  │
                    │   (Router)      │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
    ┌────────────┐    ┌────────────┐    ┌────────────┐
    │   Policy   │    │  Technical │    │   General  │
    │   Agent    │    │   Agent    │    │   Agent    │
    │            │    │            │    │            │
    │  RAG:HR    │    │  RAG:Tech  │    │  No RAG    │
    └────────────┘    └────────────┘    └────────────┘
```

## The Scenario

You're building a company assistant that handles three types of queries:
1. **HR/Policy questions** → Routed to Policy Agent (uses HR document RAG)
2. **Technical questions** → Routed to Technical Agent (uses Tech docs RAG)
3. **General questions** → Routed to General Agent (no RAG, general knowledge)

## Success Criteria

- [ ] Orchestrator correctly routes 90%+ of queries
- [ ] Specialized agents provide accurate, grounded answers
- [ ] System handles ambiguous queries gracefully
- [ ] Multi-step queries work (e.g., "What's the leave policy and how do I deploy to Azure?")
- [ ] Clear logging shows agent interactions
- [ ] Error handling for agent failures

## Deliverables

1. **Multi-agent system** (`multi_agent.py`)
2. **Architecture diagram** (showing agent interactions)
3. **Routing logic documentation**
4. **Test results** (20 queries with routing analysis)
5. **Reflection**
