# 📖 Detailed Setup Guide

Complete guide for AI Academy participants.

---

## Prerequisites

- Internet connection
- Web browser (Chrome/Firefox/Edge)
- Basic Python knowledge (you don't need to be an expert)

---

## Step 1: Google Account (2 min)

If you already have Gmail, skip this step.

1. Go to https://accounts.google.com/signup
2. Fill in the details
3. Verify your phone number
4. Done ✅

---

## Step 2: Google AI Studio - API Key (5 min)

### 2.1 Access
1. Open https://aistudio.google.com
2. Click "Sign in with Google"
3. Use your Google account
4. Accept Terms of Service

### 2.2 Creating an API Key
1. In the left menu, click **"Get API key"**
2. Click **"Create API key"**
3. Select **"Create API key in new project"**
4. Wait a few seconds
5. **Copy the API key** (looks like `AIzaSy...`)

### 2.3 Store API Key Securely
- Save to password manager
- OR to a private document
- **NEVER** put in public code!

---

## Step 3: Google Colab (3 min)

### 3.1 Opening a Notebook

**Option A: Direct link**
- Click the "Open in Colab" badge in README

**Option B: Manual**
1. Go to https://colab.research.google.com
2. File → Open notebook
3. GitHub tab
4. Enter the repository URL
5. Select notebook

### 3.2 Setting up API Key in Colab

1. In the left panel, find the 🔑 icon (Secrets)
2. Click on it
3. Click **"Add new secret"**
4. Fill in:
   - **Name:** `GOOGLE_API_KEY`
   - **Value:** *paste your API key*
5. Click the **"Notebook access"** toggle → turn it on
6. Done ✅

### 3.3 Verification

Run this cell in the notebook:

```python
from google.colab import userdata
key = userdata.get('GOOGLE_API_KEY')
print(f"✅ API key loaded: {key[:10]}...")
```

If you see an error, check:
- Is the secret named exactly `GOOGLE_API_KEY`?
- Is the "Notebook access" toggle on?

---

## Step 4: HuggingFace Account (optional, 3 min)

For deploying agents.

### 4.1 Registration
1. Go to https://huggingface.co/join
2. Fill in: Username, Email, Password
3. Click "Sign Up"
4. Confirm email

### 4.2 Access Token
1. Click avatar → Settings
2. In left menu: Access Tokens
3. Click "Create new token"
4. Name: `ai-academy`
5. Role: `write`
6. Copy token

---

## Troubleshooting

### "API key not valid"

**Cause:** Incorrect or expired key

**Solution:**
1. Go to https://aistudio.google.com
2. Get API key → Create new key
3. Update in Colab Secrets

### "429 Too Many Requests"

**Cause:** Rate limit exceeded

**Solution:**
- Wait 60 seconds
- Use `gemini-2.0-flash` instead of `gemini-2.5-pro`

### "ModuleNotFoundError"

**Cause:** Library not installed

**Solution:**
```python
!pip install google-generativeai smolagents litellm
```

### Colab is stuck

**Solution:**
1. Runtime → Restart runtime
2. Run setup cell again
3. If that doesn't help: Runtime → Disconnect and delete runtime

### GPU not available

**Cause:** High demand, free tier exhausted

**Solution:**
- Try later
- Use CPU runtime (slower but works)
- Alternative: Kaggle notebooks

---

## Tips for Effective Work

### Saving
- **Ctrl+S** = save
- Colab saves automatically, but better to save manually

### Rate limits
- Gemini Flash: 1,500 req/day (use this!)
- Gemini Pro: 50 req/day

### GPU
- Free GPU: ~4 hours/day
- Use only when needed
- For most labs, CPU is sufficient

### Export
- File → Download → Download .ipynb
- You can also directly to GitHub

---

## Useful Links

| What | URL |
|------|-----|
| Google AI Studio | https://aistudio.google.com |
| Google Colab | https://colab.research.google.com |
| HuggingFace | https://huggingface.co |
| smolagents Docs | https://huggingface.co/docs/smolagents |
| Gemini API Docs | https://ai.google.dev/docs |

---

## Contact

- 💬 Teams: `#ai-academy-help`
- 📧 Email: ai-academy@kyndryl.com

---

*Kyndryl AI Academy 2026*
