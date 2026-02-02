# Lab 05: Instructions

## Phase 1: Metrics Definition (20 min)

### Step 1.1: Choose Your Metrics

For RAG systems, common metrics include:

**Retrieval Metrics:**
- **Precision@K:** What % of retrieved docs are relevant?
- **Recall@K:** What % of relevant docs were retrieved?
- **MRR (Mean Reciprocal Rank):** Where does the first relevant doc appear?

**Generation Metrics:**
- **Accuracy:** Is the answer factually correct?
- **Relevance:** Does the answer address the question?
- **Groundedness:** Is the answer supported by retrieved context?
- **Completeness:** Does it cover all aspects?
- **Conciseness:** Is it appropriately brief?

**Choose 3-5 metrics** that matter most for your use case.

### Step 1.2: Define Scoring Rubrics

For each metric, define what scores mean:

```python
ACCURACY_RUBRIC = {
    5: "Completely correct, no errors",
    4: "Mostly correct, minor inaccuracies",
    3: "Partially correct, some errors",
    2: "Mostly incorrect, major errors",
    1: "Completely wrong or irrelevant"
}

GROUNDEDNESS_RUBRIC = {
    5: "Fully grounded in context, with citations",
    4: "Mostly grounded, minor extrapolation",
    3: "Partially grounded, some unsupported claims",
    2: "Mostly ungrounded, few connections to context",
    1: "Not grounded at all, pure hallucination"
}
```

---

## Phase 2: Dataset Creation (25 min)

### Step 2.1: Design Test Categories

Create test cases covering:

| Category | Count | Description |
|----------|-------|-------------|
| Simple factual | 15 | Answer in one sentence |
| Multi-fact | 10 | Requires combining info |
| Not in docs | 10 | Answer NOT in documents |
| Edge cases | 10 | Unusual queries |
| Adversarial | 5 | Trick questions |

### Step 2.2: Create Test Cases

Format:
```json
{
    "id": "test_001",
    "category": "simple_factual",
    "question": "How many vacation days do employees get?",
    "expected_answer": "25 days of annual leave per year",
    "expected_source": "company_policy.md",
    "difficulty": "easy"
}
```

### Step 2.3: Include Edge Cases

- Empty query
- Very long query
- Query with typos
- Query in different language
- Query asking about something not in docs
- Query combining multiple topics

---

## Phase 3: Evaluation Implementation (30 min)

### Step 3.1: Exact Match Evaluator

```python
def exact_match(expected: str, actual: str) -> float:
    """Simple exact match (normalized)."""
    expected_norm = expected.lower().strip()
    actual_norm = actual.lower().strip()
    return 1.0 if expected_norm == actual_norm else 0.0
```

### Step 3.2: Fuzzy Match Evaluator

```python
from difflib import SequenceMatcher

def fuzzy_match(expected: str, actual: str) -> float:
    """Fuzzy string matching score."""
    return SequenceMatcher(None, expected.lower(), actual.lower()).ratio()
```

### Step 3.3: LLM-as-Judge Evaluator

This is the most powerful technique - use an LLM to evaluate:

```python
def llm_judge(question: str, expected: str, actual: str, metric: str) -> dict:
    """Use LLM to evaluate response quality."""
    
    prompt = f"""
    Evaluate this AI response on a scale of 1-5 for {metric}.
    
    Question: {question}
    Expected Answer: {expected}
    Actual Answer: {actual}
    
    Rubric for {metric}:
    5 = Excellent
    4 = Good
    3 = Acceptable
    2 = Poor
    1 = Unacceptable
    
    Respond with JSON:
    {{"score": <1-5>, "reasoning": "<brief explanation>"}}
    """
    
    # TODO: Call Gemini and parse response
    pass
```

### Step 3.4: Run Evaluation Pipeline

```python
def evaluate_system(test_dataset: list, system_fn) -> dict:
    """Run full evaluation on test dataset."""
    results = []
    
    for test_case in test_dataset:
        # Get system response
        actual = system_fn(test_case["question"])
        
        # Calculate metrics
        scores = {
            "exact_match": exact_match(test_case["expected_answer"], actual),
            "fuzzy_match": fuzzy_match(test_case["expected_answer"], actual),
            "llm_accuracy": llm_judge(
                test_case["question"], 
                test_case["expected_answer"], 
                actual, 
                "accuracy"
            )
        }
        
        results.append({
            "id": test_case["id"],
            "question": test_case["question"],
            "expected": test_case["expected_answer"],
            "actual": actual,
            "scores": scores
        })
    
    return results
```

---

## Phase 4: Analysis & Reporting (15 min)

### Step 4.1: Calculate Aggregate Metrics

```python
def calculate_summary(results: list) -> dict:
    """Calculate summary statistics."""
    return {
        "total_tests": len(results),
        "exact_match_rate": sum(r["scores"]["exact_match"] for r in results) / len(results),
        "avg_fuzzy_score": sum(r["scores"]["fuzzy_match"] for r in results) / len(results),
        "avg_llm_accuracy": sum(r["scores"]["llm_accuracy"]["score"] for r in results) / len(results)
    }
```

### Step 4.2: Generate Quality Report

Create a markdown report including:
- Overall scores
- Per-category breakdown
- Worst-performing cases
- Improvement recommendations

### Step 4.3: Establish Baseline

Document current performance as baseline for future regression testing:
- Date
- Model version
- System configuration
- Scores per metric

---

## Extension Challenges

1. **A/B testing:** Compare two system versions
2. **Confidence calibration:** Is the system's confidence correlated with accuracy?
3. **Latency tracking:** Add performance metrics
4. **Human evaluation:** Compare LLM-judge with human ratings
5. **CI integration:** Run evaluation on every PR

---

## Submission

Upload to SharePoint `/07-Submissions/Labs/Lab-05/`:
- `test_dataset.json` (50+ cases)
- `evaluator.py`
- `quality_report.md`
- `baseline.json` (current metrics)
- `REFLECTION.md`
