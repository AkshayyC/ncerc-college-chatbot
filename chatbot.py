import re
from database import get_all_knowledge


def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s?]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_questions(message):
    """
    Splits a message into separate questions/topics.

    Examples:

    "Where is NCERC and what courses are offered?"

    becomes:

    ["where is ncerc", "what courses are offered"]
    """

    message = message.strip()

    if not message:
        return []

    parts = re.split(
        r"\?|"
        r"\band\b|"
        r"\balso\b|"
        r"\bplus\b",
        message,
        flags=re.IGNORECASE
    )

    questions = []

    for part in parts:
        part = part.strip(" ,.")

        if part:
            questions.append(part)

    return questions


def score_question(question, keywords):
    question = normalize(question)

    keyword_list = [
        normalize(keyword)
        for keyword in keywords.split(",")
    ]

    score = 0

    for keyword in keyword_list:

        if keyword and keyword in question:
            score += 1

            # Give longer/more specific phrases more importance
            if len(keyword.split()) > 1:
                score += 1

    return score


def find_best_answer(question, knowledge):

    best_row = None
    best_score = 0

    for row in knowledge:

        score = score_question(
            question,
            row["keywords"]
        )

        if score > best_score:
            best_score = score
            best_row = row

    if best_row and best_score > 0:
        return best_row["answer"]

    return None


def get_response(message):

    if not message or not message.strip():
        return "Please enter a question so I can help you."

    knowledge = get_all_knowledge()

    questions = split_questions(message)

    answers = []

    for question in questions:

        answer = find_best_answer(
            question,
            knowledge
        )

        if answer and answer not in answers:
            answers.append(answer)

    if not answers:

        return (
            "I'm sorry, I couldn't find that information "
            "in my NCERC knowledge base yet. "
            "Try asking about courses, admissions, "
            "library, placements, location or contact information."
        )

    if len(answers) == 1:
        return answers[0]

    return " ".join(answers)