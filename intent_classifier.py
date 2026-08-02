from config import client

MODEL = "gemini-flash-lite-latest"


def classify_intent(user_message):

    prompt = f"""
You are an intent classifier.

Classify the user's question into exactly ONE category.

Return ONLY ONE WORD.

CSV
WEB
GEMINI

CSV:
- Employee data
- Salary
- Department
- Age
- CSV file
- Data analysis

WEB:
- Latest news
- Current events
- Today
- Weather
- Sports
- Internet search

GEMINI:
- General knowledge
- Programming
- Explanations
- Conversations
- Anything else

Question:
{user_message}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip().upper()