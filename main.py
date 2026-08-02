# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load API key
# load_dotenv("aiagent.env")

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Print available models
# for model in genai.list_models():
#     if "generateContent" in model.supported_generation_methods:
#         print(model.name)

# from google import genai
# from dotenv import load_dotenv
# import os

# # Load API key
# load_dotenv("aiagent.env")

# # Create Gemini client
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# print("🤖 AI Agent Started")
# print("Type 'exit' to quit.\n")

# while True:
#     user = input("You: ")

#     if user.lower() == "exit":
#         print("Goodbye!")
#         break

#     response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=user
# )

#     print("\nAgent:", response.text)
#     print("-" * 50)

# from google import genai
# from dotenv import load_dotenv
# import os

# # Load API key
# load_dotenv("aiagent.env")

# # Create Gemini client
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# # Create chat session
# chat = client.chats.create(
#    model="gemini-flash-lite-latest"
# )

# print("🤖 AI Agent Started")
# print("Type 'exit' to quit.\n")

# while True:
#     user = input("You: ")

#     if user.lower() == "exit":
#         print("Goodbye!")
#         break

#     response = chat.send_message(user)

#     print("\n🤖 Agent:", response.text)
#     print("-" * 60)



# /////////////////New///////////////
from chat import start_chat

if __name__ == "__main__":
    start_chat()


