import re

def format_response(text):

    if not text:
        return "No response received."

    # Remove Markdown headings
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Remove bold
    text = text.replace("**", "")

    # Remove italics
    text = text.replace("*", "")

    # Remove code fences
    text = text.replace("```python", "")
    text = text.replace("```", "")

    return text.strip()