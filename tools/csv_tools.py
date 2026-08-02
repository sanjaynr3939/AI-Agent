import pandas as pd

# -----------------------------
# Keyword Groups
# -----------------------------

SALARY_WORDS = [
    "salary",
    "pay",
    "paid",
    "earn",
    "earns",
    "earning"
]

EMPLOYEE_WORDS = [
    "employee",
    "employees",
    "person",
    "staff"
]

HIGH_WORDS = [
    "highest",
    "maximum",
    "most",
    "top",
    "best",
    "largest",
    "greatest",
    "max"
]

LOW_WORDS = [
    "lowest",
    "minimum",
    "least",
    "smallest",
    "min",
    "low"
]

AVERAGE_WORDS = [
    "average",
    "mean"
]

TOTAL_WORDS = [
    "total",
    "sum"
]


# -----------------------------
# Helper Function
# -----------------------------

def contains_any(question, words):
    return any(word in question for word in words)


# -----------------------------
# CSV Analysis
# -----------------------------

def analyze_csv(file_path, question):

    df = pd.read_csv(file_path)

    question = question.lower()

    has_salary = contains_any(question, SALARY_WORDS)
    has_employee = contains_any(question, EMPLOYEE_WORDS)
    has_high = contains_any(question, HIGH_WORDS)
    has_low = contains_any(question, LOW_WORDS)
    has_average = contains_any(question, AVERAGE_WORDS)
    has_total = contains_any(question, TOTAL_WORDS)

    # -------------------------
    # Highest Salary
    # -------------------------

    if has_high and (has_salary or has_employee):

        employee = df.loc[df["Salary"].idxmax()]

        return (
            f'{employee["Name"]} is the highest paid employee '
            f'with a salary of ₹{employee["Salary"]}.'
        )

    # -------------------------
    # Lowest Salary
    # -------------------------

    if has_low and (has_salary or has_employee):

        employee = df.loc[df["Salary"].idxmin()]

        return (
            f'{employee["Name"]} is the lowest paid employee '
            f'with a salary of ₹{employee["Salary"]}.'
        )

    # -------------------------
    # Average Salary
    # -------------------------

    if has_average and has_salary:

        average = df["Salary"].mean()

        return f"The average salary is ₹{average:.2f}."

    # -------------------------
    # Total Salary
    # -------------------------

    if has_total and has_salary:

        total = df["Salary"].sum()

        return f"The total salary is ₹{total}."

    # -------------------------
    # Summary
    # -------------------------

    summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Missing Values:
{df.isnull().sum().to_string()}

Data Types:
{df.dtypes.to_string()}
"""

    if "Salary" in df.columns:

        summary += f"""

Salary Statistics
-----------------
Average Salary : {df["Salary"].mean()}
Highest Salary : {df["Salary"].max()}
Lowest Salary  : {df["Salary"].min()}
Total Salary   : {df["Salary"].sum()}
"""

    return summary