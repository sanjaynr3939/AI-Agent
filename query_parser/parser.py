import re

# -----------------------------
# Operation Keywords
# -----------------------------

OPERATIONS = {

    "ADD": [
        "sum",
        "add",
        "plus"
    ],

    "SUBTRACT": [
        "sub",
        "subtract",
        "minus"
    ],

    "MULTIPLY": [
        "multiply",
        "product",
        "times"
    ],

    "DIVIDE": [
        "divide"
    ],

    "MOD": [
        "mod",
        "remainder"
    ]

}


def parse_query(text):

    text = text.lower()

    result = {
        "numbers": [],
        "operators": [],
        "words": [],
        "operation": None
    }

    # Extract numbers
    result["numbers"] = re.findall(r"\d+", text)

    # Extract operator symbols
    result["operators"] = re.findall(r"[+\-*/%]", text)

    # Extract words
    result["words"] = re.findall(r"\b[a-z]+\b", text)

    # -----------------------------
    # Detect operator symbols
    # -----------------------------

    symbol_map = {

        "+": "ADD",
        "-": "SUBTRACT",
        "*": "MULTIPLY",
        "/": "DIVIDE",
        "%": "MOD"

    }

    if result["operators"]:

        result["operation"] = symbol_map[result["operators"][0]]

    else:

        # Detect operation from words

        for operation, keywords in OPERATIONS.items():

            for keyword in keywords:

                if keyword in result["words"]:

                    result["operation"] = operation

                    break

            if result["operation"]:

                break

    return result