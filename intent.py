import re

INTENTS = {
    "GREETING": {
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening",
        "bye",
        "thanks",
        "thank you"
    },

    "TIME": {
        "time",
        "clock"
    },

    "DATE": {
        "date"
    },

    "CSV": {
        "salary",
        "employee",
        "department",
        "income",
        "pay",
        "paid",
        "age"
    },

    "WEB": {
        "news",
        "weather",
        "sports",
        "latest",
        "current"
    }


}

# Separate variable
MATH_WORDS = {
        "sum",
        "add",
        "plus",
        "sub",
        "subtract",
        "minus",
        "multiply",
        "product",
        "divide",
        "mod"
}

MEMORY_WORDS = {
    "favorite",
    "favourite",
    "remember",
    "memory",
    "name",
    "live"
}


def detect_intent(text):

    text = text.lower()

    # Detect operators
    if any(op in text for op in ["+", "-", "*", "/", "%"]):
        return "MATH"

    # Detect math words
    for word in MATH_WORDS:
        if word in text:
            return "MATH"

    for word in MEMORY_WORDS:
        if word in text:
            return "MEMORY"

    words = set(re.findall(r"\b\w+\b", text))

    if words & INTENTS["GREETING"]:
        return "GREETING"

    for intent, keywords in INTENTS.items():

        if intent == "GREETING":
            continue

        if words & keywords:
            return intent

    return "GEMINI"