import time
from config import client
from formatter import format_response

MODEL = "gemini-flash-lite-latest"


def generate_response(user_message):

    try:

        print("Before Gemini")

        start = time.time()

        response = client.models.generate_content(
            model=MODEL,
            contents=user_message
        )

        end = time.time()

        print(f"Gemini API: {end - start:.2f}s")

        return format_response(response.text)

    except Exception as e:

        print("Gemini Error:", e)

        return "Error"