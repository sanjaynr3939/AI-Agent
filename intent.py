import re

INTENTS = {
    "GREETING": {
        "hi", "hello", "hey",
        "good morning", "good evening",
        "bye", "thanks", "thank you"
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
        "employees", "department",
        "income", "pay", "staff",
        "paid", "age"
    },

    "WEB": {
        "news", "weather",
        "sports", "latest",
        "current"
    }
}

DEPARTMENTS = {
    "it",
    "hr",
    "sales",
    "finance"
}


def detect_intent(text):

    text = text.lower()

    # Detect mathematical operators
    if any(op in text for op in ["+", "-", "*", "/", "%"]):
        return "MATH"

    words = set(re.findall(r"\b\w+\b", text))

    # Detect department names
    if words & DEPARTMENTS:
        return "CSV"

    # Detect other intents
    for intent, keywords in INTENTS.items():
        if words & keywords:
            return intent

    return "GEMINI"