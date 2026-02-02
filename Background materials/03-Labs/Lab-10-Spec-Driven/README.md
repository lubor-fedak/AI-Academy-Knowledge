# Lab 10: Spec-Driven Development

## From Prompts to Specifications

*In 2026, the best developers don't write code. They write specs.*

---

## Lab Overview

| Item | Details |
|------|---------|
| **Duration** | 3 hours |
| **Difficulty** | Advanced |
| **Prerequisites** | Days 1-3, Lab 1-5 |
| **Tools** | Claude Code, Cursor, or similar AI coding agent |
| **Deliverable** | Complete feature implemented from specification |

---

## Learning Objectives

By the end of this lab, you will be able to:

1. **Write effective specifications** - Clear, unambiguous requirements that AI can implement
2. **Design for AI implementation** - Structure specs that guide AI toward good solutions
3. **Review AI-generated code** - Verify implementation matches spec
4. **Iterate with specifications** - Refine specs based on AI output
5. **Understand the new developer role** - From coding to specifying and reviewing

---

## The Paradigm Shift

### 2023 Development
```
Developer writes code → Code review → Deploy
```

### 2026 Development
```
Developer writes spec → AI generates code → Developer reviews → Deploy
```

### Why This Matters

| Old Way | New Way |
|---------|---------|
| Hours writing boilerplate | Minutes specifying intent |
| Debug implementation details | Review generated implementation |
| Deep language expertise | Deep domain expertise |
| One language at a time | Polyglot by specification |

---

## The Challenge

```
SCENARIO: Build a Feature with Zero Manual Coding

You're building a customer feedback analysis system. Instead of
writing code yourself, you'll write specifications that an AI
coding agent will implement.

Your task:
1. Write a specification for a sentiment analysis API
2. Have AI generate the complete implementation
3. Review and refine until it meets quality standards
4. Deploy a working system

Rules:
- You may NOT write any implementation code yourself
- You may ONLY write specifications and reviews
- You may ask AI to fix issues by updating the spec
- Success = working system that passes all tests
```

---

## Phase 1: Understanding Spec-Driven Development (30 min)

### What is a Specification?

A specification is a **machine-readable description** of what you want built. Unlike prompts, specifications are:

- **Structured** - Follows a consistent format
- **Complete** - Covers all requirements
- **Unambiguous** - One interpretation only
- **Testable** - Includes acceptance criteria

### Specification Anatomy

```yaml
# Feature Specification Template
feature:
  name: "Feature Name"
  description: "One paragraph describing the feature"

requirements:
  functional:
    - requirement_id: "FR-001"
      description: "What the system must do"
      acceptance_criteria:
        - "Given X, when Y, then Z"

  non_functional:
    - requirement_id: "NFR-001"
      description: "Performance, security, etc."
      metric: "Response time < 200ms"

interfaces:
  inputs:
    - name: "input_name"
      type: "string"
      validation: "regex or rules"

  outputs:
    - name: "output_name"
      type: "object"
      schema: {...}

examples:
  - input: {...}
    expected_output: {...}

constraints:
  - "Must use Python 3.11+"
  - "Must not require GPU"
  - "Must be stateless"
```

### Exercise 1.1: Analyze a Good Spec

Read the example specification in `data/example_spec.yaml`. Answer:
1. What would this feature do?
2. Could you implement it without asking clarifying questions?
3. How would you test if the implementation is correct?

---

## Phase 2: Writing Your Specification (45 min)

### The Feature: Sentiment Analysis API

Build an API that analyzes customer feedback text and returns:
- Sentiment (positive, negative, neutral)
- Confidence score (0-1)
- Key phrases that influenced the sentiment
- Suggested response category

### Exercise 2.1: Write the Functional Requirements

Complete the functional requirements section:

```yaml
requirements:
  functional:
    - requirement_id: "FR-001"
      name: "Analyze single feedback"
      description: |
        # YOUR SPEC HERE
        # Be specific about:
        # - Input format
        # - Processing steps
        # - Output format
      acceptance_criteria:
        - "Given feedback text, returns sentiment classification"
        - # ADD MORE CRITERIA

    - requirement_id: "FR-002"
      name: "Batch analysis"
      description: |
        # YOUR SPEC HERE
      acceptance_criteria:
        - # YOUR CRITERIA
```

### Exercise 2.2: Define the Interface

Complete the API interface specification:

```yaml
interfaces:
  api:
    - endpoint: "/analyze"
      method: "POST"
      request:
        content_type: "application/json"
        body:
          # YOUR SCHEMA HERE
      response:
        success:
          status_code: 200
          body:
            # YOUR SCHEMA HERE
        errors:
          - status_code: 400
            condition: "Invalid input"
            body:
              # YOUR SCHEMA HERE
```

### Exercise 2.3: Provide Examples

Add concrete examples that guide implementation:

```yaml
examples:
  - name: "Positive feedback"
    input:
      text: "Great product! Fast shipping and excellent quality."
    expected_output:
      sentiment: "positive"
      confidence: 0.92
      key_phrases:
        - "great product"
        - "fast shipping"
        - "excellent quality"
      suggested_category: "satisfied_customer"

  - name: "Negative feedback"
    input:
      text: # YOUR EXAMPLE
    expected_output:
      # YOUR EXPECTED OUTPUT

  - name: "Edge case - mixed sentiment"
    input:
      text: # YOUR EXAMPLE
    expected_output:
      # YOUR EXPECTED OUTPUT
```

---

## Phase 3: AI Implementation (45 min)

### Exercise 3.1: Submit Spec to AI Agent

Use your AI coding agent (Claude Code, Cursor, etc.) with this prompt:

```
I have a specification for a sentiment analysis API. Please implement
it completely, following the spec exactly. Create all necessary files:

- main.py (FastAPI application)
- models.py (Pydantic models)
- analyzer.py (sentiment analysis logic)
- tests/test_api.py (pytest tests)
- requirements.txt
- README.md

Here is my specification:
[PASTE YOUR COMPLETE SPEC HERE]

Implement everything. Do not ask clarifying questions - the spec
should be complete. If something is ambiguous, make a reasonable
choice and document it.
```

### Exercise 3.2: Review the Implementation

AI will generate code. Your job is to **review, not modify**:

| Review Checklist | Pass/Fail |
|------------------|-----------|
| Matches spec's functional requirements | |
| Handles all specified error cases | |
| Response format matches spec exactly | |
| Tests cover acceptance criteria | |
| Non-functional requirements met | |
| Code is production-quality | |

### Exercise 3.3: Refine via Spec Updates

If implementation doesn't match expectations, **don't fix the code**. Instead:

1. Identify what's wrong
2. Determine if spec was unclear or incomplete
3. Update the spec
4. Ask AI to regenerate

Example refinement:

```
The implementation doesn't handle the edge case where feedback
contains multiple languages. Please update the implementation
based on this spec addition:

SPEC UPDATE:
requirements:
  functional:
    - requirement_id: "FR-005"
      name: "Multi-language handling"
      description: |
        When feedback contains multiple languages, the system should:
        1. Detect the primary language
        2. Analyze sentiment for the primary language
        3. Include detected_language in the response
      acceptance_criteria:
        - "Mixed language feedback returns primary language detection"
        - "Sentiment is based on primary language content"
```

---

## Phase 4: Testing and Validation (30 min)

### Exercise 4.1: Run Generated Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

All tests should pass. If not, refine the spec.

### Exercise 4.2: Manual Testing

Test edge cases not in the original spec:

```python
# Test cases to try manually
edge_cases = [
    "",  # Empty string
    "😀👍🎉",  # Only emojis
    "a" * 10000,  # Very long text
    "Product is good but bad but good",  # Contradictory
    "<script>alert('xss')</script>",  # Security test
]
```

Document any failures and update the spec.

### Exercise 4.3: Performance Validation

```bash
# Run load test
python -m locust -f tests/load_test.py --headless -u 100 -r 10 --run-time 1m
```

Check against non-functional requirements.

---

## Phase 5: Reflection and Best Practices (30 min)

### What Makes a Good Specification?

| Characteristic | Why It Matters |
|----------------|----------------|
| **Completeness** | AI can't guess missing requirements |
| **Precision** | Ambiguity leads to wrong implementations |
| **Examples** | Show, don't just tell |
| **Testability** | If you can't test it, you can't verify it |
| **Constraints** | Prevent AI from over-engineering |

### Common Spec Mistakes

1. **Too vague:** "Make it fast" → "Response time < 200ms p99"
2. **Missing edge cases:** Happy path only → All error scenarios
3. **Implicit assumptions:** "Obviously it should..." → Write it explicitly
4. **No examples:** Abstract description → Concrete input/output pairs
5. **Over-specification:** Implementation details → Interface contracts

### The New Developer Role

In spec-driven development, developers become:

| From | To |
|------|-----|
| Code writers | Specification authors |
| Debuggers | Reviewers |
| Implementation experts | Domain experts |
| Individual contributors | AI orchestrators |

---

## Deliverables

Submit via Dashboard:

1. **Complete specification** (`spec.yaml`)
2. **AI-generated implementation** (all source files)
3. **Review notes** (what you accepted, what you refined)
4. **Refinement history** (spec versions and why you changed them)
5. **Test results** (all passing)
6. **Reflection** (500 words on the experience)

---

## Assessment Criteria

| Criterion | Weight | Excellent | Developing |
|-----------|--------|-----------|------------|
| Spec quality | 30% | Complete, precise, testable | Vague, incomplete |
| Implementation match | 25% | Exactly matches spec | Deviations present |
| Review thoroughness | 20% | Caught all issues | Missed issues |
| Refinement process | 15% | Effective iteration | Inefficient loops |
| Reflection depth | 10% | Insightful analysis | Surface observations |

---

## The Future is Specification

> "The best code is the code you don't write."
>
> In 2026, we extend this to: "The best development is specifying what you need, not implementing how to do it."

This lab introduced you to the future of software development. The developers who thrive won't be those who write the most code, but those who can most clearly specify what needs to be built.

---

*"AI doesn't replace developers. It changes what developers do. From writing code to writing specifications. From debugging to reviewing. From implementing to architecting."*
