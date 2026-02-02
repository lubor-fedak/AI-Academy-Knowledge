# Lab 05: Build an AI Evaluation Framework

## Overview

"How good is our AI?" is the most important question you can't answer without evaluation. In this lab, you'll build a comprehensive evaluation framework for AI systems including automated metrics, human evaluation, and regression testing.

## Learning Objectives

By the end of this lab, you will be able to:
- Define measurable quality metrics for AI systems
- Create golden test datasets with expected outputs
- Implement automated evaluation pipelines
- Use LLM-as-judge for quality assessment
- Set up regression testing for AI changes

## Prerequisites

- Completed Labs 01-03
- Understanding of classification metrics
- Basic statistics knowledge helpful

## Time Estimate

**Total: 90 minutes**
- Metrics definition: 20 minutes
- Dataset creation: 25 minutes
- Evaluation implementation: 30 minutes
- Analysis & reporting: 15 minutes

## Target Roles

- **Primary:** AI-DS, FDE
- **Secondary:** AI-PM (for understanding metrics)

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Test      │────▶│     AI      │────▶│   Actual    │
│   Queries   │     │   System    │     │   Outputs   │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Expected   │────▶│  Evaluator  │◀────│   Actual    │
│  Outputs    │     │  (Metrics)  │     │   Outputs   │
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Report    │
                    │  (Scores)   │
                    └─────────────┘
```

## Success Criteria

- [ ] 50+ test cases with expected outputs
- [ ] 3+ automated metrics implemented
- [ ] LLM-as-judge evaluator working
- [ ] Evaluation pipeline runs end-to-end
- [ ] Quality report generated
- [ ] Regression test baseline established

## Deliverables

1. **Test dataset** (`test_dataset.json`) - 50+ Q&A pairs
2. **Evaluation code** (`evaluator.py`)
3. **Quality report** (`quality_report.md`)
4. **Baseline metrics** - documented current performance
5. **Reflection**
