# 🚀 AI Academy - Starter Kit

**Všetko čo potrebuješ na začiatok s Agentic AI. Zadarmo.**

```
⏱️ Setup: 15 minút
💰 Cena: $0
🎯 Výsledok: Funkčný AI agent
```

---

## 🏃 Quick Start (3 kroky)

### Krok 1: Vytvor účty (5 min)

| Služba | Link | Čo potrebuješ |
|--------|------|---------------|
| Google | [aistudio.google.com](https://aistudio.google.com) | → Get API Key → Create |
| HuggingFace | [huggingface.co/join](https://huggingface.co/join) | → Settings → Access Tokens |

### Krok 2: Otvor Setup Notebook (1 min)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/00_Setup.ipynb)

> ☝️ Klikni na badge alebo otvor `notebooks/00_Setup.ipynb` v Google Colab

### Krok 3: Pridaj API Key (2 min)

1. V Colab klikni 🔑 (Secrets) v ľavom paneli
2. **Add new secret:**
   - Name: `GOOGLE_API_KEY`
   - Value: *tvoj API kľúč z AI Studio*
3. Toggle "Notebook access" → **ON**
4. Spusti prvú bunku → Hotovo! ✅

---

## 📚 Notebooky

| # | Notebook | Popis | Colab |
|---|----------|-------|-------|
| 00 | [Setup](notebooks/00_Setup.ipynb) | Konfigurácia a test | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/00_Setup.ipynb) |
| 01 | [First Agent](notebooks/01_First_Agent.ipynb) | Základný agent | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/01_First_Agent.ipynb) |
| 02 | [Tools Agent](notebooks/02_Tools_Agent.ipynb) | Agent s nástrojmi | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/02_Tools_Agent.ipynb) |
| 03 | [RAG Agent](notebooks/03_RAG_Agent.ipynb) | Retrieval-Augmented Generation | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/03_RAG_Agent.ipynb) |
| 04 | [Multi-Agent](notebooks/04_Multi_Agent.ipynb) | Viac agentov spolupracuje | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lubor-fedak/AI-Academy-Knowledge/blob/main/starter-kit/notebooks/04_Multi_Agent.ipynb) |

---

## 🆓 Free Tier Limity

| Služba | Limit | Poznámka |
|--------|-------|----------|
| Gemini Flash | 1,500 req/deň | Hlavný model |
| Gemini Pro | 50 req/deň | Pre komplexné úlohy |
| Colab GPU | ~4h/deň | Voliteľné |
| HF Spaces | Unlimited | CPU hosting |

---

## 🆘 Troubleshooting

<details>
<summary><b>❌ "API key not valid"</b></summary>

1. Choď na [aistudio.google.com](https://aistudio.google.com)
2. Get API Key → Create new key
3. Skopíruj a aktualizuj v Colab Secrets
</details>

<details>
<summary><b>❌ "429 Too Many Requests"</b></summary>

- Počkaj 60 sekúnd
- Alebo použi `gemini-2.0-flash` namiesto `gemini-2.5-pro`
</details>

<details>
<summary><b>❌ "Module not found"</b></summary>

Spusti v novej bunke:
```python
!pip install google-generativeai smolagents litellm
```
</details>

<details>
<summary><b>❌ Colab sa zasekol</b></summary>

Runtime → Restart runtime → Spusti setup bunku znova
</details>

---

## 📁 Štruktúra Repozitára

```
ai-academy-starter/
├── README.md              # Tento súbor
├── notebooks/
│   ├── 00_Setup.ipynb     # Setup a test
│   ├── 01_First_Agent.ipynb
│   ├── 02_Tools_Agent.ipynb
│   ├── 03_RAG_Agent.ipynb
│   └── 04_Multi_Agent.ipynb
├── templates/
│   ├── app.py             # HuggingFace Spaces template
│   └── requirements.txt
└── docs/
    └── SETUP_GUIDE.md     # Detailný setup guide
```

---

## 🔗 Užitočné Linky

- [Google AI Studio](https://aistudio.google.com) - API kľúče
- [Google Colab](https://colab.research.google.com) - Notebooky
- [HuggingFace Spaces](https://huggingface.co/spaces) - Deployment
- [smolagents Docs](https://huggingface.co/docs/smolagents) - Framework

---

## 📞 Podpora

- 💬 Teams: `#ai-academy-help`
- 📧 Email: ai-academy@kyndryl.com
- 🕐 Office Hours: [kalendár]

---

*Kyndryl AI Academy 2026*
