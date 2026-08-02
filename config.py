import os
from dotenv import load_dotenv
from google import genai

load_dotenv("aiagent.env")

print("Config loaded")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)