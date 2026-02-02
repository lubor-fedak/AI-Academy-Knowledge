# AI Platform Technical Guide

## Getting Started with KAF

The Kyndryl Agentic Framework (KAF) is our standard platform for building AI agents.

### Installation

```bash
pip install kaf-framework
```

### Basic Usage

```python
from kaf import Agent, Tool

agent = Agent(
    name="my_agent",
    model="gemini-1.5-flash",
    tools=[search_tool, calculator_tool]
)

response = agent.run("What is 2 + 2?")
```

## Deployment

### Azure Container Apps

1. Build Docker image
2. Push to Azure Container Registry
3. Deploy to Container Apps
4. Configure environment variables

### Environment Variables

Required variables:
- `GEMINI_API_KEY`: Your API key
- `AZURE_STORAGE_CONNECTION`: Storage connection string
- `LOG_LEVEL`: DEBUG, INFO, WARNING, ERROR

## Monitoring

### Logging
All logs are sent to Azure Application Insights. Use structured logging:

```python
logger.info("Processing request", extra={"user_id": "123", "action": "search"})
```

### Metrics
Track these KPIs:
- Response latency (p50, p95, p99)
- Token usage per request
- Error rate
- User satisfaction score
