from query_parser.parser import parse_query


def calculate(user):

    parsed = parse_query(user)

    numbers = parsed["numbers"]
    operation = parsed["operation"]
    words = parsed["words"]

    if len(numbers) < 2:
        return None

    a = int(numbers[0])
    b = int(numbers[1])

    if operation == "ADD":
        return f"The answer is {a + b}"

    elif operation == "SUBTRACT":

        # Handle: subtract 3 from 9
        if "from" in words:
            return f"The answer is {b - a}"

        return f"The answer is {a - b}"

    elif operation == "MULTIPLY":
        return f"The answer is {a * b}"

    elif operation == "DIVIDE":

        if b == 0:
            return "Cannot divide by zero."

        return f"The answer is {a / b}"

    elif operation == "MOD":

        if b == 0:
            return "Cannot divide by zero."

        return f"The answer is {a % b}"

    return None