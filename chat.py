from database import save_message, save_memory
from tools.datetime_tools import get_current_time, get_current_date
from router import route_query


def start_chat():
    print("🤖 AI Agent Started")
    print("Type 'exit' to quit.\n")

    while True:

        # User input
        user = input("You: ")

        # Exit
        if user.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        # # Time Tool
        # if "time" in user.lower():
        #     print("\n🤖 Agent:", get_current_time())
        #     print("-" * 60)
        #     continue

        # # Date Tool
        # if "date" in user.lower():
        #     print("\n🤖 Agent:", get_current_date())
        #     print("-" * 60)
        #     continue

        # Save user message
        save_message("User", user)
        

        # Save important memories
        text = user.lower()

        if (
            text.startswith("my name is")
            or text.startswith("i live in")
            or text.startswith("my favorite")
            or text.startswith("i am")
        ):
           save_memory(user)
 
        

        # Generate AI response
        

        answer = route_query(user)

       

        print("\n🤖 Agent:", answer)
        print("-" * 60)

        # Save AI response
        save_message("Assistant", answer)