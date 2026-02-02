# Lab 07: Instructions

## Phase 1: KPI Definition (15 min)

### Step 1.1: Identify Stakeholder Questions

What do different stakeholders want to know?

| Stakeholder | Question |
|-------------|----------|
| Executive | Is this AI investment paying off? |
| Product | Are users satisfied? What features do they use? |
| Engineering | Is the system healthy? Where are bottlenecks? |
| Finance | What's the cost per query? Are we within budget? |

### Step 1.2: Define KPIs

For each category, define 2-3 metrics:

**Usage Metrics:**
- Total queries per day/week/month
- Unique users
- Queries per user
- Peak usage times
- Feature adoption rates

**Quality Metrics:**
- Average response quality score
- Hallucination rate
- User satisfaction (thumbs up/down)
- Escalation rate to human

**Performance Metrics:**
- Average latency (p50, p95, p99)
- Error rate
- Availability/uptime
- Token usage per query

**Business Metrics:**
- Cost per query
- Time saved (compared to baseline)
- Issues resolved without human
- ROI calculation

### Step 1.3: Document Each KPI

Template:
```markdown
## KPI: Queries Per Day

**Definition:** Total number of user queries processed in 24 hours

**Formula:** COUNT(queries) WHERE timestamp >= today_start

**Data Source:** Application logs

**Target:** 500 queries/day by end of Q1

**Owner:** Product Team

**Visualization:** Line chart with daily trend
```

---

## Phase 2: Data Pipeline (30 min)

### Step 2.1: Define Log Schema

```python
from pydantic import BaseModel
from datetime import datetime

class QueryLog(BaseModel):
    query_id: str
    timestamp: datetime
    user_id: str
    query_text: str
    response_text: str
    latency_ms: int
    tokens_input: int
    tokens_output: int
    model: str
    success: bool
    quality_score: float | None
    user_feedback: str | None  # "positive", "negative", None
```

### Step 2.2: Generate Sample Data

```python
import random
from datetime import datetime, timedelta

def generate_sample_logs(n: int = 1000) -> list[dict]:
    """Generate sample query logs for dashboard development."""
    logs = []
    base_time = datetime.now() - timedelta(days=30)
    
    for i in range(n):
        logs.append({
            "query_id": f"q_{i:05d}",
            "timestamp": base_time + timedelta(
                hours=random.randint(0, 720),
                minutes=random.randint(0, 59)
            ),
            "user_id": f"user_{random.randint(1, 50)}",
            "query_text": f"Sample query {i}",
            "latency_ms": random.randint(200, 5000),
            "tokens_input": random.randint(50, 500),
            "tokens_output": random.randint(100, 2000),
            "success": random.random() > 0.05,
            "quality_score": random.uniform(3.0, 5.0),
            "user_feedback": random.choice([None, None, None, "positive", "negative"])
        })
    
    return logs
```

### Step 2.3: Calculate Metrics

```python
import pandas as pd

def calculate_daily_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate logs into daily metrics."""
    df['date'] = df['timestamp'].dt.date
    
    daily = df.groupby('date').agg({
        'query_id': 'count',
        'user_id': 'nunique',
        'latency_ms': ['mean', 'median', lambda x: x.quantile(0.95)],
        'tokens_input': 'sum',
        'tokens_output': 'sum',
        'success': 'mean',
        'quality_score': 'mean'
    }).reset_index()
    
    daily.columns = [
        'date', 'queries', 'unique_users', 
        'latency_mean', 'latency_p50', 'latency_p95',
        'tokens_in', 'tokens_out', 'success_rate', 'avg_quality'
    ]
    
    return daily
```

---

## Phase 3: Dashboard Creation (35 min)

### Step 3.1: Choose Your Tool

**Option A: Streamlit (Python)**
- Quick to build
- Interactive
- Easy deployment

**Option B: Power BI**
- Enterprise standard
- Rich visuals
- Familiar to business users

### Step 3.2: Streamlit Dashboard (Example)

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Analytics", layout="wide")

st.title("🤖 AI System Analytics Dashboard")

# Load data
df = pd.read_csv("metrics.csv")

# KPI cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Queries", f"{df['queries'].sum():,}")
col2.metric("Unique Users", f"{df['unique_users'].max():,}")
col3.metric("Avg Latency", f"{df['latency_mean'].mean():.0f}ms")
col4.metric("Success Rate", f"{df['success_rate'].mean()*100:.1f}%")

# Charts
st.subheader("📈 Daily Query Volume")
fig1 = px.line(df, x='date', y='queries', title="Queries per Day")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("⚡ Latency Distribution")
fig2 = px.box(df, y='latency_p95', title="P95 Latency Trend")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("💰 Token Usage & Cost")
# Calculate cost (example: $0.001 per 1K tokens)
df['cost'] = (df['tokens_in'] + df['tokens_out']) / 1000 * 0.001
fig3 = px.bar(df, x='date', y='cost', title="Daily API Cost")
st.plotly_chart(fig3, use_container_width=True)
```

### Step 3.3: Required Visualizations

Include at least:
1. **KPI summary cards** - headline numbers
2. **Time series** - trends over time
3. **Distribution** - latency, quality scores
4. **Breakdown** - by user, by feature, by time of day
5. **ROI/Cost** - business value visualization

---

## Phase 4: Storytelling (10 min)

### Step 4.1: Executive Summary Template

```markdown
# AI System Performance - Executive Summary

## Key Insights

1. **Usage is growing**: 40% increase in queries over last month
2. **Quality is stable**: Average quality score 4.2/5.0
3. **ROI is positive**: Estimated €50K saved in Q1

## Recommendations

1. Increase capacity - approaching 80% of rate limits
2. Investigate Tuesday latency spikes
3. Promote underutilized features

## Next Steps

- [Action item 1]
- [Action item 2]
```

---

## Extension Challenges

1. **Real-time updates:** Add live data streaming
2. **Alerting:** Set up anomaly detection
3. **Forecasting:** Predict future usage/costs
4. **A/B comparison:** Compare system versions
5. **User segments:** Analyze by user cohort

---

## Submission

Upload to SharePoint `/07-Submissions/Labs/Lab-07/`:
- `kpi_definitions.md`
- `pipeline.py`
- `dashboard.py` or `dashboard.pbix`
- `executive_summary.md`
- `REFLECTION.md`
