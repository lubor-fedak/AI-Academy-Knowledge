# AI Academy - Tools & Access Guide

## Quick Links

| Tool | URL | Purpose |
|------|-----|---------|
| ChatGPT Enterprise | [Link TBD] | AI Tutors |
| Google Antigravity | [Link TBD] | Development IDE |
| Azure Portal | https://portal.azure.com | Infrastructure |
| SharePoint | [Link TBD] | Documents & Materials |
| Azure DevOps | [Link TBD] | Code Repository |

---

## 1. ChatGPT Enterprise (AI Tutors)

### Access
- URL: https://chat.openai.com (enterprise login)
- Login: Your Kyndryl email
- SSO: Enabled

### Finding Your AI Tutor
1. Log in to ChatGPT Enterprise
2. Navigate to **Workspaces** → **AI Academy 2026**
3. Select your role-specific tutor:
   - `AI Academy - FDE Tutor`
   - `AI Academy - AI-SE Tutor`
   - `AI Academy - AI-PM Tutor`
   - `AI Academy - AI-FE Tutor`
   - `AI Academy - AI-SEC Tutor`
   - `AI Academy - AI-DX Tutor`
   - `AI Academy - AI-DA Tutor`
   - `AI Academy - AI-DS Tutor`

### Best Practices
- Start each session with context about your current situation
- Be specific in your questions
- Challenge the AI's responses
- Export important conversations for your checkpoint

### Troubleshooting
| Issue | Solution |
|-------|----------|
| Can't find workspace | Contact IT Support |
| Tutor not responding | Refresh page, try new chat |
| Wrong tutor responses | Check you're in correct workspace |

---

## 2. Google Antigravity (Development IDE)

### Access
- URL: [Antigravity Portal Link]
- Login: Google Enterprise credentials
- Workspace: Pre-assigned per role

### Your Workspace
```
Workspaces/
├── ai-academy-common/          # Shared templates (read-only)
│   ├── rag-template/
│   ├── agent-template/
│   └── kaf-quickstart/
│
└── [your-role]-track/          # Your workspace
    └── [your-name]/            # Personal workspace
```

### Key Features
- **Gemini 3 Pro** built-in for AI assistance
- **Browser control** for testing
- **Git integration** with Azure DevOps
- Pre-configured environment variables

### First-Time Setup
1. Log in to Antigravity
2. Open your assigned workspace
3. Verify `.env` file has Gemini API key
4. Run `npm install` or `pip install -r requirements.txt`
5. Test: Run the hello-world example

### Troubleshooting
| Issue | Solution |
|-------|----------|
| Workspace not found | Contact Cloud Team |
| API key errors | Check `.env` file, contact support |
| Build failures | Check console, ask AI Tutor |

---

## 3. Azure Portal

### Access
- URL: https://portal.azure.com
- Login: Kyndryl Azure AD credentials
- Subscription: `AI-Academy-2026`

### Resource Groups

**Shared Resources** (read access):
```
rg-ai-academy-shared/
├── Azure AI Search
├── Cosmos DB
├── Key Vault
└── Application Insights
```

**Team Resources** (Week 4+):
```
rg-team-[name]/
├── Container Apps
├── Storage Account
└── Budget: $150 cap
```

### Key Services

| Service | Purpose | When Used |
|---------|---------|-----------|
| Azure AI Search | Vector search, RAG | Labs, Projects |
| Cosmos DB | Document storage | Labs, Projects |
| Container Apps | Deployment | Week 4+ |
| Key Vault | Secrets management | All |

### Budget Alerts
- You'll receive email at 50%, 75%, 90% of budget
- Hard cap prevents overspend
- Contact Academy Lead if you need exception

---

## 4. SharePoint (Documents)

### Access
- URL: [SharePoint Site Link]
- Login: M365 credentials
- Mobile: SharePoint app available

### Site Structure
```
AI Academy 2026/
├── 00-Program/          # Schedules, assessment
├── 01-Common-Foundations/
├── 02-Role-Tracks/      # Your role folder
├── 03-Labs/
├── 04-Team-Projects/
├── 05-Hackathon/
├── 06-Reference/        # KAF docs, glossary
└── 07-Submissions/      # Upload here
```

### Submitting Work
1. Navigate to `07-Submissions/Weekly-Checkpoints/Week-XX/`
2. Create folder with your name
3. Upload all artifacts
4. Notify mentor via Teams

### Permissions
| Folder | Your Access |
|--------|-------------|
| 00-Program | Read |
| 01-Common-Foundations | Read |
| 02-Role-Tracks/[Your Role] | Read |
| 02-Role-Tracks/[Other Roles] | Read |
| 03-Labs | Read |
| 07-Submissions/[Your Name] | Read/Write |
| 08-Mentor-Zone | No Access |

---

## 5. Azure DevOps (Code Repository)

### Access
- URL: https://dev.azure.com/kyndryl/ai-academy-2026
- Login: Azure AD credentials

### Repository Structure
```
ai-academy-2026/
├── labs/                # Lab starter code
├── templates/           # Project templates
└── teams/              # Team project repos (Week 4+)
    ├── team-alpha/
    ├── team-beta/
    └── ...
```

### Git Setup
```bash
# Clone your team repo (Week 4+)
git clone https://dev.azure.com/kyndryl/ai-academy-2026/_git/team-[name]

# Configure identity
git config user.name "Your Name"
git config user.email "your.email@kyndryl.com"
```

### Branch Strategy
- `main` - Protected, requires PR
- `dev` - Integration branch
- `feature/*` - Your work

---

## 6. Microsoft Teams

### Channels
| Channel | Purpose |
|---------|---------|
| #ai-academy-general | Announcements |
| #ai-academy-help | Technical support |
| #ai-academy-[role] | Role-specific discussion |
| #ai-academy-team-[name] | Team project (Week 4+) |

### Office Hours
- **When:** Daily 15:00-16:00 CET
- **Where:** Teams meeting link in channel
- **Who:** Rotating mentors

---

## 7. Gemini API (Google Partner Credits)

### Access
- API Key: Pre-configured in Antigravity `.env`
- Quota: Shared pool, generous limits
- Models: Gemini 3 Pro, Gemini 3 Flash

### Direct API Access (if needed)
```python
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-3-pro')
response = model.generate_content("Hello, world!")
```

### Rate Limits
- Requests: 60/minute
- Tokens: 1M/day per user
- If you hit limits, wait or contact support

---

## Troubleshooting Flowchart

```
Problem?
    │
    ├─→ Can't log in?
    │       └─→ Contact IT Support
    │
    ├─→ Tool not working?
    │       └─→ Check #ai-academy-help
    │       └─→ Ask AI Tutor
    │       └─→ Contact Cloud Team
    │
    ├─→ Budget issues?
    │       └─→ Contact Academy Lead
    │
    └─→ Content/curriculum questions?
            └─→ Ask your Mentor
            └─→ Check SharePoint FAQ
```

---

## Support Contacts

| Issue Type | Contact | Response Time |
|------------|---------|---------------|
| Login/Access | IT Support | 4 hours |
| Cloud/Azure | Cloud Team | Same day |
| Content | Your Mentor | Same day |
| General | Academy Lead | Same day |

---

## First Day Checklist

- [ ] Log in to ChatGPT Enterprise
- [ ] Find your AI Tutor
- [ ] Log in to Antigravity
- [ ] Open your workspace
- [ ] Log in to Azure Portal
- [ ] Verify subscription access
- [ ] Access SharePoint site
- [ ] Join Teams channels
- [ ] Test Gemini API (run hello-world)

**If anything doesn't work, report immediately in #ai-academy-help**
