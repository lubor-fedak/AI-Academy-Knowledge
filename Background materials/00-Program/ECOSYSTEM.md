# AI Academy Ecosystem Architecture v2

## Executive Summary

Revised infrastructure plan for Kyndryl AI Academy (February 2 - March 15, 2026, 80 participants across 8 roles) leveraging existing enterprise licenses and Google Partner credits.

**Key Change:** Primary AI API is Gemini (via Google Partner credits), with Azure OpenAI as optional scale-up.

---

## 1. PLATFORM STACK

| Layer | Tool | Purpose | Status |
|-------|------|---------|--------|
| **AI Tutors** | ChatGPT Enterprise | 8 role-specific custom GPTs | Available |
| **IDE + AI Coding** | Google Antigravity | Development, agentic coding, Gemini 3 | Available |
| **AI API (Primary)** | Gemini API | Labs, RAG, agents | Google Partner credits |
| **AI API (Optional)** | Azure OpenAI | KAF integration, enterprise deployment | On-demand |
| **Infrastructure** | Azure | Container Apps, AI Search, Cosmos DB | Available |
| **Documents** | SharePoint / OneDrive | Syllabi, materials, submissions | M365 E5 |
| **Code Repository** | Azure DevOps | Version control, CI/CD | Available |

---

## 2. SANDBOX ARCHITECTURE

### 2.1 Learning Sandbox: ChatGPT Enterprise

**Purpose:** AI-native learning with role-specific tutors

```
ChatGPT Enterprise Workspace
└── AI Academy 2026
    ├── [GPT] FDE Tutor
    ├── [GPT] AI-SE Tutor
    ├── [GPT] AI-PM Tutor
    ├── [GPT] AI-FE Tutor
    ├── [GPT] AI-SEC Tutor
    ├── [GPT] AI-DX Tutor
    ├── [GPT] AI-DA Tutor
    └── [GPT] AI-DS Tutor
```

**Configuration:**
- Enable conversation history export for assessment
- Upload KAF documentation to each tutor's knowledge base
- Configure workspace sharing per role group

---

### 2.2 Development Sandbox: Google Antigravity

**Purpose:** Hands-on coding, agentic development, API experimentation

**Why Antigravity is ideal for AI Academy:**
- Agentic coding with Gemini 3 Pro built-in
- Browser control for testing (students can build + test in one flow)
- Async agent patterns (matches your "productive struggle" philosophy)
- Artifact generation (implementation plans, walkthroughs) for assessment
- VS Code-familiar interface (Windsurf base)

**Workspace Setup:**

```
Antigravity Workspaces
├── ai-academy-common/          # Shared starter templates
│   ├── rag-template/
│   ├── agent-template/
│   └── kaf-quickstart/
│
├── fde-track/                  # Role-specific starters
│   ├── participant-01/
│   ├── participant-02/
│   └── ... (10 workspaces)
│
├── ai-se-track/
│   └── ... (10 workspaces)
│
└── ... (all 8 roles)
```

**Per-Participant Configuration:**
- Clone from role-specific template
- Pre-configured `.env` with Gemini API keys (from Partner credits)
- Azure CLI authenticated for deployment phase
- Git connected to Azure DevOps repo

---

### 2.3 Integration Sandbox: Azure Resource Groups

**Purpose:** Team projects (Week 4-5) and Hackathon (March 15)

```
Azure Subscription: AI-Academy-2026
│
├── rg-ai-academy-shared/
│   ├── Azure AI Search (shared index)
│   ├── Cosmos DB (shared document store)
│   ├── Key Vault (API keys, secrets)
│   └── Application Insights (monitoring)
│
├── rg-team-alpha/
│   ├── Container Apps (deployment target)
│   ├── Storage Account (team data)
│   └── Budget: $150 cap
│
├── rg-team-beta/
│   └── ... (identical)
│
└── ... (8 teams total)
```

**Hackathon Day Budget:** Additional $50/team cap for March 15

---

## 3. LEARNING MATERIALS STRUCTURE

### 3.1 SharePoint Site Architecture

```
SharePoint: AI Academy 2026
│
├── 00-Program/
│   ├── README.md                 # Academy overview
│   ├── Calendar.md               # Day-by-day schedule
│   ├── Assessment-Criteria.md    # Grading rubric
│   └── Templates/
│       ├── Daily-Journal.md
│       ├── Project-Brief.md
│       └── Demo-Checklist.md
│
├── 01-Common-Foundations/        # Days 1-3 (all participants)
│   ├── Day-01-AI-Landscape/
│   │   ├── SITUATION.md          # Challenge description
│   │   ├── RESOURCES.md          # Links, readings
│   │   └── DEBRIEF.md            # Discussion points
│   ├── Day-02-Prompt-Engineering/
│   └── Day-03-Agentic-Patterns/
│
├── 02-Role-Tracks/
│   ├── FDE/
│   │   ├── Syllabus.md
│   │   ├── Week-02/
│   │   ├── Week-04/
│   │   └── Week-05/
│   ├── AI-SE/
│   ├── AI-PM/
│   ├── AI-FE/
│   ├── AI-SEC/
│   ├── AI-DX/
│   ├── AI-DA/
│   └── AI-DS/
│
├── 03-Labs/
│   ├── Lab-01-Chatbot-Basics/
│   │   ├── Instructions.md
│   │   └── Antigravity-Template (link)
│   ├── Lab-02-RAG-Pipeline/
│   └── Lab-03-Multi-Agent/
│
├── 04-Projects/
│   ├── Team-Alpha/
│   ├── Team-Beta/
│   └── ... (8 teams)
│
├── 05-Hackathon/
│   ├── Client-Brief.md
│   ├── Evaluation-Criteria.md
│   └── Presentation-Template.pptx
│
├── 06-Reference/
│   ├── KAF-Documentation/
│   ├── AI-Innovation-Lab-Method/
│   ├── Prompt-Library.md
│   └── Troubleshooting.md
│
└── 07-Submissions/               # Student deliverables
    ├── Weekly-Checkpoints/
    │   ├── Week-01/
    │   └── ...
    └── Final-Projects/
```

### 3.2 Content Format: SITUATION.md

```markdown
# [Situation Title]

## The Challenge
[Open-ended problem - no prescribed solution]

## Context
[Why this matters, real-world connection]

## Success Looks Like
[Observable outcomes, NOT step-by-step instructions]

## Time Box
- Exploration: XX minutes
- AI Tutor / Antigravity Agent: encouraged
- Mentor check-in: at XX:XX

## Starting Point
[Link to Antigravity template or starter code]

## Hints (unlock after 30 min if stuck)
<details>
<summary>Hint 1</summary>
[First nudge]
</details>
```

### 3.3 Access Control

| Content | Access | Method |
|---------|--------|--------|
| Syllabi, schedules | All participants | SharePoint permissions |
| Daily situations | Unlocked each morning | Folder permissions by date |
| Solutions | Post-debrief only | Separate "Solutions" folder |
| AI Tutors | Role-specific | ChatGPT Enterprise workspace |
| Antigravity templates | Role-specific | Workspace cloning |

---

## 4. PROJECT STRUCTURE

### 4.1 Individual Practice (Weeks 1-2)

**Daily Flow:**

| Time | Activity | Tool |
|------|----------|------|
| 09:00-09:10 | Situation introduction | Teams/Zoom + SharePoint |
| 09:10-10:10 | Individual exploration | Antigravity + AI Tutor |
| 10:10-10:25 | Debrief discussion | Teams/Zoom |
| 10:25-10:30 | Tomorrow preview | Mentor |
| --- | --- | --- |
| Self-study (90 min) | Lab + reading | Antigravity + SharePoint |

**Weekly Checkpoint (Friday):**
- Upload artifact to SharePoint `/07-Submissions/Weekly-Checkpoints/`
- 5-minute peer review in pairs
- Mentor feedback by Monday

---

### 4.2 Team Projects (Weeks 4-5)

**Team Formation (end of Week 2):**
- 8 cross-functional teams
- 1 person per role in each team
- Team lead: FDE or AI-PM

**Azure DevOps Repository Structure:**

```
team-alpha/
├── docs/
│   ├── problem-statement.md
│   ├── architecture.md
│   └── demo-script.md
├── src/
│   ├── agents/
│   ├── api/
│   └── frontend/
├── tests/
├── infra/
│   └── main.bicep
└── README.md
```

**Milestones:**

| Day | Milestone | Deliverable |
|-----|-----------|-------------|
| 1 | Problem framing | Problem statement |
| 3 | Architecture | Solution diagram |
| 5 | MVP working | Demo-able prototype |
| 7 | Peer review | Cross-team feedback |
| 10 | Final polish | Presentation ready |

---

### 4.3 Hackathon (March 15)

**Resources per team:**
- Azure resource group (pre-provisioned)
- Gemini API (Partner credits)
- $50 Azure budget cap (for any Azure-specific services)
- Azure DevOps repo from template

**Deliverables:**
1. Working MVP demo
2. Solution architecture (1 page)
3. Value proposition (2-3 slides)
4. Security assessment (AI-SEC checklist)
5. 10-minute presentation

---

## 5. AI CREDITS & COSTS

### 5.1 Primary: Google Partner Credits (Gemini API)

| Usage | Estimated Tokens | Notes |
|-------|------------------|-------|
| Common Foundations (3 days) | ~15M tokens | 80 users x exploration |
| Role-Specific Learning (10 days) | ~100M tokens | Labs, experiments |
| Team Projects (10 days) | ~150M tokens | Heavier usage |
| Hackathon (1 day) | ~10M tokens | Intensive sprint |
| **Total Estimated** | **~275M tokens** | |

**Gemini 3 Pro pricing reference:**
- Input: $0.50 / 1M tokens
- Output: $1.50 / 1M tokens
- Estimated cost if paid: ~$300-500

**Covered by Google Partner credits** - confirm allocation with your Google rep.

---

### 5.2 Optional: Azure OpenAI (On-Demand)

**When to activate:**
- Gemini quota exceeded
- KAF-specific labs requiring Azure OpenAI
- Client hackathon explicitly requires Azure stack
- Certification prep for Azure AI Engineer

**Recommended Models (January 2026 pricing per 1M tokens):**

| Model | Input | Output | Best For |
|-------|-------|--------|----------|
| gpt-5-nano | $0.05 | $0.40 | General tasks, experiments |
| gpt-4o-mini | $0.15 | $0.60 | Coding, RAG pipelines |
| gpt-4.1-nano | $0.10 | $0.40 | Alternative to gpt-5-nano |
| text-embedding-3-small | $0.02 | - | RAG embeddings |

**Realistic Budget (if needed):**

| Usage | Tokens | Model Mix | Est. Cost |
|-------|--------|-----------|-----------|
| Labs + experiments | 200M | gpt-5-nano | ~$50 |
| RAG embeddings | 50M | embedding-3-small | ~$1 |
| Complex reasoning | 25M | gpt-4o-mini | ~$15 |
| **Buffer (50%)** | - | - | ~$35 |
| **TOTAL** | ~275M | mixed | **~$100** |

**Quota Request (prepare in advance):**

```
Subject: Azure OpenAI Quota Request - Kyndryl AI Academy

Subscription: [your-subscription-id]
Region: West Europe

Requested (standby):
- gpt-5-nano: 500K TPM
- gpt-4o-mini: 300K TPM
- text-embedding-3-small: 300K TPM

Use Case: Internal training (80 users), Feb-Mar 2026
Contact: [email]
```

---

### 5.3 Cost Summary

| Item | Status | Cost |
|------|--------|------|
| ChatGPT Enterprise | Existing | $0 |
| Google Antigravity | Existing | $0 |
| Gemini API | Partner credits | $0 |
| Azure Infrastructure | Existing | $0 |
| SharePoint/OneDrive | M365 E5 | $0 |
| Azure DevOps | Existing | $0 |
| **Azure OpenAI (optional)** | On-demand | **~$100** |

**Best case:** $0 additional spend (Gemini covers everything)
**With Azure OpenAI buffer:** ~$100

---

## 6. IMPLEMENTATION CHECKLIST

### Week of January 20-24

| Task | Owner | Status |
|------|-------|--------|
| Confirm Gemini API quota with Google Partner | Academy Lead | Pending |
| Verify ChatGPT Enterprise seat count (80+) | IT | Pending |
| Create SharePoint site structure | Academy Lead | Pending |
| Set up Azure DevOps project | Cloud Team | Pending |
| Request Azure OpenAI quota (standby) | Cloud Team | Pending |

### Week of January 27-31

| Task | Owner | Status |
|------|-------|--------|
| Create 8 AI Tutor GPTs in ChatGPT Enterprise | Instructors | Pending |
| Upload KAF docs to each tutor's knowledge | Instructors | Pending |
| Set up Antigravity workspace templates | Cloud Team | Pending |
| Populate SharePoint with Day 1-3 content | Instructors | Pending |
| Create Azure resource groups for teams | Cloud Team | Pending |
| Configure budget alerts ($150/team) | Cloud Team | Pending |
| Test full flow with 2-3 pilot users | Academy Lead | Pending |

### February 1 (Day Before Launch)

| Task | Owner | Status |
|------|-------|--------|
| Verify all 80 participants have access | Academy Lead | Pending |
| Send welcome email with links | Academy Lead | Pending |
| Final environment check | Cloud Team | Pending |

---

## 7. TOOL-TO-ACTIVITY MAPPING

| Activity | Primary Tool | Backup |
|----------|--------------|--------|
| Learning concepts | AI Tutor (ChatGPT) | Gemini in Antigravity |
| Writing code | Antigravity | VS Code local |
| Running code | Antigravity | Azure Container Apps |
| Building RAG | Antigravity + Gemini API | Azure AI Search + OpenAI |
| Team collaboration | Azure DevOps + Teams | GitHub + Slack |
| Document storage | SharePoint | OneDrive |
| Presentations | PowerPoint (M365) | Google Slides |
| Deployment | Azure Container Apps | - |

---

## 8. RISK MITIGATION

| Risk | Impact | Mitigation |
|------|--------|------------|
| Gemini quota exceeded | Medium | Pre-request generous quota; Azure OpenAI as backup |
| Antigravity outage | High | Document VS Code + local setup as fallback |
| ChatGPT Enterprise issues | Medium | Gemini in Antigravity can serve as tutor |
| SharePoint access issues | Low | OneDrive personal backup |
| Azure budget overrun | Medium | Hard caps per resource group, daily monitoring |

---

## APPENDIX: Quick Links Template

Create this as a pinned Teams post / SharePoint homepage:

```markdown
# AI Academy 2026 - Quick Links

## Daily Essentials
- [Today's Situation](sharepoint-link)
- [My AI Tutor](chatgpt-enterprise-link)
- [My Antigravity Workspace](antigravity-link)
- [Submit Checkpoint](sharepoint-submissions-link)

## Reference
- [KAF Documentation](sharepoint-kaf-link)
- [Troubleshooting Guide](sharepoint-troubleshooting-link)
- [Full Calendar](sharepoint-calendar-link)

## Help
- Teams Channel: #ai-academy-help
- Mentor Office Hours: [calendar-link]
```

---

*Document Version: 2.0*
*Created: January 25, 2026*
*Stack: ChatGPT Enterprise + Google Antigravity + Gemini API + Azure*
