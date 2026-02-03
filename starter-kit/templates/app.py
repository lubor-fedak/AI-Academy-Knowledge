"""
AI Academy - Agent Demo App
============================
Template for deployment to HuggingFace Spaces.

Usage:
1. Create a new Space at huggingface.co/spaces
2. Upload this file as app.py
3. Add requirements.txt
4. Set GOOGLE_API_KEY in Settings → Secrets
"""

import gradio as gr
import google.generativeai as genai
import os
from typing import List, Tuple

# ============================================
# CONFIGURATION
# ============================================

# API Key from environment variable (set in HF Secrets)
API_KEY = os.environ.get('GOOGLE_API_KEY')

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set! Add it in Settings → Secrets")

genai.configure(api_key=API_KEY)

# Model
MODEL_NAME = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_NAME)

# ============================================
# SYSTEM PROMPT
# ============================================

SYSTEM_PROMPT = """
You are a friendly AI assistant created in Kyndryl AI Academy.

Rules:
1. Answer briefly and clearly
2. If you don't know something, say so directly
3. Be helpful and professional
4. Use emoji for better readability
"""

# ============================================
# CHAT FUNCTIONS
# ============================================

def format_history(history: List[Tuple[str, str]]) -> str:
    """Formats conversation history for the model."""
    formatted = SYSTEM_PROMPT + "\n\n"
    for human, ai in history:
        formatted += f"User: {human}\n"
        formatted += f"Assistant: {ai}\n\n"
    return formatted

def chat(message: str, history: List[Tuple[str, str]]) -> str:
    """
    Processes a message and returns a response.
    
    Args:
        message: Current message from user
        history: Conversation history [(user, assistant), ...]
    
    Returns:
        Assistant's response
    """
    try:
        # Create context
        context = format_history(history)
        context += f"User: {message}\nAssistant:"
        
        # Call the model
        response = model.generate_content(context)
        
        return response.text
    
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nPlease try again or contact support."

# ============================================
# GRADIO INTERFACE
# ============================================

# Example questions
EXAMPLES = [
    "Hi! Who are you?",
    "Explain what an AI agent is in simple terms",
    "What is RAG and why is it important?",
    "Write a simple Python function to calculate factorial",
    "What are best practices for prompt engineering?",
]

# Create interface
demo = gr.ChatInterface(
    fn=chat,
    title="🤖 AI Academy Demo Agent",
    description="""
    **Simple AI assistant created in Kyndryl AI Academy**
    
    Powered by Gemini 2.0 Flash | [GitHub](https://github.com/lubor-fedak/AI-Academy-Knowledge)
    """,
    examples=EXAMPLES,
    theme="soft",
    retry_btn="🔄 Try again",
    undo_btn="↩️ Undo",
    clear_btn="🗑️ Clear",
)

# ============================================
# RUN
# ============================================

if __name__ == "__main__":
    demo.launch(
        share=False,  # True if you want a public link
        show_error=True,
    )
