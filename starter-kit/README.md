# 🚀 AI Academy - Starter Kit

**Everything you need to start with Agentic AI. For free.**

```
⏱️ Setup: 15 minutes
💰 Cost: $0
🎯 Result: Working AI agent
```

---

## 🏃 Quick Start (3 steps)

### Step 1: Create accounts (5 min)

| Service | Link | What you need |
|---------|------|---------------|
| Google | [aistudio.google.com](https://aistudio.google.com) | → Get API Key → Create |
| HuggingFace | [huggingface.co/join](https://huggingface.co/join) | → Settings → Access Tokens |

### Step 2: Open Setup Notebook (1 min)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/00_Setup.ipynb)

> ☝️ Click the badge or open `notebooks/00_Setup.ipynb` in Google Colab

### Step 3: Add API Key (2 min)

1. In Colab, click 🔑 (Secrets) in the left panel
2. **Add new secret:**
   - Name: `GOOGLE_API_KEY`
   - Value: *your API key from AI Studio*
3. Toggle "Notebook access" → **ON**
4. Run the first cell → Done! ✅

---

## 📚 Notebooks

| # | Notebook | Description | Colab |
|---|----------|-------------|-------|
| 00 | [Setup](notebooks/00_Setup.ipynb) | Configuration and test | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/00_Setup.ipynb) |
| 01 | [First Agent](notebooks/01_First_Agent.ipynb) | Basic agent | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/01_First_Agent.ipynb) |
| 02 | [Tools Agent](notebooks/02_Tools_Agent.ipynb) | Agent with tools | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/02_Tools_Agent.ipynb) |
| 03 | [RAG Agent](notebooks/03_RAG_Agent.ipynb) | Retrieval-Augmented Generation | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/03_RAG_Agent.ipynb) |
| 04 | [Multi-Agent](notebooks/04_Multi_Agent.ipynb) | Multiple agents working together | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/04_Multi_Agent.ipynb) |

---

## 🆓 Free Tier Limits

| Service | Limit | Notes |
|---------|-------|-------|
| Gemini Flash | 1,500 req/day | Main model |
| Gemini Pro | 50 req/day | For complex tasks |
| Colab GPU | ~4h/day | Optional |
| HF Spaces | Unlimited | CPU hosting |

---

## 🆘 Troubleshooting

<details>
<summary><b>❌ "API key not valid"</b></summary>

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Get API Key → Create new key
3. Copy and update in Colab Secrets
</details>

<details>
<summary><b>❌ "429 Too Many Requests"</b></summary>

- Wait 60 seconds
- Or use `gemini-2.0-flash` instead of `gemini-2.5-pro`
</details>

<details>
<summary><b>❌ "Module not found"</b></summary>

Run in a new cell:
```python
!pip install google-generativeai smolagents litellm
```
</details>

<details>
<summary><b>❌ Colab is stuck</b></summary>

Runtime → Restart runtime → Run setup cell again
</details>

---

## 📁 Repository Structure

```
starter-kit/
├── README.md              # This file
├── notebooks/
│   ├── 00_Setup.ipynb     # Setup and test
│   ├── 01_First_Agent.ipynb
│   ├── 02_Tools_Agent.ipynb
│   ├── 03_RAG_Agent.ipynb
│   └── 04_Multi_Agent.ipynb
├── templates/
│   ├── app.py             # HuggingFace Spaces template
│   └── requirements.txt
└── docs/
    └── SETUP_GUIDE.md     # Detailed setup guide
```

---

## 🔗 Useful Links

- [Google AI Studio](https://aistudio.google.com) - API keys
- [Google Colab](https://colab.research.google.com) - Notebooks
- [HuggingFace Spaces](https://huggingface.co/spaces) - Deployment
- [smolagents Docs](https://huggingface.co/docs/smolagents) - Framework

---

## 📞 Support

- 💬 Teams: `#ai-academy-help`
- 📧 Email: ai-academy@kyndryl.com
- 🕐 Office Hours: [calendar]

---

*Kyndryl AI Academy 2026*
