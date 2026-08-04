import re

INTENTS = {
    "GREETING": {
        "hi", "hello", "hey",
        "good morning", "good evening",
        "bye", "thanks","Thanks","Thank you", "thank you"
    },

    "TIME": {
        "time", "clock"
    },

    "DATE": {
        "date"
    },

    "DAY": {
        "day", "weekday", "today", "which day"
    },

    "MATH": {
        "sum", "add", "plus",
        "sub", "subtract", "minus",
        "multiply", "product",
        "divide", "mod"
    },

    "MEMORY": {
        "favorite", "favourite",
        "remember", "memory",
        "name", "live"
    },

    "CSV": {
        "salary", "employee",
        "department", "income",
        "pay", "paid", "age"
    },

    "WEB": {
        "news", "weather",
        "sports", "latest",
        "current"
    }
}


def detect_intent(text):

    text = text.lower()

    # Detect mathematical operators
    if any(op in text for op in ["+", "-", "*", "/", "%"]):
        return "MATH"

    words = set(re.findall(r"\b\w+\b", text))

    for intent, keywords in INTENTS.items():
        if words & keywords:
            return intent

    return "GEMINI"