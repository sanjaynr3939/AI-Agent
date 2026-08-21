import pandas as pd
from query_parser.parser import parse_query







# -----------------------------
# CSV Analysis
# -----------------------------

def analyze_csv(file_path, question):

    df = pd.read_csv(file_path)

    question = question.lower()
    parsed = parse_query(question)
    

    # -------------------------
    # Highest Salary
    # -------------------------

    if (
        parsed["action"] == "highest"
        and
        parsed["column"] == "salary"
    ):

        employee = df.loc[df["Salary"].idxmax()]

        return (
            f'{employee["Name"]} is the highest paid employee '
            f'with a salary of ₹{employee["Salary"]}.'
        )

        # -------------------------
        # Lowest Salary
        # -------------------------

    if (
        parsed["action"] == "lowest"
        and
        parsed["column"] == "salary"
    ):

        employee = df.loc[df["Salary"].idxmin()]

        return (
            f'{employee["Name"]} is the lowest paid employee '
            f'with a salary of ₹{employee["Salary"]}.'
        )

    # -------------------------
    # Average Salary
    # -------------------------

    if (
        parsed["action"] == "average"
        and
        parsed["column"] == "salary"
    ):

        average = df["Salary"].mean()

        return f"The average salary is ₹{average:.2f}."
    # -------------------------
    # Total Salary
    # -------------------------

    if (
        parsed["action"] == "total"
        and
        parsed["column"] == "salary"
    ):

        total = df["Salary"].sum()

        return f"The total salary is ₹{total}."
    

    # -------------------------
    # Department Filter
    # -------------------------

    if (
        parsed["action"] == "filter"
        and
        parsed["column"] == "department"
    ):

        filtered = df[
            df["Department"].str.upper() == parsed["value"]
        ]

        if filtered.empty:
            return "No employees found."

        return filtered.to_string(index=False)

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