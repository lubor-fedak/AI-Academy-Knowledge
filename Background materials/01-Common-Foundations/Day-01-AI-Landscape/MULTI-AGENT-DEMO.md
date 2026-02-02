# Day 1 Live Demo: Customer Issue Resolution Pipeline

## Overview

**Cieľ:** Ukázať praktickú multi-agent orchestráciu - zákazník hlási vágny problém, AI agenti urobia research, nájdu riešenie, identifikujú príležitosti a navrhnú koho internekonzultovať.

```
📧 Zákazník: "Máme problémy s latenciou servera, nevieme čím to je..."

    ↓

🔍 Research Agent
   → Skontroluje infraštruktúru zákazníka
   → Prezrie nedávne incidenty
   → Analyzuje kontext z emailov

    ↓

💡 Advisor Agent
   → Identifikuje možné príčiny
   → Navrhne riešenia
   → Nájde upsell príležitosti (nová revenue!)
   → Odporučí koho v Kyndryle konzultovať

    ↓

✍️ Response Agent
   → Pripraví draft odpovede
   → Pridá CC na konzultovaných kolegov
   → Užívateľ odošle manuálne
```

**Prečo toto demo:**

- Zákazník hlási vágny problém (realita)
- Agent ušetrí hodiny manuálneho research-u
- Identifikuje revenue príležitosti (business value)
- Naviguje internú organizáciu (kto čo vlastní)
- Človek má finálnu kontrolu pred odoslaním

---

## Čo Demo Ukazuje

| Koncept | Ako sa prejaví |
|---------|----------------|
| **Agent ako researcher** | Zbiera info z viacerých zdrojov |
| **Knowledge grounding** | Používa SharePoint, incident históriu |
| **Business value** | Nájde upsell príležitosti |
| **Organizational navigation** | Vie kto čo vlastní v Kyndryle |
| **Human-in-the-loop** | Človek konzultuje a odosiela |

---

## Demo Setup

### Prerequisites

```text
1. Claude API key (alebo Azure OpenAI)
2. Terminál s farebným outputom
3. Mock dáta pre zákazníka (infraštruktúra, incidenty)
4. Mock Kyndryl kontakty (account manager, SMEs)
```

### Folder Structure

```text
demo-issue-pipeline/
├── orchestrator.py
├── sample_emails/
│   └── customer_latency_issue.txt
├── mock_data/
│   ├── customer_infrastructure.json
│   ├── recent_incidents.json
│   ├── customer_context.json
│   └── kyndryl_contacts.json
└── output/
    ├── 01_research.json
    ├── 02_recommendations.json
    └── 03_draft_email.md
```

---

## Mock Data Files

### customer_infrastructure.json

```json
{
  "customer": "AutoParts Manufacturing GmbH",
  "account_id": "APM-2024-DE",
  "environment": {
    "cloud_provider": "Microsoft Azure",
    "region": "West Europe (Netherlands)",
    "subscription": "AutoParts-Production",
    "virtual_machines": [
      {
        "name": "apm-app-01",
        "type": "Standard_D4s_v5",
        "role": "Application Server",
        "os": "RHEL 8.6",
        "vcpus": 4,
        "ram_gb": 16,
        "last_patched": "2025-12-15"
      },
      {
        "name": "apm-db-01",
        "type": "Standard_E8s_v5",
        "role": "Database Server (Azure SQL MI)",
        "os": "Managed Instance",
        "vcpus": 8,
        "ram_gb": 64,
        "storage_gb": 512,
        "last_patched": "2025-11-20"
      },
      {
        "name": "apm-web-01",
        "type": "Standard_D2s_v5",
        "role": "Web Server",
        "os": "RHEL 8.6",
        "vcpus": 2,
        "ram_gb": 8,
        "last_patched": "2026-01-10"
      }
    ],
    "network": {
      "vnet": "apm-prod-vnet",
      "firewall": "Azure Firewall",
      "load_balancer": "Azure Application Gateway - Basic SKU",
      "expressroute": false
    },
    "monitoring": {
      "tool": "Dynatrace",
      "alerting": "Email only",
      "coverage": "Partial - servers only, no APM"
    },
    "backup": {
      "solution": "Veeam",
      "frequency": "Daily",
      "retention_days": 30,
      "last_test": "2025-06-15"
    }
  },
  "contract": {
    "type": "Managed Infrastructure",
    "sla": "99.5% availability",
    "support_hours": "8x5",
    "expires": "2027-03-31",
    "monthly_value_eur": 12500
  },
  "notes": "Customer mentioned interest in cloud migration during last QBR"
}
```

### recent_incidents.json

```json
{
  "customer": "AutoParts Manufacturing GmbH",
  "incidents_last_90_days": [
    {
      "id": "INC0089234",
      "date": "2026-01-28",
      "severity": "P3",
      "title": "Slow application response times",
      "status": "Resolved",
      "resolution": "Restarted application server, temporary fix",
      "root_cause": "Memory leak in application - vendor notified",
      "time_to_resolve_hours": 4
    },
    {
      "id": "INC0088901",
      "date": "2026-01-15",
      "severity": "P3",
      "title": "Database connection timeouts",
      "status": "Resolved",
      "resolution": "Increased connection pool size",
      "root_cause": "Insufficient connection pool for peak load",
      "time_to_resolve_hours": 2
    },
    {
      "id": "INC0087456",
      "date": "2025-12-20",
      "severity": "P2",
      "title": "Web server unresponsive",
      "status": "Resolved",
      "resolution": "Emergency failover to backup",
      "root_cause": "Disk full - logs not rotated properly",
      "time_to_resolve_hours": 1.5
    },
    {
      "id": "INC0085123",
      "date": "2025-11-28",
      "severity": "P3",
      "title": "Intermittent network latency",
      "status": "Resolved",
      "resolution": "Identified network congestion during backup window",
      "root_cause": "Backup job overlapping with business hours",
      "time_to_resolve_hours": 6
    }
  ],
  "trend": "Increasing frequency - 4 incidents in 90 days vs 2 in previous quarter",
  "pattern": "Multiple issues related to capacity and performance tuning"
}
```

### customer_context.json

```json
{
  "customer": "AutoParts Manufacturing GmbH",
  "industry": "Manufacturing - Automotive",
  "employees": 450,
  "location": "Munich, Germany",
  "relationship_since": "2022",
  "satisfaction_score": 7.2,
  "last_qbr": "2025-12-10",
  "qbr_notes": [
    "Customer satisfied with support response times",
    "Concerned about aging infrastructure",
    "Asked about cloud options but no budget approved yet",
    "New ERP system planned for 2027 - potential opportunity"
  ],
  "key_contacts": [
    {
      "name": "Thomas Weber",
      "role": "IT Director",
      "email": "t.weber@autoparts-gmbh.de",
      "decision_maker": true,
      "notes": "Technical, prefers detailed explanations"
    },
    {
      "name": "Sandra Müller",
      "role": "CFO",
      "email": "s.mueller@autoparts-gmbh.de",
      "decision_maker": true,
      "notes": "Cost-focused, needs ROI justification"
    }
  ],
  "open_opportunities": [],
  "competitors_mentioned": ["T-Systems", "Atos"]
}
```

### kyndryl_contacts.json

```json
{
  "account_team": {
    "account_manager": {
      "name": "Sarah Mitchell",
      "email": "sarah.mitchell@kyndryl.com",
      "phone": "+49 170 123 4567",
      "responsibility": "Commercial relationship, renewals, expansions"
    },
    "service_delivery_manager": {
      "name": "Marcus Berg",
      "email": "marcus.berg@kyndryl.com",
      "phone": "+49 171 234 5678",
      "responsibility": "Day-to-day service delivery, incident escalations"
    },
    "technical_account_manager": {
      "name": "David Chen",
      "email": "david.chen@kyndryl.com",
      "phone": "+49 172 345 6789",
      "responsibility": "Technical architecture, roadmap, modernization"
    }
  },
  "practice_leads": {
    "cloud": {
      "name": "Anna Kowalski",
      "email": "anna.kowalski@kyndryl.com",
      "expertise": "Cloud migration, Azure, AWS"
    },
    "observability": {
      "name": "Erik Larsson",
      "email": "erik.larsson@kyndryl.com",
      "expertise": "Dynatrace, monitoring, AIOps"
    },
    "security": {
      "name": "James Wilson",
      "email": "james.wilson@kyndryl.com",
      "expertise": "Security operations, compliance"
    },
    "network": {
      "name": "Maria Santos",
      "email": "maria.santos@kyndryl.com",
      "expertise": "Network optimization, SD-WAN"
    }
  }
}
```

---

## Sample Customer Email

### customer_latency_issue.txt

```text
From: t.weber@autoparts-gmbh.de
To: support@kyndryl.com
Subject: Server response issues - need assistance

Hello,

Over the past few days we have been experiencing server response problems.
The application is running slowly and users are complaining that it
"freezes" especially in the afternoon between 14:00-16:00.

We cannot pinpoint the exact cause. Sometimes it's better, sometimes
worse. This morning it was fine, but after lunch problems started again.

Could you please look into this? We have an important presentation
for our biggest customer on Friday and we need the system to work
reliably.

Thank you for a quick response.

Best regards,
Thomas Weber
IT Director
AutoParts Manufacturing GmbH
```

---

## Agent Definitions

### 1. Research Agent

**Úloha:** Zhromaždiť všetky relevantné informácie o probléme a zákazníkovi.

```text
SYSTEM PROMPT:

You are a Research Agent at Kyndryl. Your job is to gather and analyze all
relevant information about a customer issue before recommending solutions.

You have access to:
1. Customer infrastructure details (servers, network, monitoring)
2. Recent incident history
3. Customer context (relationship, preferences, opportunities)

ANALYZE:
- What infrastructure could be causing the reported issue?
- Are there patterns in recent incidents?
- What is the customer's technical environment?
- Any relevant context from relationship history?

OUTPUT FORMAT (JSON):

{
  "customer_summary": {
    "name": "Customer name",
    "contract_type": "Type of contract",
    "relationship_health": "Good/Fair/At risk"
  },

  "reported_issue": {
    "summary": "What they reported",
    "timeframe": "When it happens",
    "business_impact": "Why it matters to them"
  },

  "infrastructure_analysis": {
    "relevant_components": [
      {
        "component": "Server/service name",
        "potential_issue": "What might be wrong",
        "evidence": "Why we think this"
      }
    ],
    "gaps_identified": ["Missing monitoring", "Outdated config", etc.]
  },

  "incident_patterns": {
    "recent_incidents": "Summary of related incidents",
    "trend": "Getting better/worse/stable",
    "recurring_themes": ["Theme 1", "Theme 2"]
  },

  "customer_context": {
    "key_stakeholder": "Who sent the email, their preferences",
    "upcoming_events": "Any important dates mentioned",
    "relationship_notes": "Relevant history"
  },

  "initial_hypotheses": [
    {
      "hypothesis": "What might be causing this",
      "likelihood": "high/medium/low",
      "investigation_needed": "What to check"
    }
  ]
}
```

### 2. Advisor Agent

**Úloha:** Na základe research-u navrhnúť riešenia, identifikovať príležitosti a odporučiť koho konzultovať.

```text
SYSTEM PROMPT:

You are an Advisor Agent at Kyndryl. Based on research about a customer issue,
you recommend solutions, identify business opportunities, and advise who to consult.

Your job:
1. Propose solutions to the immediate problem
2. Identify root causes to prevent recurrence
3. Find opportunities for service improvement (potential revenue)
4. Recommend which Kyndryl colleagues to involve before responding

KYNDRYL CONTACTS AVAILABLE:
- Account Manager: Commercial decisions, customer relationship
- Service Delivery Manager: Operational issues, incident management
- Technical Account Manager: Architecture, technical roadmap
- Practice Leads: Subject matter experts (Cloud, Observability, Security, Network)

OUTPUT FORMAT (JSON):

{
  "immediate_actions": [
    {
      "action": "What to do now",
      "owner": "Who should do it",
      "timeline": "How urgent"
    }
  ],

  "root_cause_analysis": {
    "most_likely_cause": "Primary hypothesis",
    "contributing_factors": ["Factor 1", "Factor 2"],
    "evidence": "Why we believe this"
  },

  "recommended_solutions": [
    {
      "solution": "Description",
      "effort": "Low/Medium/High",
      "impact": "How it helps",
      "timeline": "How long to implement"
    }
  ],

  "improvement_opportunities": [
    {
      "opportunity": "What could be improved",
      "business_value": "Benefit to customer",
      "kyndryl_service": "What we can sell",
      "estimated_revenue": "Potential value",
      "approach": "How to position it"
    }
  ],

  "internal_consultation": {
    "consult_before_responding": [
      {
        "person": "Name",
        "role": "Their role",
        "email": "Email",
        "reason": "Why their input is needed",
        "question_for_them": "Specific question to ask"
      }
    ],
    "inform_after": [
      {
        "person": "Name",
        "role": "Role",
        "reason": "Why they should know"
      }
    ]
  },

  "response_strategy": {
    "tone": "How to communicate",
    "key_messages": ["Message 1", "Message 2"],
    "what_not_to_say": ["Avoid this topic because..."]
  }
}
```

### 3. Response Agent

**Role:** Write a professional draft email with CC to consulted colleagues.

```text
SYSTEM PROMPT:

You are a Response Agent at Kyndryl. You draft professional email responses
to customers based on research and recommendations.

GUIDELINES:
1. Always write in English
2. Be professional but warm
3. Show you understand their urgency
4. Reference specific details from their email
5. Propose concrete next steps
6. Keep it concise (under 200 words for main body)
7. Include appropriate colleagues in CC based on consultation

OUTPUT FORMAT (Markdown):

# Draft Email Response

**To:** [Customer email]
**CC:** [Colleagues who were consulted]
**Subject:** Re: [Original subject]

---

[Professional greeting]

[Acknowledge their email and show understanding of urgency - 1-2 sentences]

[Explain what we found / what we're doing - 2-3 sentences, not too technical]

[Concrete next steps with timeline]

[Reassurance for their important event]

[Professional closing]

---

## Pre-Send Checklist

- [ ] Tone matches situation
- [ ] Facts are correct
- [ ] CC list is appropriate
- [ ] Customer has clear next step

## Internal Notes

**Consulted with:**
- [Person 1] - [Their input summary]
- [Person 2] - [Their input summary]

**Follow-up akcie pre tím:**
- [Action 1]
- [Action 2]

**Obchodné príležitosti na preskúmanie:**
- [Opportunity 1]
```

---

## Demo Script (8-10 minút)

### Minute 0-1: Context Setting

**Mentor hovorí:**

> "Dostali ste email od zákazníka - IT Director píše že majú 'nejaké
> problémy s latenciou'. Vágne, že? Čo spravíte?
>
> Normálne by ste: otvorili ticketing systém, SharePoint, pozreli
> sa na incidenty, zistili kto je account manager, napísali odpoveď...
> Trvá to hodinu, možno viac.
>
> Ukážem vám ako AI agenti spravia research za vás a ešte nájdu
> príležitosť na upsell."

**Mentor zobrazí email:**

```bash
cat sample_emails/customer_latency_issue.txt
```

### Minute 1-3: Research Agent

**Mentor spustí pipeline:**

```bash
python orchestrator.py sample_emails/customer_latency_issue.txt
```

**Na obrazovke:**

```text
╔═══════════════════════════════════════════════════════════════╗
║   🔍 CUSTOMER ISSUE RESOLUTION PIPELINE                       ║
║   Research → Advisor → Response                               ║
╚═══════════════════════════════════════════════════════════════╝

📨 Customer issue: customer_latency_issue.txt
   From: t.weber@autoparts-gmbh.de
   Subject: Problémy s odozvou serverov

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍  RESEARCH AGENT is working...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   → Loading customer infrastructure data...
   → Checking recent incidents...
   → Analyzing customer context...
   → Forming hypotheses...

✓ Research complete
  Customer: AutoParts Manufacturing GmbH
  Contract: €12,500/month, expires 2027-03
  Recent incidents: 4 in last 90 days (trend: increasing)
  Pattern: Capacity and performance issues
  Hypothesis: Database connection pool + backup window overlap
```

**Mentor checkpoint:**

> "Agent zistil že za posledných 90 dní mali 4 incidenty - dvojnásobok
> oproti predchádzajúcemu kvartálu. Vidí pattern: problémy s kapacitou.
> Hypotéza je database connection pool alebo backup window.
> Schvaľujem research, ideme k odporúčaniam."

### Minute 3-5: Advisor Agent

**Na obrazovke:**

```text
✅ Research complete → Handing off to Advisor Agent

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡  ADVISOR AGENT is working...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   → Analyzing root causes...
   → Formulating solutions...
   → Identifying business opportunities...
   → Finding internal experts to consult...

✓ Recommendations ready

  IMMEDIATE: Check DB connection pool, review backup schedule

  ROOT CAUSE: Insufficient capacity + no APM monitoring

  💰 UPSELL OPPORTUNITIES:
     • Full Dynatrace APM    → ~€3,000/month
     • 24x7 support upgrade  → ~€2,500/month
     • Proactive monitoring  → ~€1,500/month

  📞 CONSULT BEFORE RESPONDING:
     • Marcus Berg (SDM) - incident coordination
     • Erik Larsson (Observability) - monitoring gap
     • Sarah Mitchell (AM) - upsell approach
```

**Mentor checkpoint:**

> "Toto je zaujímavé! Agent nielen navrhol riešenie, ale našiel že
> zákazník má slabý monitoring - len servery, žiadny APM. To je
> príležitosť na €3,000 mesačne.
>
> A hovorí nám: pred odpoveďou konzultuj s Service Delivery Managerom
> a Observability Practice Leadom. Account Managerku informuj o upselle.
>
> Schvaľujem, ideme písať odpoveď."

### Minute 5-7: Response Agent

**Na obrazovke:**

```text
✅ Advisor complete → Handing off to Response Agent

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✍️  RESPONSE AGENT is working...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   → Drafting professional response...
   → Adding CC for consulted colleagues...
   → Including next steps...
   → Preparing internal notes...

✓ Draft ready
```

**Mentor opens draft and reads:**

```text
To: t.weber@autoparts-gmbh.de
CC: marcus.berg@kyndryl.com, erik.larsson@kyndryl.com
Subject: Re: Server response issues - need assistance

Dear Mr. Weber,

Thank you for reporting this issue. I understand the urgency given
your important presentation on Friday.

We have analyzed your Azure infrastructure and identified a likely
cause - a combination of database connection pool settings and
backup job timing during business hours. Our team is already working
on configuration adjustments.

Proposed next steps:
1. Today afternoon: Move backup window outside peak hours (14-16h)
2. Tomorrow morning: Optimize DB connection pool
3. Before Friday: Stability verification test

I will call you today at 15:00 with an update. If this time doesn't
work for you, please let me know.

Best regards,
[Your name]
Kyndryl Service Team

---

CC: Marcus Berg (SDM), Erik Larsson (Observability Lead)
```

### Minute 7-8: Review & Discussion

**Mentor:**

> "Notice a few things:
> 1. Email is professional and addresses Mr. Weber by name
> 2. CC includes colleagues we consulted (SDM, Observability Lead)
> 3. Concrete steps with specific times
> 4. References Friday presentation - agent picked that up from the email
>
> And in the internal notes we have follow-up on upsell monitoring services."

### Minute 8-10: Key Takeaways

**Mentor otázky:**

1. "Koľko času by vám trvalo spraviť tento research manuálne?"
2. "Agent našiel €7,000/mesiac potenciálnej novej revenue. Všimli by ste si to?"
3. "Čo by ste v odpovedi zmenili pred odoslaním?"
4. "Kde je riziko ak by agent odpovedal automaticky bez schválenia?"

---

## Orchestrator Code (orchestrator.py)

```python
#!/usr/bin/env python3
"""
Customer Issue Resolution Pipeline
Day 1 Demo - AI Academy 2026

Pipeline: Research → Advisor → Response
"""

import os
import sys
import json
import time
from anthropic import Anthropic

# ═══════════════════════════════════════════════════════════════
# Terminal Colors
# ═══════════════════════════════════════════════════════════════

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

def print_banner():
    print(f"\n{Colors.CYAN}{Colors.BOLD}")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║   🔍 CUSTOMER ISSUE RESOLUTION PIPELINE                       ║")
    print("║                                                               ║")
    print("║   🔍 Research → 💡 Advisor → ✍️  Response                      ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}")

def print_agent_start(agent_name: str, emoji: str, tasks: list[str]):
    print(f"\n{Colors.BOLD}{'━' * 60}{Colors.END}")
    print(f"{emoji}  {Colors.BOLD}{agent_name}{Colors.END} is working...")
    print(f"{Colors.DIM}{'━' * 60}{Colors.END}")
    for task in tasks:
        print(f"   {Colors.DIM}→ {task}{Colors.END}")
        time.sleep(0.3)  # Visual effect
    print()

def print_handoff(from_agent: str, to_agent: str):
    print(f"\n{Colors.GREEN}{'─' * 60}")
    print(f"✅ {from_agent} complete")
    print(f"📤 Handing off to {to_agent}...")
    print(f"{'─' * 60}{Colors.END}\n")
    time.sleep(0.5)

def ask_approval(agent_name: str, output_file: str) -> bool:
    print(f"\n{Colors.YELLOW}{'─' * 60}")
    print(f"🔍 {agent_name} output saved to: {Colors.BOLD}{output_file}{Colors.END}")
    print(f"{Colors.YELLOW}{'─' * 60}{Colors.END}")
    response = input(f"\n{Colors.BOLD}[SUPERVISOR] Approve and continue? [Y/n]: {Colors.END}").strip().lower()
    return response in ['', 'y', 'yes']

def save_output(filename: str, content: str):
    os.makedirs("output", exist_ok=True)
    filepath = f"output/{filename}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def load_mock_data():
    """Load all mock data files"""
    data = {}
    mock_files = [
        ("infrastructure", "mock_data/customer_infrastructure.json"),
        ("incidents", "mock_data/recent_incidents.json"),
        ("context", "mock_data/customer_context.json"),
        ("contacts", "mock_data/kyndryl_contacts.json")
    ]

    for key, filepath in mock_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data[key] = json.load(f)
        except FileNotFoundError:
            print(f"{Colors.YELLOW}Warning: {filepath} not found, using empty data{Colors.END}")
            data[key] = {}

    return data

def run_agent(client: Anthropic, system_prompt: str, user_input: str, expect_json: bool = False) -> str | dict:
    """Run an agent and return the response"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_input}]
    )
    text = response.content[0].text

    if expect_json:
        # Clean up potential markdown code blocks
        if "```json" in text:
            text = text.split("```json")[1]
        elif "```" in text:
            text = text.split("```")[1]
        if "```" in text:
            text = text.split("```")[0]
        return json.loads(text.strip())

    return text

# ═══════════════════════════════════════════════════════════════
# Agent System Prompts
# ═══════════════════════════════════════════════════════════════

RESEARCH_AGENT_PROMPT = """You are a Research Agent at Kyndryl. Your job is to gather and analyze all relevant information about a customer issue.

You have access to:
- Customer infrastructure details (servers, network, monitoring setup)
- Recent incident history
- Customer context (relationship, preferences, upcoming events)

ANALYZE:
1. What infrastructure components could be causing the issue?
2. Are there patterns in recent incidents?
3. What monitoring/visibility gaps exist?
4. What is the customer's context and urgency?

OUTPUT FORMAT (JSON only, no markdown):
{
  "customer_summary": {
    "name": "Customer name",
    "contract_value": "Monthly value",
    "relationship_health": "Good/Fair/At risk"
  },
  "reported_issue": {
    "summary": "What they reported",
    "timeframe": "When it occurs",
    "business_impact": "Why it matters (e.g., important event)"
  },
  "infrastructure_analysis": {
    "relevant_components": [
      {"component": "Name", "potential_issue": "What might be wrong", "evidence": "Why"}
    ],
    "gaps_identified": ["Gap 1", "Gap 2"]
  },
  "incident_patterns": {
    "count_90_days": "Number",
    "trend": "Increasing/Stable/Decreasing",
    "recurring_themes": ["Theme 1", "Theme 2"]
  },
  "customer_context": {
    "contact_preferences": "How they like to communicate",
    "upcoming_events": "Important dates",
    "relationship_notes": "Relevant history"
  },
  "hypotheses": [
    {"hypothesis": "What might cause this", "likelihood": "high/medium/low"}
  ]
}"""


ADVISOR_AGENT_PROMPT = """You are an Advisor Agent at Kyndryl. Based on research, you recommend solutions and identify business opportunities.

Your job:
1. Propose solutions to fix the immediate problem
2. Identify root causes
3. Find opportunities for service improvements (potential new revenue!)
4. Recommend which Kyndryl colleagues to consult before responding

ALWAYS LOOK FOR UPSELL OPPORTUNITIES:
- Missing monitoring → Observability services
- Capacity issues → Infrastructure upgrade
- 8x5 support hitting limits → 24x7 upgrade
- Manual processes → Automation services
- Security gaps → Security services

OUTPUT FORMAT (JSON only, no markdown):
{
  "immediate_actions": [
    {"action": "What to do", "owner": "Who", "timeline": "When"}
  ],
  "root_cause": {
    "primary_cause": "Most likely cause",
    "contributing_factors": ["Factor 1", "Factor 2"],
    "evidence": "Why we believe this"
  },
  "solutions": [
    {"solution": "Description", "effort": "Low/Medium/High", "impact": "Benefit"}
  ],
  "upsell_opportunities": [
    {
      "opportunity": "What to sell",
      "customer_benefit": "Why they need it",
      "estimated_monthly_revenue": "EUR amount",
      "positioning": "How to present it"
    }
  ],
  "internal_consultation": {
    "consult_before_responding": [
      {
        "name": "Person name",
        "role": "Their role",
        "email": "Email",
        "reason": "Why consult them",
        "question": "What to ask"
      }
    ],
    "inform_after": [
      {"name": "Name", "role": "Role", "reason": "Why inform"}
    ]
  },
  "response_strategy": {
    "tone": "How to communicate",
    "key_messages": ["Message 1", "Message 2"],
    "avoid": ["What not to say"]
  }
}"""


RESPONSE_AGENT_PROMPT = """You are a Response Agent at Kyndryl. You draft professional email responses.

IMPORTANT RULES:
1. Always write in English
2. Be professional but warm
3. Show you understand their urgency
4. Propose concrete next steps with times
5. Add consulted colleagues to CC
6. Keep main body under 150 words

OUTPUT FORMAT (Markdown):

# Draft Email

**To:** [Customer email]
**CC:** [Consulted colleagues - name and email]
**Subject:** Re: [Original subject]

---

[Greeting in customer's language]

[Acknowledge email and urgency - 1-2 sentences]

[What we found / what we're doing - 2-3 sentences, not too technical]

[Concrete next steps with timeline - numbered list]

[Reassurance about their important event if mentioned]

[Professional closing]

---

## Pre-Send Checklist

- [ ] Tone matches situation
- [ ] Facts are correct
- [ ] CC list is appropriate
- [ ] Next steps are clear

## Internal Notes (DO NOT SEND)

**Consulted with:**
- [Name]: [Their input]

**Follow-up actions:**
- [Action 1]

**Revenue opportunities to pursue:**
- [Opportunity with value]
"""

# ═══════════════════════════════════════════════════════════════
# Main Pipeline
# ═══════════════════════════════════════════════════════════════

def main():
    if len(sys.argv) < 2:
        print(f"{Colors.RED}Usage: python orchestrator.py <email_file.txt>{Colors.END}")
        print(f"{Colors.DIM}Example: python orchestrator.py sample_emails/customer_latency_issue.txt{Colors.END}")
        sys.exit(1)

    email_file = sys.argv[1]

    # Read the email
    try:
        with open(email_file, 'r', encoding='utf-8') as f:
            email_content = f.read()
    except FileNotFoundError:
        print(f"{Colors.RED}Error: File '{email_file}' not found{Colors.END}")
        sys.exit(1)

    # Load mock data
    mock_data = load_mock_data()

    client = Anthropic()

    print_banner()

    # Show email preview
    lines = email_content.strip().split('\n')
    from_line = next((l for l in lines if l.startswith('From:')), 'Unknown sender')
    subject_line = next((l for l in lines if l.startswith('Subject:')), 'No subject')

    print(f"📨 {Colors.BOLD}Customer issue:{Colors.END} {email_file}")
    print(f"   {from_line}")
    print(f"   {subject_line}")
    time.sleep(1)

    # ═══════════════════════════════════════════════════════
    # AGENT 1: Research
    # ═══════════════════════════════════════════════════════
    print_agent_start(
        "RESEARCH AGENT",
        "🔍",
        ["Loading customer infrastructure data...",
         "Checking recent incidents...",
         "Analyzing customer context...",
         "Forming hypotheses..."]
    )

    research_input = f"""
Customer email:
{email_content}

Customer infrastructure:
{json.dumps(mock_data.get('infrastructure', {}), indent=2)}

Recent incidents:
{json.dumps(mock_data.get('incidents', {}), indent=2)}

Customer context:
{json.dumps(mock_data.get('context', {}), indent=2)}

Analyze this customer issue based on all available data.
"""

    research = run_agent(client, RESEARCH_AGENT_PROMPT, research_input, expect_json=True)
    research_file = save_output("01_research.json", json.dumps(research, indent=2, ensure_ascii=False))

    print(f"\n{Colors.GREEN}✓ Research complete{Colors.END}")
    print(f"  Customer: {Colors.BOLD}{research.get('customer_summary', {}).get('name', 'N/A')}{Colors.END}")
    incidents = research.get('incident_patterns', {})
    print(f"  Recent incidents: {incidents.get('count_90_days', 'N/A')} (trend: {incidents.get('trend', 'N/A')})")
    if research.get('hypotheses'):
        top_hypothesis = research['hypotheses'][0]
        print(f"  Top hypothesis: {top_hypothesis.get('hypothesis', 'N/A')}")

    if not ask_approval("Research Agent", research_file):
        print(f"{Colors.RED}Pipeline stopped.{Colors.END}")
        sys.exit(0)

    print_handoff("Research Agent", "Advisor Agent")

    # ═══════════════════════════════════════════════════════
    # AGENT 2: Advisor
    # ═══════════════════════════════════════════════════════
    print_agent_start(
        "ADVISOR AGENT",
        "💡",
        ["Analyzing root causes...",
         "Formulating solutions...",
         "Identifying business opportunities...",
         "Finding internal experts to consult..."]
    )

    advisor_input = f"""
Research findings:
{json.dumps(research, indent=2)}

Kyndryl contacts available:
{json.dumps(mock_data.get('contacts', {}), indent=2)}

Based on this research, provide recommendations including:
1. Immediate actions
2. Root cause analysis
3. Solutions
4. Upsell opportunities (IMPORTANT: look for revenue potential!)
5. Who to consult internally before responding
"""

    recommendations = run_agent(client, ADVISOR_AGENT_PROMPT, advisor_input, expect_json=True)
    advisor_file = save_output("02_recommendations.json", json.dumps(recommendations, indent=2, ensure_ascii=False))

    print(f"\n{Colors.GREEN}✓ Recommendations ready{Colors.END}")

    # Show immediate actions
    if recommendations.get('immediate_actions'):
        print(f"\n  {Colors.BOLD}IMMEDIATE:{Colors.END} {recommendations['immediate_actions'][0].get('action', 'N/A')}")

    # Show upsell opportunities
    upsells = recommendations.get('upsell_opportunities', [])
    if upsells:
        print(f"\n  {Colors.YELLOW}💰 UPSELL OPPORTUNITIES:{Colors.END}")
        total_revenue = 0
        for opp in upsells[:3]:
            revenue = opp.get('estimated_monthly_revenue', '€0')
            print(f"     • {opp.get('opportunity', 'N/A')} → {revenue}/month")
            # Try to extract numeric value
            try:
                num = int(''.join(filter(str.isdigit, str(revenue))))
                total_revenue += num
            except:
                pass
        if total_revenue > 0:
            print(f"     {Colors.BOLD}Total potential: ~€{total_revenue:,}/month{Colors.END}")

    # Show who to consult
    consult = recommendations.get('internal_consultation', {}).get('consult_before_responding', [])
    if consult:
        print(f"\n  {Colors.CYAN}📞 CONSULT BEFORE RESPONDING:{Colors.END}")
        for person in consult[:3]:
            print(f"     • {person.get('name', 'N/A')} ({person.get('role', 'N/A')})")

    if not ask_approval("Advisor Agent", advisor_file):
        print(f"{Colors.RED}Pipeline stopped.{Colors.END}")
        sys.exit(0)

    print_handoff("Advisor Agent", "Response Agent")

    # ═══════════════════════════════════════════════════════
    # AGENT 3: Response
    # ═══════════════════════════════════════════════════════
    print_agent_start(
        "RESPONSE AGENT",
        "✍️",
        ["Drafting professional response...",
         "Adding CC for consulted colleagues...",
         "Including concrete next steps...",
         "Preparing internal notes..."]
    )

    response_input = f"""
Original customer email:
{email_content}

Research findings:
{json.dumps(research, indent=2)}

Recommendations:
{json.dumps(recommendations, indent=2)}

Draft a professional email response in English.
Include consulted colleagues in CC.
"""

    draft = run_agent(client, RESPONSE_AGENT_PROMPT, response_input, expect_json=False)
    response_file = save_output("03_draft_email.md", draft)

    print(f"\n{Colors.GREEN}✓ Draft email ready{Colors.END}")

    # ═══════════════════════════════════════════════════════
    # DONE
    # ═══════════════════════════════════════════════════════
    print(f"\n{Colors.GREEN}{Colors.BOLD}")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║  ✅ ISSUE RESOLUTION COMPLETE                                 ║")
    print("║                                                               ║")
    print("║  Output files:                                                ║")
    print("║    🔍 output/01_research.json        (Research)               ║")
    print("║    💡 output/02_recommendations.json (Recommendations)        ║")
    print("║    ✍️  output/03_draft_email.md       (Draft Email)            ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}")

    print(f"\n{Colors.CYAN}Next steps:{Colors.END}")
    print("  1. Review the draft: cat output/03_draft_email.md")
    print("  2. Consult with recommended colleagues")
    print("  3. Adjust tone/content as needed")
    print("  4. Send manually from your email client")
    print()

if __name__ == "__main__":
    main()
```

---

## Key Learning Points

Po demo mentor zhrnie:

| Bod | Vysvetlenie |
|-----|-------------|
| **Agent ako researcher** | Ušetrí hodiny manuálneho hľadania |
| **Knowledge grounding** | Používa reálne dáta (infra, incidenty, kontext) |
| **Revenue finder** | Identifikuje príležitosti ktoré by ste prehliadli |
| **Organizational navigator** | Vie koho zapojiť podľa typu problému |
| **Human stays in control** | Konzultácia a odoslanie je vždy manuálne |

---

## Rozšírenie Pre Production

V reálnom nasadení by pipeline mal:

| Komponent | Integrácia |
|-----------|------------|
| **Email** | Microsoft Graph API (Outlook) |
| **Infraštruktúra** | ServiceNow CMDB |
| **Incidenty** | ServiceNow Incident Management |
| **Zákazník kontext** | Salesforce / Dynamics CRM |
| **Kyndryl kontakty** | SharePoint / Active Directory |
| **Upsell tracking** | CRM Opportunity creation |

---

*Demo vytvorené pre AI Academy 2026 - Day 1: AI Landscape*
*"Agents act, humans supervise"*
