"""
AI Academy - Agent Demo App
============================
Template pre deployment na HuggingFace Spaces.

Použitie:
1. Vytvor nový Space na huggingface.co/spaces
2. Nahraj tento súbor ako app.py
3. Pridaj requirements.txt
4. Nastav GOOGLE_API_KEY v Settings → Secrets
"""

import gradio as gr
import google.generativeai as genai
import os
from typing import List, Tuple

# ============================================
# KONFIGURÁCIA
# ============================================

# API Key z environment variable (nastav v HF Secrets)
API_KEY = os.environ.get('GOOGLE_API_KEY')

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY nie je nastavený! Pridaj ho do Settings → Secrets")

genai.configure(api_key=API_KEY)

# Model
MODEL_NAME = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_NAME)

# ============================================
# SYSTEM PROMPT
# ============================================

SYSTEM_PROMPT = """
Si priateľský AI asistent vytvorený v Kyndryl AI Academy.

Pravidlá:
1. Odpovedaj stručne a jasne
2. Ak niečo nevieš, povedz to priamo
3. Buď nápomocný a profesionálny
4. Používaj emoji pre lepšiu čitateľnosť
"""

# ============================================
# CHAT FUNKCIE
# ============================================

def format_history(history: List[Tuple[str, str]]) -> str:
    """Formátuje históriu konverzácie pre model."""
    formatted = SYSTEM_PROMPT + "\n\n"
    for human, ai in history:
        formatted += f"Používateľ: {human}\n"
        formatted += f"Asistent: {ai}\n\n"
    return formatted

def chat(message: str, history: List[Tuple[str, str]]) -> str:
    """
    Spracuje správu a vráti odpoveď.
    
    Args:
        message: Aktuálna správa od používateľa
        history: História konverzácie [(user, assistant), ...]
    
    Returns:
        Odpoveď asistenta
    """
    try:
        # Vytvor kontext
        context = format_history(history)
        context += f"Používateľ: {message}\nAsistent:"
        
        # Zavolaj model
        response = model.generate_content(context)
        
        return response.text
    
    except Exception as e:
        return f"❌ Chyba: {str(e)}\n\nSkús to znova alebo kontaktuj support."

# ============================================
# GRADIO INTERFACE
# ============================================

# Príklady otázok
EXAMPLES = [
    "Ahoj! Kto si?",
    "Vysvetli čo je AI agent v jednoduchých slovách",
    "Čo je RAG a prečo je dôležitý?",
    "Napíš jednoduchú Python funkciu na výpočet faktoriálu",
    "Aké sú best practices pre prompt engineering?",
]

# Vytvor interface
demo = gr.ChatInterface(
    fn=chat,
    title="🤖 AI Academy Demo Agent",
    description="""
    **Jednoduchý AI asistent vytvorený v Kyndryl AI Academy**
    
    Powered by Gemini 2.0 Flash | [GitHub](https://github.com/your-org/ai-academy-starter)
    """,
    examples=EXAMPLES,
    theme="soft",
    retry_btn="🔄 Skúsiť znova",
    undo_btn="↩️ Späť",
    clear_btn="🗑️ Vymazať",
)

# ============================================
# SPUSTENIE
# ============================================

if __name__ == "__main__":
    demo.launch(
        share=False,  # True ak chceš verejný link
        show_error=True,
    )
