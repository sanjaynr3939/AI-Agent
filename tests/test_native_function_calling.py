import sys
import os

# Add the project folder to Python's path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from google.genai import types
from config import client
from tools.calculator import calculate

MODEL = "gemini-3.5-flash"

response = client.models.generate_content(
    model=MODEL,
    contents="Calculate ((12345*6789)-98765)/23 using the calculator tool.",
    config=types.GenerateContentConfig(
        tools=[calculate]
    )
)

print(response.text)