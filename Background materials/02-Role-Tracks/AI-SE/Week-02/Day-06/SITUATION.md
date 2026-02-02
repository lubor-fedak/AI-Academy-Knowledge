# Day 6: Refactor the Monolith

## AI-SE Track - Week 2, Day 6

---

## The Situation

### "This Can't Scale"

```
The AI system started as a proof of concept. One Python file.
Then features got added. Then more features. Then production.

Now it's 3000 lines of spaghetti. And the PM wants:
- Support for a second LLM provider (fallback/cost optimization)
- Multiple document format support (PDF, Word, HTML)
- Caching layer for repeated queries
- Better error handling and retries

Every change touches everything. Tests are slow and flaky.
Developers are afraid to modify anything.

"We can add features faster if we refactor first."
"We don't have time to refactor, we need features now."

Sound familiar?
```

---

## Your Challenge

Decompose the monolith into clean service architecture that enables future changes.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Separation** | Clear boundaries between components |
| **Abstraction** | LLM provider can be swapped without changing business logic |
| **Testability** | Components can be unit tested independently |
| **Documentation** | Interfaces are clearly defined |

### Deliverables

1. **Architecture Diagram**
   - Service decomposition
   - Interface definitions
   - Data flow

2. **Refactored Code**
   - At least 3 separate modules/services
   - Clean interfaces between them
   - Unit tests for each

3. **Interface Contracts** (1 page)
   - Input/output specifications
   - Error handling contracts
   - Versioning strategy

---

## Micro-Context (5 minutes)

> Clean architecture isn't about perfection - it's about change. 
> Code that's easy to change beats code that's "perfect" but frozen.
>
> Key principles:
> - **Dependency Inversion** - Depend on abstractions, not concretions
> - **Single Responsibility** - One reason to change
> - **Interface Segregation** - Small, focused interfaces
>
> Hint: Start by identifying what's likely to CHANGE. That's where you need abstraction.

---

## Target Architecture

### From This (Monolith)
```
┌─────────────────────────────────────────┐
│           main.py (3000 lines)          │
│                                         │
│  - API endpoints                        │
│  - LLM calls (hardcoded to OpenAI)      │
│  - Document processing                  │
│  - Vector search                        │
│  - Caching (inline)                     │
│  - Error handling (try/except everywhere)│
└─────────────────────────────────────────┘
```

### To This (Clean Architecture)
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   API       │────▶│   Service   │────▶│   LLM       │
│   Layer     │     │   Layer     │     │   Adapter   │
└─────────────┘     └─────────────┘     └──────┬──────┘
                           │                   │
                    ┌──────┴──────┐      ┌─────┴─────┐
                    ▼             ▼      │ OpenAI    │
              ┌──────────┐  ┌──────────┐ │ Gemini    │
              │  Cache   │  │  Vector  │ │ Claude    │
              │  Layer   │  │  Store   │ └───────────┘
              └──────────┘  └──────────┘
```

---

## Step-by-Step Approach

### Step 1: Identify Boundaries

What are the natural seams in the code?
- **API Layer** - HTTP handling, request/response
- **Business Logic** - The actual "what it does"
- **LLM Integration** - Calls to external AI services
- **Document Processing** - Parsing, chunking
- **Storage** - Vector DB, cache

### Step 2: Define Interfaces

```python
# llm_adapter.py
from abc import ABC, abstractmethod

class LLMAdapter(ABC):
    @abstractmethod
    def complete(self, prompt: str, **kwargs) -> str:
        pass
    
    @abstractmethod
    def embed(self, text: str) -> list[float]:
        pass

class OpenAIAdapter(LLMAdapter):
    def complete(self, prompt: str, **kwargs) -> str:
        # OpenAI-specific implementation
        pass

class GeminiAdapter(LLMAdapter):
    def complete(self, prompt: str, **kwargs) -> str:
        # Gemini-specific implementation
        pass
```

### Step 3: Extract and Test

1. Extract one component at a time
2. Write tests BEFORE refactoring
3. Verify behavior is unchanged
4. Repeat

---

## Common Refactoring Patterns

### Pattern 1: Adapter Pattern (for external services)
```python
# Before: Hardcoded OpenAI calls everywhere
response = openai.chat.completions.create(...)

# After: Abstracted behind adapter
response = self.llm_adapter.complete(prompt)
```

### Pattern 2: Repository Pattern (for data access)
```python
# Before: Direct database calls in business logic
results = vector_db.search(query)

# After: Repository abstraction
results = self.document_repository.find_similar(query)
```

### Pattern 3: Strategy Pattern (for algorithms)
```python
# Before: If/else for different chunking methods
if method == "paragraph":
    chunks = split_by_paragraph(text)
elif method == "sentence":
    chunks = split_by_sentence(text)

# After: Strategy pattern
chunker = ChunkerFactory.create(method)
chunks = chunker.chunk(text)
```

---

## Hints

<details>
<summary>Hint 1: Where to start (Click after 10 min)</summary>

Start with the EXTERNAL dependencies:
1. LLM provider (most likely to change)
2. Vector database (might switch vendors)
3. Document parsers (need to add formats)

These are the "edges" of your system where change is most likely.
</details>

<details>
<summary>Hint 2: Testing strategy (Click after 25 min)</summary>

For each component:
1. Write characterization tests FIRST (capture current behavior)
2. Extract the component
3. Verify tests still pass
4. Add proper unit tests

Don't skip the first step - it's your safety net.
</details>

<details>
<summary>Hint 3: Dependency injection (Click after 40 min)</summary>

Make dependencies explicit:

```python
# Bad: Creates its own dependencies
class RAGService:
    def __init__(self):
        self.llm = OpenAI()  # Hardcoded!
        
# Good: Dependencies injected
class RAGService:
    def __init__(self, llm: LLMAdapter, vector_store: VectorStore):
        self.llm = llm
        self.vector_store = vector_store
```
</details>

---

## Self-Study Assignment (90 min)

1. **Create architecture diagram** - Target state with interfaces (20 min)
2. **Extract LLM adapter** - Abstract away the LLM provider (40 min)
3. **Add second provider** - Implement Gemini adapter (20 min)
4. **Write tests** - Unit tests for adapters (10 min)

### Stretch Goals
- Implement adapter for caching layer
- Add circuit breaker pattern for external calls
- Create factory for runtime provider selection
