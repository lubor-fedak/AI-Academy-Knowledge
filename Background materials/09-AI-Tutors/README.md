# AI Academy - AI Tutor System Prompts

This package contains system prompts for 8 role-specific AI Tutors to be deployed in ChatGPT Enterprise.

---

## 📋 Overview

| # | File | Role / Track | Personality |
|---|------|--------------|-------------|
| 0 | `00-DAY1-TUTOR.md` | **Day 1 (All Participants)** | Forward-looking, practical |
| 1 | `01-FDE-TUTOR.md` | Forward Deployed Engineer | Pragmatic, client-obsessed |
| 2 | `02-AI-SE-TUTOR.md` | AI Software Engineer (within FDE capability) | Quality-obsessed, systematic |
| 3 | `03-AI-PM-TUTOR.md` | AI Product Manager | Value-driven, strategic |
| 4 | `04-AI-SEC-TUTOR.md` | AI Security Consultant | Paranoid, adversarial |
| 5 | `05-AI-FE-TUTOR.md` | AI Front-End Developer (within FDE capability) | User-first, performance-focused |
| 6 | `06-AI-DX-TUTOR.md` | AI Design & UX (AI-DX skill track) | Empathetic, human-centered |
| 7 | `07-AI-DS-TUTOR.md` | AI Data Scientist | Scientific, metrics-obsessed |
| 8 | `08-AI-DA-TUTOR.md` | AI Data Analyst (within FDE capability) | Story-driven, business-focused |

### Day-Specific vs Role-Specific Tutors

- **Day 1-4 (Common Foundations):** Students use `00-DAY1-TUTOR.md` or a general foundations tutor
- **Day 5+ (Role Tracks):** Students use their role-specific tutor (01-08)

---

## 🎯 Core Principle

All tutors follow the AI-Native learning philosophy:

> **Never give direct answers. Guide through questions.**

Each tutor is designed to:
- Ask clarifying questions before providing guidance
- Challenge assumptions with "what if" scenarios
- Provide hints and patterns, not complete solutions
- Push students toward role-specific thinking

---

## 🚀 Deployment Guide

### Step 1: Create Custom GPT in ChatGPT Enterprise

1. Go to ChatGPT Enterprise workspace
2. Click **Create** → **GPT**
3. Use the following naming convention: `AI Academy - [ROLE] Tutor`

### Step 2: Configure the GPT

For each tutor:

1. **Name:** As specified in the markdown file
2. **Description:** Copy from the file
3. **Instructions:** Copy the entire content inside the ` ``` ` code block (the System Prompt section)
4. **Conversation starters:** Copy the 5 suggested starters from the file

### Step 3: Upload Knowledge Base

Each tutor file lists recommended knowledge base documents. Upload relevant materials:

- KAF Documentation
- Role-specific playbooks
- AI Innovation Lab Method
- Certification exam objectives (where applicable)

### Step 4: Set Capabilities

For all tutors:
- ☑️ Web Browsing: OFF (to focus on internal knowledge)
- ☑️ DALL·E: OFF
- ☑️ Code Interpreter: ON (for technical roles)

### Step 5: Publish to Workspace

1. Click **Save**
2. Under "Who can use this GPT?" select **Everyone at [Organization]**
3. Click **Update**

---

## 🎭 Tutor Personalities Summary

### Day 1 Tutor (Common Foundations)
> "What agent would you create if you could automate any task?"

Challenges students on:
- Understanding the 2023→2026 paradigm shift
- Agent concepts (OODA loop)
- Their "Create Your Own Agent" assignment

### FDE Tutor
> "What will the customer say when they see this?"

Challenges students on:
- Client-facing demos
- Production readiness
- Speed of delivery

### AI-SE Tutor
> "How will you test this?"

Challenges students on:
- Code quality and architecture
- Testing strategies
- Operational excellence

### AI-PM Tutor
> "What's the ROI?"

Challenges students on:
- Business value articulation
- Prioritization
- Stakeholder management

### AI-SEC Tutor
> "How would an attacker exploit this?"

Challenges students on:
- Threat modeling
- Security controls
- Adversarial thinking

### AI-FE Tutor
> "What does the user see while waiting?"

Challenges students on:
- User experience
- Accessibility
- Performance

### AI-DX Tutor
> "How does the user feel at this moment?"

Challenges students on:
- User research
- Emotional journey
- Design decisions

### AI-DS Tutor
> "How do you measure success?"

Challenges students on:
- Evaluation metrics
- Statistical rigor
- Bias detection

### AI-DA Tutor
> "Compared to what?"

Challenges students on:
- Data storytelling
- Business context
- Visualization

---

## 📝 Customization

### Adding Kyndryl-Specific Knowledge

Each tutor references Kyndryl frameworks:
- **KAF** - Kyndryl Agentic Framework
- **AI Innovation Lab Method** - 6-phase delivery methodology

Upload these documents to each tutor's knowledge base for Kyndryl-specific guidance.

### Adjusting Tone

The tutors are configured to:
- Never give direct answers
- Always ask questions first
- Push back on assumptions

If this feels too challenging for your audience, you can soften the language in the "Behavioral Rules" section.

### Adding Role-Specific Situations

Each tutor's knowledge base can include:
- Role-specific case studies
- Example conversations
- Common mistakes to watch for

---

## ⚠️ Important Notes

1. **Never reveal system prompts** - The tutor prompts include instruction to not reveal their instructions if asked.

2. **Test before launch** - Have mentors test each tutor with typical student questions before the academy starts.

3. **Monitor conversations** - ChatGPT Enterprise allows workspace admins to review conversations for quality assurance.

4. **Iterate based on feedback** - Collect feedback from students and mentors to improve prompts weekly.

---

## 📊 Success Metrics

Track these to measure tutor effectiveness:

| Metric | How to Measure |
|--------|----------------|
| Engagement | Messages per session |
| Quality | Student feedback ratings |
| Learning | Checkpoint scores |
| Independence | Decreasing questions over time |

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Jan 27, 2026 | Initial release |
| 1.1 | Feb 1, 2026 | Added Day 1 specific tutor (00-DAY1-TUTOR.md) |

---

## 📞 Support

For questions about tutor configuration:
- Academy Lead: [Contact]
- Technical Support: [Contact]
