import re

# -----------------------------
# Math Operations
# -----------------------------

OPERATIONS = {
    "ADD": ["sum", "add", "plus"],
    "SUBTRACT": ["subtract", "minus", "sub"],
    "MULTIPLY": ["multiply", "times", "product"],
    "DIVIDE": ["divide"],
    "MOD": ["mod", "remainder"]
}

# -----------------------------
# CSV Actions
# -----------------------------

CSV_ACTIONS = {

    "highest": [...],

    "lowest": [...],

    "average": [...],

    "total": [...],

    "sort": [...],

    "count": [
        "count",
        "many",
        "number"
    ]
}

# -----------------------------
# CSV Columns
# -----------------------------

CSV_COLUMNS = {
    "salary": [
        "salary",
        "paid",
        "pay",
        "income",
        "earn",
        "earns",
        "earning"
    ],

    "age": [
        "age",
        "old",
        "older",
        "young",
        "younger"
    ],

    "department": [
        "department"
    ],

    "name": [
        "name"
    ],

    "employee": [
        "employee",
        "employees",
        "staff"
    ]
}

# -----------------------------
# Departments
# -----------------------------

DEPARTMENTS = [
    "it",
    "hr",
    "sales",
    "finance",
    "marketing"
]

# -----------------------------
# Employee Names
# -----------------------------

EMPLOYEE_NAMES = [
    "ram",
    "ravi",
    "amit",
    "priya",
    "sneha"
]

# -----------------------------
# Comparison
# -----------------------------

COMPARISON_WORDS = {

    "greater_than": [
        "greater",
        "more",
        "above",
        "over",
        "older"
    ],

    "less_than": [
        "less",
        "below",
        "under",
        "younger"
    ]
}


def parse_query(text):

    text = text.lower()

    result = {

        "numbers": [],
        "operators": [],
        "words": [],

        "operation": None,

        "action": None,
        "column": None,
        "comparison": None,

        "value": None,

        "department": None,
        "name": None

    }

    # -----------------------------
    # Extract Numbers
    # -----------------------------

    result["numbers"] = re.findall(r"\d+", text)

    # -----------------------------
    # Extract Operators
    # -----------------------------

    result["operators"] = re.findall(r"[+\-*/%]", text)

    # -----------------------------
    # Extract Words
    # -----------------------------

    result["words"] = re.findall(r"\b[a-z]+\b", text)

    # -----------------------------
    # Symbol Operations
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

    # -----------------------------
    # Word Operations
    # -----------------------------

    if result["operation"] is None:

        for op, keywords in OPERATIONS.items():

            if any(word in keywords for word in result["words"]):

                result["operation"] = op
                break

    # -----------------------------
    # CSV Action
    # -----------------------------

    for action, keywords in CSV_ACTIONS.items():

        if any(word in keywords for word in result["words"]):

            result["action"] = action
            break

    # -----------------------------
    # Detect Salary Keywords FIRST
    # -----------------------------

    salary_words = CSV_COLUMNS["salary"]

    if any(word in salary_words for word in result["words"]):
        result["column"] = "salary"

    # -----------------------------
    # Detect Age
    # -----------------------------

    elif any(word in CSV_COLUMNS["age"] for word in result["words"]):
        result["column"] = "age"

    # -----------------------------
    # Detect Name
    # -----------------------------

    elif "name" in result["words"]:
        result["column"] = "name"

    # -----------------------------
    # Detect Department
    # -----------------------------

    elif "department" in result["words"]:
        result["column"] = "department"

    # -----------------------------
    # Detect Employee
    # -----------------------------

    elif any(word in CSV_COLUMNS["employee"] for word in result["words"]):
        result["column"] = "employee"

    # -----------------------------
    # Department Value
    # -----------------------------

    for dept in DEPARTMENTS:

        if dept in result["words"]:

            result["department"] = dept.upper()
            break

    # -----------------------------
    # Comparison
    # -----------------------------

    for comp, keywords in COMPARISON_WORDS.items():

        if any(word in keywords for word in result["words"]):

            result["comparison"] = comp
            break

    # -----------------------------
    # Numeric Value
    # -----------------------------

    if result["numbers"]:

        result["value"] = int(result["numbers"][0])

    # -----------------------------
    # Employee Name
    # -----------------------------

    for word in result["words"]:

        if word in EMPLOYEE_NAMES:

            result["name"] = word.capitalize()
            break

    return result