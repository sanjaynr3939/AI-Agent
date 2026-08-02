from google import genai
from dotenv import load_dotenv
import os

load_dotenv("aiagent.env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Calling Gemini...")

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Say hello"
)

print("Gemini returned!")
print(response.text)