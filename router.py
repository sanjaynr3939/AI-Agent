from tool_registry import TOOLS
from gemini_service import generate_response
from intent import detect_intent


def route_query(user):

    intent = detect_intent(user)

    print(f"Intent -> {intent}")

    if intent == "GREETING":
        return "Hello Sanjay! 👋"

    if intent in TOOLS:

        tool = TOOLS[intent]

    if intent == "CSV":
        return tool("employees.csv", user)

    elif intent in ["TIME", "DATE"]:
        return tool()

    else:
        return tool(user)