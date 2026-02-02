# Day 5: Test the Untestable

## AI-SE Track - Week 1, Day 5

### The Situation: "How Do You Test Randomness?"

Your tech lead asks: "Where are the tests?"
You explain: "It's an LLM. The outputs are non-deterministic."
She replies: "Figure it out. We don't ship untested code."

**Challenge:** Design and implement a testing strategy for non-deterministic AI.

### Testing Approaches

| Approach | What It Tests | Example |
|----------|--------------|---------|
| Deterministic parts | Non-AI code | Unit test chunking |
| Contract testing | Structure | Response has fields |
| Property-based | Invariants | Length < 1000 |
| Semantic similarity | Meaning | Embedding distance |
| Evaluation metrics | Quality | Accuracy > 85% |

### Week 1 Checkpoint
- Code review document
- Testing strategy document
- Working test suite (10+ tests)
- CI pipeline configuration
