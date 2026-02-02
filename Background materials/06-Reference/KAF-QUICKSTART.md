# KAF (Kyndryl Agentic Framework) Quick Start

## What is KAF?

KAF is Kyndryl's framework for building production AI agents.

### Core Components

```
┌─────────────────────────────────────────┐
│              KAF Platform               │
├─────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │ Agent   │  │ Tool    │  │ Memory  │ │
│  │ Engine  │  │ Layer   │  │ Store   │ │
│  └─────────┘  └─────────┘  └─────────┘ │
├─────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │ LLM     │  │ Vector  │  │ Trust   │ │
│  │ Gateway │  │ Store   │  │ Layer   │ │
│  └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
```

## Quick Start

### 1. Create an Agent

```python
from kaf import Agent, Tool

# Define tools
search_tool = Tool(
    name="search_docs",
    description="Search internal documents",
    function=search_documents
)

# Create agent
agent = Agent(
    name="assistant",
    instructions="You help employees find information.",
    tools=[search_tool]
)
```

### 2. Run the Agent

```python
response = agent.run("What's our vacation policy?")
print(response.content)
```

### 3. Add Memory

```python
from kaf import MemoryStore

memory = MemoryStore(
    provider="azure_cosmos",
    connection_string=os.environ["COSMOS_CONNECTION"]
)

agent = Agent(
    name="assistant",
    memory=memory
)
```

## Key Patterns

### RAG Pattern
```
Query → Retrieve → Augment → Generate
```

### Tool Use Pattern
```
Query → Plan → Execute Tools → Synthesize
```

### Multi-Agent Pattern
```
Query → Orchestrator → [Agent A | Agent B] → Combine
```

## Best Practices

1. **Start simple** - Single agent with 2-3 tools
2. **Add guardrails early** - Input/output filtering
3. **Log everything** - You'll need it for debugging
4. **Test with real queries** - Synthetic tests aren't enough
5. **Monitor in production** - Track quality metrics

## Resources

- Full documentation: SharePoint/06-Reference/KAF-Documentation/
- Code examples: /ai-academy-common/kaf-quickstart/
- Support: #kaf-support on Teams
