import re

def calculate(text):

    text = text.lower()

    try:

        # sum of 3 and 5
        m = re.search(r"sum of (\d+) and (\d+)", text)
        if m:
            return f"The answer is {int(m.group(1)) + int(m.group(2))}"

        # multiply 5 by 8
        m = re.search(r"multiply (\d+) by (\d+)", text)
        if m:
            return f"The answer is {int(m.group(1)) * int(m.group(2))}"

        # divide 20 by 4
        m = re.search(r"divide (\d+) by (\d+)", text)
        if m:
            return f"The answer is {int(m.group(1)) / int(m.group(2))}"

        # subtract 8 from 20
        m = re.search(r"sub(?:tract)? of (\d+) and (\d+)", text)
        if m:
            return f"The answer is {int(m.group(1)) - int(m.group(2))}"

        # Normal expression (4+7)
        m = re.search(r"\d+\s*[\+\-\*/%]\s*\d+", text)

        if m:
            expression = m.group()
            return f"The answer is {eval(expression)}"

        return None

    except Exception:
        return None