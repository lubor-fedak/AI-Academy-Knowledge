# Team Formation Guide

## Overview
8 cross-functional teams, 10 members each (1 per role).

## Team Composition

Each team has exactly:
| Role / Track | Count | Primary Responsibility |
|--------------|-------|------------------------|
| FDE | 1 | Technical lead, architecture |
| AI-SE (within FDE capability) | 1 | Platform, CI/CD, quality |
| AI-PM | 1 | Scope, stakeholders, delivery |
| AI-FE (within FDE capability) | 1 | User interface |
| AI-SEC | 1 | Security review |
| AI-DX (Design/UX skill track) | 1 | User experience & journey mapping |
| AI-DS | 1 | Evaluation, quality metrics |
| AI-DA (within FDE capability) | 1 | Analytics, ROI |

> Taxonomy note: In the Consult model, AI-SE, AI-FE and AI-DA are specializations within the **Forward Deployed Engineer capability**, and AI-DX is a **design/UX skill track**, not a separate Designer job role. The team structure here keeps 8 tracks for the academy schedule while aligning skills to the Consult capability model.

## Team Leadership

**Option A:** FDE leads (technical-first projects)
**Option B:** AI-PM leads (business-first projects)

Decision made per team based on project nature.

## Team Assignment Process

1. **Self-selection round** (Day 1)
   - Teams form organically
   - Balance skills and experience

2. **Mentor adjustment** (Day 1)
   - Ensure balanced teams
   - Consider personality dynamics

3. **Final teams** (Day 2)
   - Locked for duration
   - No changes after Day 2

## Azure Resources Per Team

```
rg-team-[name]/
├── Container Apps Environment
├── Storage Account
├── Key Vault
├── Application Insights
└── Budget: €150 cap
```

## Communication

- **Primary:** Microsoft Teams channel per team
- **Code:** Azure DevOps repository
- **Docs:** SharePoint team folder
- **Standups:** Daily 15-min check-in
