# Lab 05: Mentor Notes

## Key Concepts

1. **Evaluation is hard:** There's no perfect metric for AI
2. **LLM-as-judge:** Powerful but has limitations
3. **Regression testing:** Catch quality drops before production
4. **Human calibration:** Validate automated metrics periodically

## Common Struggles

### "My metrics don't match human judgment"
**Intervention:** LLM-judge may need better prompts. Try adding examples.

### "Test cases are too easy"
**Intervention:** Include adversarial cases. Real users ask strange things.

### "Exact match always fails"
**Intervention:** That's expected! Use semantic similarity or LLM-judge.

## Debrief Topics

1. **What metrics matter?** Depends on use case. Production vs. demo.
2. **LLM-as-judge limitations:** May have same biases as system being evaluated.
3. **Cost of evaluation:** Running eval on every change adds up.
4. **Human-in-the-loop:** When to involve humans?

## What Good Looks Like

- Diverse test dataset (not just happy path)
- Multiple evaluation methods
- Clear quality thresholds
- Actionable improvement recommendations
