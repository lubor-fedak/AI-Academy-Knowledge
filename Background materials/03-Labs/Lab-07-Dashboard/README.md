# Lab 07: Build an AI Analytics Dashboard

## Overview

Data drives decisions. In this lab, you'll build an analytics dashboard that tracks AI system performance, usage patterns, and business value. This is essential for proving ROI and continuous improvement.

## Learning Objectives

By the end of this lab, you will be able to:
- Define meaningful KPIs for AI systems
- Build data pipelines for AI metrics
- Create interactive visualizations
- Calculate ROI and business impact
- Tell stories with data

## Prerequisites

- Completed Labs 01-05
- Basic SQL knowledge
- Familiarity with visualization tools (Power BI, Streamlit, or similar)

## Time Estimate

**Total: 90 minutes**
- KPI definition: 15 minutes
- Data pipeline: 30 minutes
- Dashboard creation: 35 minutes
- Storytelling: 10 minutes

## Target Roles

- **Primary:** AI-DA, AI-PM
- **Secondary:** All roles (data literacy)

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Application │────▶│    Logs     │────▶│  Data Lake  │
│   Logs      │     │   Parser    │     │  (Storage)  │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │  Transform  │
                                        │  (Metrics)  │
                                        └──────┬──────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │  Dashboard  │
                                        │  (Visuals)  │
                                        └─────────────┘
```

## Success Criteria

- [ ] 10+ KPIs defined with clear definitions
- [ ] Data pipeline ingests sample logs
- [ ] Dashboard has 5+ visualizations
- [ ] Usage trends visible over time
- [ ] ROI calculation implemented
- [ ] Executive summary created

## Deliverables

1. **KPI definitions** (`kpi_definitions.md`)
2. **Data pipeline** (`pipeline.py`)
3. **Dashboard** (Streamlit app or Power BI file)
4. **Executive summary** (1-page insights)
5. **Reflection**
