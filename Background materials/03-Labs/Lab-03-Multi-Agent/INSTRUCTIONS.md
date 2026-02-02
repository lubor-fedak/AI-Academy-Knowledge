# Lab 03: Instructions

## Phase 1: Architecture Design (20 min)

### Step 1.1: Define Your Agents

Before coding, design your agent architecture:

**Orchestrator Agent:**
- Purpose: Classify queries and route to appropriate agent
- Input: User query
- Output: Agent selection + reasoning

**Policy Agent:**
- Purpose: Answer HR/policy questions
- Knowledge: Company handbook, leave policies, expenses
- Tools: RAG over HR documents

**Technical Agent:**
- Purpose: Answer technical/platform questions
- Knowledge: KAF docs, deployment guides, API references
- Tools: RAG over technical documents

**General Agent:**
- Purpose: Handle general queries, chitchat, out-of-scope
- Knowledge: General LLM knowledge
- Tools: None (pure LLM)

### Step 1.2: Define Routing Logic

Create a classification scheme:

```python
ROUTING_CATEGORIES = {
    "policy": ["leave", "vacation", "expense", "HR", "salary", "benefits", "policy"],
    "technical": ["deploy", "code", "API", "error", "bug", "KAF", "Azure", "install"],
    "general": ["hello", "thanks", "weather", "joke", "help"]
}
```

**Question:** How will you handle queries that match multiple categories?

### Step 1.3: Draw Your Architecture

Create a diagram showing:
- Agent communication flow
- Shared vs. isolated state
- Error handling paths

---

## Phase 2: Agent Implementation (40 min)

### Step 2.1: Base Agent Class

Create a reusable agent structure:

```python
class Agent:
    def __init__(self, name: str, system_prompt: str, tools: list = None):
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools or []
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def run(self, query: str, context: dict = None) -> dict:
        """Execute agent with query and optional context."""
        # TODO: Implement
        pass
```

### Step 2.2: Policy Agent

```python
policy_agent = Agent(
    name="PolicyAgent",
    system_prompt="""You are an HR policy expert for Kyndryl.
    Answer questions about company policies based ONLY on the provided context.
    If information is not in the context, say "I don't have that policy information."
    Always cite which policy document you're referencing.""",
    tools=[rag_search_hr]
)
```

### Step 2.3: Technical Agent

```python
technical_agent = Agent(
    name="TechnicalAgent",
    system_prompt="""You are a technical expert for the Kyndryl AI Platform.
    Answer questions about KAF, deployment, APIs, and technical issues.
    Provide code examples when helpful.
    If you don't know, suggest where to find the answer.""",
    tools=[rag_search_tech]
)
```

### Step 2.4: General Agent

```python
general_agent = Agent(
    name="GeneralAgent",
    system_prompt="""You are a helpful assistant for Kyndryl employees.
    Handle general questions, greetings, and out-of-scope queries.
    If a question should go to Policy or Technical agents, say so.""",
    tools=[]
)
```

---

## Phase 3: Orchestrator Implementation (30 min)

### Step 3.1: Router Function

The orchestrator needs to:
1. Analyze the query
2. Decide which agent should handle it
3. Pass the query to that agent
4. Return the result

```python
class Orchestrator:
    def __init__(self):
        self.agents = {
            "policy": policy_agent,
            "technical": technical_agent,
            "general": general_agent
        }
        self.router_model = genai.GenerativeModel("gemini-1.5-flash")
    
    def route(self, query: str) -> str:
        """Determine which agent should handle the query."""
        routing_prompt = f"""
        Classify this query into one category: policy, technical, or general.
        
        - policy: HR, leave, expenses, benefits, company rules
        - technical: code, deployment, APIs, errors, KAF platform
        - general: greetings, chitchat, unclear, other
        
        Query: {query}
        
        Respond with ONLY the category name.
        """
        # TODO: Implement routing
        pass
    
    def run(self, query: str) -> dict:
        """Route query to appropriate agent and return result."""
        # TODO: Implement full flow
        pass
```

### Step 3.2: Multi-Agent Queries

Some queries need multiple agents:
- "What's the leave policy and how do I set up the dev environment?"

Implement a strategy for:
1. Detecting multi-part queries
2. Routing parts to different agents
3. Combining results

### Step 3.3: Conversation State

Track conversation across turns:
```python
class ConversationState:
    def __init__(self):
        self.history = []
        self.current_agent = None
        self.context = {}
```

---

## Phase 4: Testing & Debugging (30 min)

### Test Queries

Test these 20 queries and record routing + answers:

**Policy (should route to PolicyAgent):**
1. How many vacation days do I get?
2. What's the expense policy for hotels?
3. Who approves my leave request?
4. Can I work from home?
5. What happens to unused sick days?

**Technical (should route to TechnicalAgent):**
6. How do I deploy to Azure Container Apps?
7. What environment variables does KAF need?
8. How do I check the logs?
9. My agent keeps crashing, what should I check?
10. How do I use the embedding API?

**General (should route to GeneralAgent):**
11. Hello!
12. Thanks for your help
13. What's the weather like?
14. Tell me a joke
15. What can you help me with?

**Ambiguous (interesting routing decisions):**
16. I need help (policy? technical? general?)
17. Where do I find the documentation? (could be either)
18. How do I submit something? (expense? code? leave?)
19. What are the rules? (policy rules? coding rules?)
20. Who do I contact? (HR? IT? depends)

### Debug Logging

Add logging to trace agent interactions:
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In orchestrator
logger.info(f"Query: {query}")
logger.info(f"Routed to: {agent_name}")
logger.info(f"Response: {response[:100]}...")
```

---

## Extension Challenges

1. **Confidence scoring:** Route to multiple agents if confidence is low
2. **Agent memory:** Let agents remember previous interactions
3. **Parallel execution:** Run multiple agents simultaneously
4. **Fallback chain:** If one agent fails, try another
5. **Human escalation:** Detect when to escalate to human

---

## Submission

Upload to SharePoint `/07-Submissions/Labs/Lab-03/`:
- `multi_agent.py`
- `architecture.md` (with diagram)
- `test_results.csv` (20 queries with analysis)
- `REFLECTION.md`
