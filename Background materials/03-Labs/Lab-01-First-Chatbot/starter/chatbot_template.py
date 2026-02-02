"""
AI Academy - Lab 01: First Chatbot
Starter template - fill in the TODOs
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# TODO: Configure Gemini with your API key
# genai.configure(api_key=...)

# TODO: Define your system prompt
SYSTEM_PROMPT = """
You are a helpful assistant for AI Academy.
[Add more instructions here]
"""

# TODO: Initialize the model
# model = genai.GenerativeModel(...)

def create_chat():
    """Initialize a new chat session."""
    # TODO: Create and return a chat session
    pass

def send_message(chat, user_message):
    """Send a message and get response."""
    # TODO: Implement message sending
    # TODO: Add error handling
    # TODO: Track token usage
    pass

def main():
    """Main chat loop."""
    print("Welcome to AI Academy Chatbot!")
    print("Type 'quit' to exit.\n")
    
    # TODO: Initialize chat
    chat = create_chat()
    
    while True:
        # TODO: Get user input
        user_input = input("You: ")
        
        # TODO: Check for quit command
        
        # TODO: Send message and display response
        
        # TODO: Display token usage

if __name__ == "__main__":
    main()
