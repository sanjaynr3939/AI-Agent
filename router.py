from tool_registry import TOOLS
from gemini_service import generate_response
from intent import detect_intent


def route_query(user):

    intent = detect_intent(user)

    print(f"Intent -> {intent}")

    if intent == "GREETING":
        return "Hello Sanjay! 👋"

    tool_info = TOOLS.get(intent)

    if not tool_info:
        return generate_response(user)

    tool = tool_info["function"]
    args = tool_info["args"]

    if args == 0:
        return tool()

    elif args == 1:
        return tool(user)

    elif args == 2:
        return tool("employees.csv", user)

    return generate_response(user)