# Day 2: Prompt Engineering - Mentor Notes

> **CONFIDENTIAL - For Mentors Only**

## Session Overview

| Item | Details |
|------|---------|
| **Duration** | 90 minutes |
| **Participants** | All 80 (combined session) |
| **Deliverable** | Root cause analysis + Solution + Client email |
| **Key Learning** | Hallucinations, system prompts, grounding |

---

## What Students Should Discover

| Concept | Key Insight |
|---------|-------------|
| **Hallucinations** | LLMs generate plausible text, not verified facts |
| **System Prompts** | Can constrain but not eliminate false outputs |
| **Grounding** | Connecting to real data is essential for factual claims |
| **Testing** | Must adversarially test AI before production |
| **Communication** | Explaining AI failures requires honesty without blame |

---

## Typical Misconceptions

| Misconception | Reality | How to Address |
|---------------|---------|----------------|
| "Better prompts fix hallucinations" | Prompts help but don't solve | Ask: "What if user asks tricky question?" |
| "RAG eliminates hallucinations" | RAG reduces, doesn't eliminate | Ask: "What if retrieved data is wrong?" |
| "AI was lying" | AI doesn't lie - it generates | Ask: "Does autocomplete lie?" |
| "We need to retrain the model" | Usually unnecessary - grounding works | Ask: "What's faster and cheaper?" |

---

## Intervention Triggers

| Signal | Intervention |
|--------|--------------|
| Blaming the AI | "The AI isn't malicious - it's a prediction machine" |
| Over-engineering solution | "What's the simplest fix that works?" |
| Ignoring testing | "How would you verify this actually works?" |
| Technical client email | "Would a retail executive understand this?" |

---

## Sample Good Solution

```
ROOT CAUSE:
The chatbot had no access to inventory data. When asked about 
stock, it generated a plausible-sounding number based on 
patterns in its training data.

FIX:
1. Add function calling to query inventory API
2. Update system prompt to never claim inventory without data
3. Add guardrail to flag any numeric claims for review

TESTING:
- 50 adversarial prompts attempting to elicit false claims
- Weekly monitoring of inventory-related conversations
- Human review of flagged responses

CLIENT EMAIL:
"We identified that our AI assistant made an incorrect 
statement about inventory. This happened because the system 
was generating a response without checking our actual data. 
We've fixed this by connecting the AI directly to our 
inventory system and adding safeguards to prevent future 
assumptions. We apologize for any inconvenience and have 
implemented monitoring to ensure this doesn't recur."
```

---

## Debrief Points

1. Why did the AI say "500 units" specifically?
2. What's the difference between grounding and fine-tuning?
3. When should AI say "I don't know"?
4. How do you test for hallucinations at scale?
5. What's the hardest part of explaining this to clients?
