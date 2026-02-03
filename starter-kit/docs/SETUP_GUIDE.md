# 📖 Detailný Setup Guide

Kompletný návod pre účastníkov AI Academy.

---

## Predpoklady

- Internetové pripojenie
- Webový prehliadač (Chrome/Firefox/Edge)
- Základná znalosť Python (nemusíš byť expert)

---

## Krok 1: Google Account (2 min)

Ak už máš Gmail, tento krok preskoč.

1. Choď na https://accounts.google.com/signup
2. Vyplň údaje
3. Potvrď telefónne číslo
4. Hotovo ✅

---

## Krok 2: Google AI Studio - API Key (5 min)

### 2.1 Prístup
1. Otvor https://aistudio.google.com
2. Klikni "Sign in with Google"
3. Použi svoj Google účet
4. Akceptuj Terms of Service

### 2.2 Vytvorenie API kľúča
1. V ľavom menu klikni **"Get API key"**
2. Klikni **"Create API key"**
3. Vyber **"Create API key in new project"**
4. Počkaj pár sekúnd
5. **Skopíruj API kľúč** (vyzerá ako `AIzaSy...`)

### 2.3 Ulož API kľúč bezpečne
- Ulož do password managera
- ALEBO do súkromného dokumentu
- **NIKDY** nedávaj do verejného kódu!

---

## Krok 3: Google Colab (3 min)

### 3.1 Otvorenie notebooku

**Možnosť A: Priamy link**
- Klikni na "Open in Colab" badge v README

**Možnosť B: Manuálne**
1. Choď na https://colab.research.google.com
2. File → Open notebook
3. GitHub tab
4. Zadaj URL repozitára
5. Vyber notebook

### 3.2 Nastavenie API kľúča v Colab

1. V ľavom paneli nájdi ikonu 🔑 (Secrets)
2. Klikni na ňu
3. Klikni **"Add new secret"**
4. Vyplň:
   - **Name:** `GOOGLE_API_KEY`
   - **Value:** *vlož svoj API kľúč*
5. Klikni na toggle **"Notebook access"** → zapni ho
6. Hotovo ✅

### 3.3 Verifikácia

Spusti túto bunku v notebooku:

```python
from google.colab import userdata
key = userdata.get('GOOGLE_API_KEY')
print(f"✅ API key loaded: {key[:10]}...")
```

Ak vidíš chybu, skontroluj:
- Je secret pomenovaný presne `GOOGLE_API_KEY`?
- Je toggle "Notebook access" zapnutý?

---

## Krok 4: HuggingFace Account (voliteľné, 3 min)

Pre deployment agentov.

### 4.1 Registrácia
1. Choď na https://huggingface.co/join
2. Vyplň: Username, Email, Password
3. Klikni "Sign Up"
4. Potvrď email

### 4.2 Access Token
1. Klikni na avatar → Settings
2. V ľavom menu: Access Tokens
3. Klikni "Create new token"
4. Name: `ai-academy`
5. Role: `write`
6. Skopíruj token

---

## Troubleshooting

### "API key not valid"

**Príčina:** Nesprávny alebo expirovaný kľúč

**Riešenie:**
1. Choď na https://aistudio.google.com
2. Get API key → Create new key
3. Aktualizuj v Colab Secrets

### "429 Too Many Requests"

**Príčina:** Prekročený rate limit

**Riešenie:**
- Počkaj 60 sekúnd
- Použi `gemini-2.0-flash` namiesto `gemini-2.5-pro`

### "ModuleNotFoundError"

**Príčina:** Knižnica nie je nainštalovaná

**Riešenie:**
```python
!pip install google-generativeai smolagents litellm
```

### Colab sa zasekol

**Riešenie:**
1. Runtime → Restart runtime
2. Spusti setup bunku znova
3. Ak nepomôže: Runtime → Disconnect and delete runtime

### GPU nie je dostupné

**Príčina:** Vysoký dopyt, free tier vyčerpaný

**Riešenie:**
- Skús neskôr
- Použi CPU runtime (pomalšie ale funguje)
- Alternatíva: Kaggle notebooks

---

## Tips pre efektívnu prácu

### Ukladanie
- **Ctrl+S** = uložiť
- Colab ukladá automaticky, ale radšej ukladaj manuálne

### Rate limits
- Gemini Flash: 1,500 req/deň (používaj tento!)
- Gemini Pro: 50 req/deň

### GPU
- Free GPU: ~4 hodiny/deň
- Používaj len keď potrebuješ
- Pre väčšinu labov stačí CPU

### Export
- File → Download → Download .ipynb
- Môžeš aj priamo do GitHub

---

## Užitočné linky

| Čo | URL |
|----|-----|
| Google AI Studio | https://aistudio.google.com |
| Google Colab | https://colab.research.google.com |
| HuggingFace | https://huggingface.co |
| smolagents Docs | https://huggingface.co/docs/smolagents |
| Gemini API Docs | https://ai.google.dev/docs |

---

## Kontakt

- 💬 Teams: `#ai-academy-help`
- 📧 Email: ai-academy@kyndryl.com

---

*Kyndryl AI Academy 2026*
