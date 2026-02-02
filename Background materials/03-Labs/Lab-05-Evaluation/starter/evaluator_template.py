"""
AI Academy Lab 05 - Evaluation Framework
Starter template
"""

import json
from typing import Callable
from difflib import SequenceMatcher
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# ============================================
# Basic Evaluators
# ============================================

def exact_match(expected: str, actual: str) -> float:
    """Exact string match (normalized)."""
    # TODO: Implement
    pass


def fuzzy_match(expected: str, actual: str) -> float:
    """Fuzzy string similarity."""
    # TODO: Implement using SequenceMatcher
    pass


def contains_keywords(expected: str, actual: str) -> float:
    """Check if key terms from expected are in actual."""
    # TODO: Implement
    pass


# ============================================
# LLM-as-Judge Evaluator
# ============================================

def llm_judge(question: str, expected: str, actual: str, metric: str) -> dict:
    """Use LLM to evaluate response quality."""
    # TODO: Implement LLM-based evaluation
    # Return: {"score": 1-5, "reasoning": "..."}
    pass


# ============================================
# Evaluation Pipeline
# ============================================

def load_test_dataset(filepath: str) -> list:
    """Load test cases from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def evaluate_system(test_dataset: list, system_fn: Callable) -> list:
    """Run evaluation on all test cases."""
    results = []
    
    for test_case in test_dataset:
        # TODO: Get system response
        # TODO: Calculate all metrics
        # TODO: Store results
        pass
    
    return results


def calculate_summary(results: list) -> dict:
    """Calculate aggregate statistics."""
    # TODO: Compute averages, per-category breakdown, etc.
    pass


def generate_report(results: list, summary: dict, output_path: str):
    """Generate markdown quality report."""
    # TODO: Create readable report
    pass


# ============================================
# Main
# ============================================

def main():
    # 1. Load test dataset
    # dataset = load_test_dataset("../data/test_dataset.json")
    
    # 2. Define system under test
    # def my_system(question: str) -> str:
    #     # Your RAG system here
    #     pass
    
    # 3. Run evaluation
    # results = evaluate_system(dataset, my_system)
    
    # 4. Generate report
    # summary = calculate_summary(results)
    # generate_report(results, summary, "quality_report.md")
    
    print("Evaluation complete!")


if __name__ == "__main__":
    main()
