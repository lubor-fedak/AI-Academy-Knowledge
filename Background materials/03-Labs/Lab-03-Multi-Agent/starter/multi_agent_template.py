"""
AI Academy - Lab 03: Multi-Agent System
Starter template
"""

import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================
# Agent Base Class
# ============================================

class Agent:
    """Base class for all agents."""
    
    def __init__(self, name: str, system_prompt: str, tools: list = None):
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools or []
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def run(self, query: str, context: dict = None) -> dict:
        """Execute agent with query and return structured response."""
        logger.info(f"[{self.name}] Processing: {query[:50]}...")
        
        # TODO: Build prompt with system message and context
        # TODO: Call model
        # TODO: Parse and return response
        
        return {
            "agent": self.name,
            "query": query,
            "response": "TODO: Implement",
            "sources": []
        }


# ============================================
# Specialized Agents
# ============================================

# TODO: Create PolicyAgent with HR RAG

# TODO: Create TechnicalAgent with Tech RAG

# TODO: Create GeneralAgent (no RAG)


# ============================================
# Orchestrator
# ============================================

class Orchestrator:
    """Routes queries to appropriate agents."""
    
    def __init__(self):
        # TODO: Initialize agents
        self.agents = {}
        self.router_model = genai.GenerativeModel("gemini-1.5-flash")
    
    def route(self, query: str) -> str:
        """Classify query and return agent name."""
        routing_prompt = """
        Classify this query into one category: policy, technical, or general.
        
        Categories:
        - policy: HR, leave, vacation, expenses, benefits, salary, company rules
        - technical: code, deployment, APIs, errors, KAF, Azure, programming
        - general: greetings, chitchat, unclear questions, other
        
        Query: {query}
        
        Respond with ONLY the category name (policy, technical, or general).
        """.format(query=query)
        
        # TODO: Implement routing
        return "general"  # Default
    
    def run(self, query: str) -> dict:
        """Process query through appropriate agent."""
        # Step 1: Route
        agent_name = self.route(query)
        logger.info(f"Routed to: {agent_name}")
        
        # Step 2: Get agent
        # TODO: Get correct agent
        
        # Step 3: Execute
        # TODO: Run agent and return result
        
        return {"error": "Not implemented"}


# ============================================
# Main
# ============================================

def main():
    orchestrator = Orchestrator()
    
    print("Multi-Agent System Ready!")
    print("I can help with policy questions, technical questions, or general queries.")
    print("Type 'quit' to exit.\n")
    
    while True:
        query = input("You: ")
        if query.lower() == 'quit':
            break
        
        result = orchestrator.run(query)
        print(f"\n[{result.get('agent', 'Unknown')}]: {result.get('response', 'Error')}\n")


if __name__ == "__main__":
    main()
