from tools.csv_tools import analyze_csv

questions = [
    "Who has the highest salary?",
    "Who has the lowest salary?",
    "What is the average salary?",
    "What is the total salary?"
]

for question in questions:
    print(analyze_csv("employees.csv", question))