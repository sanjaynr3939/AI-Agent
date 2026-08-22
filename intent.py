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
    words = set(re.findall(r"\b\w+\b", text))
    print(words)

    # Department queries
    if (
        ("employee" in words or
        "employees" in words or
        "staff" in words or
        "department" in words)
        and
        words & DEPARTMENTS
    ):
        return "CSV"
    # Salary filter queries
    if (
        (
            "employee" in words
            or "employees" in words
            or "staff" in words
        )
        and
        (
            "salary" in words
            or "earn" in words
            or "earns" in words
            or "earning" in words
            or "pay" in words
            or "paid" in words
            or "income" in words
        )
    ):
        return "CSV"
    # Web queries first
    if words & INTENTS["WEB"]:
        return "WEB"

    # Time / Date / Day
    if words & INTENTS["TIME"]:
        return "TIME"

    if words & INTENTS["DATE"]:
        return "DATE"

    if words & INTENTS["DAY"]:
        return "DAY"

    # Remaining intents
    for intent in ["GREETING", "MATH", "MEMORY", "CSV"]:
        if words & INTENTS[intent]:
            return intent

    return "GEMINI"