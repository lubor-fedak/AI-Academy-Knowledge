# Day 9: Agent Crashed at 2 AM

## FDE Track - Week 2, Day 9

---

## The Situation

### "Production is Down"

```
3:47 AM. Your phone buzzes. Then buzzes again. And again.

Subject: [CRITICAL] GlobalBank AI Assistant - Unresponsive

"Users are reporting the AI assistant isn't responding.
Error rate spiked to 100% at 2:34 AM.
Last deployment was 3 days ago.
Please investigate immediately."

You open your laptop in bed. The Application Insights 
dashboard is a sea of red. Errors everywhere.

But WHICH error is the real problem? 
There are 47 different error types in the last hour.

You have no runbook. No debugging guide. No idea where 
to start. And the client's morning shift starts in 4 hours.

Welcome to production.
```

---

## Your Challenge

Build monitoring and observability so you catch problems BEFORE 3 AM.

### Success Looks Like

| Criterion | What Good Looks Like |
|-----------|---------------------|
| **Dashboard** | Health visible at a glance |
| **Alerts** | Right people notified for right issues |
| **Logs** | Structured, searchable, no PII |
| **Runbook** | Step-by-step debugging guide |

### Deliverables

1. **Monitoring Dashboard**
   - 5 key health metrics
   - Clear visualization
   - Time-based trends

2. **Alert Configuration**
   - 3-5 critical alerts
   - Appropriate thresholds
   - Correct notification channels

3. **Incident Runbook** (2 pages)
   - First 5 minutes checklist
   - Common issues and fixes
   - Escalation path

4. **Post-Mortem Template**
   - Timeline
   - Root cause
   - Prevention plan

---

## Micro-Context (5 minutes)

> Production debugging is different from development debugging. You can't add print statements. You have to work with what's logged.
>
> Key observability pillars:
> - **Metrics** - Numbers that tell you system health
> - **Logs** - Events that tell you what happened
> - **Traces** - Request flow through the system
>
> Hint: The error you see is rarely the root cause. Trace backwards.

---

## AI-Specific Monitoring

### Health Metrics to Track

| Metric | Why It Matters | Alert Threshold |
|--------|----------------|-----------------|
| Error rate | Something is broken | >5% for 5 min |
| Latency P95 | User experience | >10s |
| Request rate | Traffic anomalies | ±50% from baseline |
| Token usage | Cost and quota | >80% of limit |
| Success rate | Core functionality | <95% |

### AI-Specific Metrics

| Metric | What It Tells You | Alert Threshold |
|--------|-------------------|-----------------|
| Empty retrieval rate | RAG finding nothing | >20% |
| Fallback rate | AI saying "I don't know" | >30% |
| Confidence scores | Answer quality | Average <0.7 |
| User feedback | Thumbs down/up ratio | >20% negative |

---

## Debugging Methodology

### Step 1: Establish Timeline
```
- When did errors start? → 2:34 AM
- What changed around that time? → Check deployments, config changes
- Any patterns? → All users? Specific queries? Specific regions?
```

### Step 2: Categorize Errors
```
47 error types → Group by:
- API errors (external dependency)
- Application errors (our code)
- Infrastructure errors (platform)

Which category has the EARLIEST errors?
```

### Step 3: Form Hypotheses
```
Could be:
□ API rate limit hit
□ Memory exhaustion  
□ Database connection pool
□ External service down
□ Bad deployment (but last deploy was 3 days ago...)
```

### Step 4: Test Hypotheses
```
API rate limit → Check API dashboard
Memory → Check container metrics
Database → Check connection count
External service → Check status page
Deployment → Check what actually changed
```

---

## Post-Mortem Template

```markdown
# Incident Post-Mortem: [Date]

## Summary
[One sentence: what broke and impact]

## Impact
- Duration: X hours Y minutes
- Users affected: N
- Business impact: [revenue, reputation, etc.]

## Timeline (all times UTC)
- 02:34 - First errors in logs
- 02:47 - Alert triggered
- 03:47 - Engineer engaged
- 04:15 - Root cause identified
- 04:45 - Fix deployed
- 04:50 - Service restored

## Root Cause
[What actually broke and why]

## What Went Well
- Alert fired within 15 minutes
- Logs had enough detail to diagnose

## What Went Poorly
- Took 30 min to identify root cause
- No runbook existed

## Action Items
| Action | Owner | Due Date |
|--------|-------|----------|
| Add memory alert | @alice | Feb 28 |
| Create runbook | @bob | Mar 1 |
```

---

## Hints

<details>
<summary>Hint 1: Finding root cause (Click after 10 min)</summary>

In our scenario, the clue is: "Last deployment was 3 days ago."

So it's probably NOT a code change. Think about:
- External API changes (did OpenAI/Gemini change something?)
- Data changes (new documents uploaded?)
- Traffic patterns (sudden spike?)
- Resource exhaustion (slow memory leak?)
</details>

<details>
<summary>Hint 2: Application Insights queries (Click after 25 min)</summary>

Useful KQL queries:
```kusto
// Error count by type
exceptions
| where timestamp > ago(24h)
| summarize count() by problemId
| order by count_ desc

// Latency percentiles
requests
| where timestamp > ago(1h)
| summarize percentile(duration, 95) by bin(timestamp, 5m)
```
</details>

<details>
<summary>Hint 3: Alert design (Click after 40 min)</summary>

Good alerts:
1. **Actionable** - Someone can do something about it
2. **Not noisy** - Fires only when truly important
3. **Contextual** - Includes enough info to start investigating

Bad alert: "Error occurred"
Good alert: "Error rate >5% (currently 23%) for ai-assistant in prod. Recent errors: RateLimitExceeded"
</details>

---

## Self-Study Assignment (90 min)

1. **Build monitoring dashboard** - 5 key metrics (30 min)
2. **Configure alerts** - 3 critical alerts (20 min)
3. **Write incident runbook** - First 15 minutes guide (25 min)
4. **Create post-mortem template** - For your team (15 min)

### Stretch Goals
- Set up distributed tracing
- Create SLO/SLA dashboard
- Implement synthetic monitoring (automated health checks)
