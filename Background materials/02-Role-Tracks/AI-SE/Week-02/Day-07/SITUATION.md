# Day 7: CI/CD for AI

## AI-SE Track - Week 2, Day 7 (Tuesday)

---

## The Situation

### "The Pipeline is Broken"

```
Every merge to main breaks something. The team does 
"Deployment Friday" because nobody wants to deploy 
on Monday and deal with issues all week.

The current "process":
1. Developer says "it works on my machine"
2. Someone manually runs tests (sometimes)
3. Someone manually deploys (no rollback plan)
4. Everyone hopes for the best

Last week, a broken deployment went unnoticed for 3 hours.
Customers were getting hallucinated responses because 
a prompt change wasn't tested.

"We need CI/CD" says the PM. "And we need it yesterday."
```

---

## Your Challenge

Build a CI/CD pipeline that makes deployment boring and safe.

### Deliverables

1. **Pipeline Definition** (GitHub Actions or Azure DevOps)
   - Lint, test, build stages
   - Deployment to staging then prod
   - Automatic rollback on failure

2. **Test Suite** that runs in CI
   - Unit tests
   - Integration tests
   - LLM output validation

3. **Deployment Runbook**
   - How to deploy
   - How to rollback
   - How to verify

---

## Pipeline Stages

```yaml
name: AI System CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run linters
        run: |
          pip install ruff
          ruff check .

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: |
          pip install pytest
          pytest tests/ --tb=short

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build container
        run: docker build -t myapp:${{ github.sha }} .

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy to staging
        run: |
          az containerapp update --name myapp-staging ...

  smoke-test:
    needs: deploy-staging
    runs-on: ubuntu-latest
    steps:
      - name: Run smoke tests
        run: pytest tests/smoke/ --base-url=$STAGING_URL

  deploy-prod:
    needs: smoke-test
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy to production
        run: |
          az containerapp update --name myapp-prod ...
```

---

## Testing AI Systems in CI

### Challenge: Non-Deterministic Outputs

```python
# DON'T: Exact string match
def test_response():
    response = llm.complete("What is 2+2?")
    assert response == "The answer is 4"  # Will fail randomly

# DO: Semantic validation
def test_response():
    response = llm.complete("What is 2+2?")
    assert "4" in response  # More robust
    assert len(response) < 500  # Sanity check
```

### Test Categories for AI

| Type | What to Test | Example |
|------|-------------|---------|
| Unit | Deterministic code | Chunking function |
| Contract | API shape | Response has required fields |
| Semantic | Meaning preserved | Contains expected keywords |
| Golden | Known good cases | Regression tests |
| Cost | Token limits | Response under budget |

---

## Self-Study Assignment (90 min)

1. **Create pipeline** - Working CI/CD configuration (45 min)
2. **Add tests** - At least 10 tests that run in CI (30 min)
3. **Document** - Deployment runbook (15 min)
