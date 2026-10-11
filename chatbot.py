import os

import json

import re
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from database import get_all_knowledge


# Load the API key from the project's .env file
load_dotenv(Path(__file__).with_name(".env"))

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY) if API_KEY else None

MODEL = "gemini-3.5-flash-lite"


def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s?]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def score_question(question, keywords):
    question = normalize(question)

    keyword_list = [
        normalize(keyword)
        for keyword in keywords.split(",")
    ]

    score = 0

    for keyword in keyword_list:
        if not keyword:
            continue

        # Match complete phrases or words, not partial words
        pattern = r"(?<!\w)" + re.escape(keyword) + r"(?!\w)"

        if re.search(pattern, question):
            score += 1

            if len(keyword.split()) > 1:
                score += 1

    return score


def find_best_answer(question, knowledge):
    best_row = None
    best_score = 0

    for row in knowledge:
        score = score_question(question, row["keywords"])

        if score > best_score:
            best_score = score
            best_row = row

    if best_row and best_score > 0:
        return best_row["answer"]

    return None


def is_greeting(message):
    text = normalize(message)

    greetings = {
        "hi",
        "hello",
        "hey",
        "hii",
        "hiii",
        "good morning",
        "good afternoon",
        "good evening",
        "how are you",
        "who are you",
        "what is your name",
        "thanks",
        "thank you",
        "bye",
        "goodbye"
    }

    return text in greetings


def is_college_question(message):
    text = normalize(message)

    college_terms = [
        "ncerc",
        "nehru college",
        "admission",
        "admissions",
        "fee structure",
        "fees",
        "fee",
        "scholarship",
        "hostel",
        "faculty",
        "principal",
        "hod",
        "department",
        "departments",
        "placement",
        "placements",
        "library",
        "semester exam",
        "hall ticket",
        "ktu",
        "attendance",
        "student portal",
        "canteen",
        "college bus",
        "college timings",
        "college location",
        "college address",
        "college website",
        "anti ragging",
        "campus",
        "courses offered",
        "course offered",
        "college"
    ]

    return any(term in text for term in college_terms)


def ask_gemini(message):
    if client is None:
        return "Gemini is not configured. Please check your .env file."

    response = client.models.generate_content(
        model=MODEL,
        contents=message,
        config={
            "system_instruction": """
You are the NCERC College Assistant, embedded directly on the official NCERC college website.
Answer general questions about Python, AI, science, mathematics, and everyday topics.
For NCERC information, never invent official facts.
If college information is missing, say:
Sorry, I don't have that information in my current NCERC database yet. Please contact the relevant college department for confirmation.
Never tell users to visit the official NCERC website because they are already using it.
Keep answers friendly and concise.
"""
        }
    )

    if response.text:
        return response.text.strip()

    return "Sorry, I couldn't generate an answer. Please try again."

def generate_knowledge_draft(source_text):
    """
    Generate a proposed knowledge record using the
    existing Gemini client. Does not save to the database.
    """
    if client is None:
        raise RuntimeError(
            "Gemini is not configured. Check your .env file."
        )

    source_text = source_text.strip()

    if not source_text:
        raise ValueError("Please provide college information.")

    response = client.models.generate_content(
        model=MODEL,
        contents=(
            "Create a draft knowledge-base record for the "
            "NCERC College Assistant using only the information "
            "in the source text below.\n\n"
            "Return JSON with exactly these fields:\n"
            '- "category": a short topic category\n'
            '- "keywords": comma-separated search keywords\n'
            '- "answer": a clear answer for a student\n\n'
            "Do not invent facts or add information that the "
            "source does not support. If details are unclear, "
            "mention only what the source confirms.\n\n"
            "SOURCE TEXT:\n"
            f"{source_text}"
        ),
        config={
            "response_mime_type": "application/json"
        }
    )

    if not response.text:
        raise RuntimeError(
            "Gemini did not return a draft. Please try again."
        )

    draft = json.loads(response.text)

    required_fields = ["category", "keywords", "answer"]

    for field in required_fields:
        if not isinstance(draft.get(field), str):
            raise ValueError(
                f"Gemini returned an invalid {field} field."
            )

        draft[field] = draft[field].strip()

        if not draft[field]:
            raise ValueError(
                f"The generated {field} field is empty."
            )

    return draft



def get_response(message):
    if not message or not message.strip():
        return "Please enter a question so I can help you."

    message = message.strip()
    normalized_message = normalize(message)

    try:
        knowledge = get_all_knowledge()

        # Check saved knowledge for every message first
        answer = find_best_answer(message, knowledge)

        if answer:
            return answer

        # Handle greetings and simple social messages

        # Handle greetings and simple social messages
        if is_greeting(message):
            answer = find_best_answer(message, knowledge)

            if answer:
                return answer

            if normalized_message in {"hi", "hello", "hey", "hii", "hiii"}:
                return (
                    "Hello! 👋 I'm the NCERC College Assistant. "
                    "How can I help you today?"
                )

        # College questions must use the NCERC knowledge base
        if is_college_question(message):
            answer = find_best_answer(message, knowledge)

            if answer:
                return answer

            return (
                "I'm sorry, I couldn't find reliable information "
                "about that in my NCERC knowledge base yet. "
                "Please check the official NCERC website or "
                "contact the college office for confirmation."
            )

        # General questions are answered by Gemini
        return ask_gemini(message)

    except Exception as error:
        print("CHATBOT ERROR TYPE:", type(error).__name__)
        print("CHATBOT ERROR DETAILS:", error)

        error_text = str(error).lower()

        if "503" in error_text or "unavailable" in error_text:
            return (
                "Gemini is temporarily busy. Please try again "
                "in a few moments."
            )

        if "429" in error_text or "resource_exhausted" in error_text:
            return (
                "The AI service has reached its current usage "
                "limit. Please try again later."
            )

        return (
            "Sorry, I couldn't process your question right now. "
            "Please try again in a moment."
        )