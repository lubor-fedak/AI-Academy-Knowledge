# Lab 01: Instructions

## Phase 1: Environment Setup (15 min)

### Step 1.1: Create Project Structure

```bash
mkdir my-chatbot
cd my-chatbot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 1.2: Install Dependencies

```bash
pip install google-generativeai python-dotenv
```

### Step 1.3: Configure API Key

Create a `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

**⚠️ NEVER commit `.env` to version control!**

### Step 1.4: Verify Setup

Create `test_setup.py`:
```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Say 'Hello, AI Academy!'")
print(response.text)
```

Run: `python test_setup.py`

If you see the greeting, you're ready!

---

## Phase 2: Core Implementation (45 min)

### Step 2.1: Basic Chat Loop

Your first task is to create a simple chat loop. The chatbot should:
- Accept user input
- Send it to Gemini
- Display the response
- Repeat until user types "quit"

**Hints:**
- Use `input()` for user input
- Use `model.generate_content()` for responses
- Wrap in a `while True` loop with break condition

### Step 2.2: Add Conversation History

LLMs are stateless - they don't remember previous messages. You need to:
- Store messages in a list
- Send the full history with each request
- Format as alternating user/assistant messages

**Think about:**
- What data structure will you use?
- How will you format messages for the API?
- What happens when history gets too long?

### Step 2.3: Implement System Prompt

The system prompt defines your chatbot's personality and behavior. Create a chatbot that:
- Has a specific persona (helpful assistant, technical expert, etc.)
- Follows specific rules (stay on topic, be concise, etc.)
- Has knowledge boundaries (what it should/shouldn't discuss)

**Your system prompt should include:**
- Identity: Who is this chatbot?
- Behavior: How should it respond?
- Constraints: What should it avoid?

### Step 2.4: Add Error Handling

Your chatbot needs to handle:
- API connection failures
- Rate limiting (429 errors)
- Invalid responses
- Empty user input

**Use try/except blocks** around API calls and provide helpful error messages to users.

### Step 2.5: Track Token Usage

For cost awareness, log token usage:
- Input tokens (your prompt)
- Output tokens (model response)
- Total tokens per conversation

**Check:** `response.usage_metadata` for token counts

---

## Phase 3: Testing & Polish (20 min)

### Step 3.1: Test Scenarios

Test your chatbot with these scenarios:

1. **Basic Q&A:** Ask simple questions
2. **Multi-turn:** Have a 5+ message conversation
3. **Context retention:** Reference earlier messages
4. **Edge cases:** Empty input, very long input, special characters
5. **Error recovery:** Disconnect internet briefly, then reconnect

### Step 3.2: Code Quality

Review your code for:
- [ ] Clear variable names
- [ ] Comments explaining non-obvious logic
- [ ] Functions for reusable code
- [ ] No hardcoded values (use config)
- [ ] No exposed secrets

### Step 3.3: Documentation

Add a brief README to your project explaining:
- What the chatbot does
- How to run it
- Configuration options

---

## Phase 4: Reflection (10 min)

Answer these questions in a file called `REFLECTION.md`:

1. What surprised you about working with LLMs?
2. What was the hardest part of this lab?
3. How would you improve your chatbot with more time?
4. What questions do you have for your AI Tutor?

---

## Extension Challenges (Optional)

If you finish early, try:

1. **Streaming responses:** Display text as it's generated
2. **Conversation export:** Save chat history to file
3. **Multiple personas:** Let user choose chatbot personality
4. **Input validation:** Detect and handle toxic/inappropriate input
5. **Cost calculator:** Show estimated cost per conversation

---

## Submission

Upload to SharePoint `/07-Submissions/Labs/Lab-01/`:
- `chatbot.py` (main code)
- `config.py` (configuration)
- `REFLECTION.md` (your reflections)
- `conversation.log` or screenshot (sample conversation)

## Need Help?

1. **First:** Ask your AI Tutor in ChatGPT Enterprise
2. **Then:** Check the troubleshooting guide
3. **Finally:** Ask in Teams #ai-academy-help
