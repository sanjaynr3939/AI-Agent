import pandas as pd
from query_parser.parser import parse_query







# -----------------------------
# CSV Analysis
# -----------------------------

def analyze_csv(file_path, question):

    df = pd.read_csv(file_path)

    question = question.lower()
    parsed = parse_query(question)
    # print(parsed)
    # print("Reached CSV Tool")
    # print("Name =", parsed["name"])
    


    # -------------------------
    # Highest Salary
    # -------------------------

    if (
        parsed["action"] == "highest"
        and parsed["column"] == "salary"
    ):

        data = df

        if parsed["department"] is not None:

            data = df[
                df["Department"].str.upper() == parsed["department"]
            ]

            if data.empty:
                return "No employees found."

            employee = data.loc[data["Salary"].idxmax()]

            return (
                f'{employee["Name"]} is the highest paid employee '
                f'in {parsed["department"]} with a salary of '
                f'₹{employee["Salary"]}.'
            )

        employee = data.loc[data["Salary"].idxmax()]

        return (
            f'{employee["Name"]} is the highest paid employee '
            f'with a salary of ₹{employee["Salary"]}.'
        )
        # -------------------------
    # Highest Age
    # -------------------------
    # -------------------------
    # Highest Age
    # -------------------------

    if (
        parsed["action"] == "highest"
        and parsed["column"] == "age"
        and parsed["department"] is None
    ):

        employee = df.loc[df["Age"].idxmax()]

        return (
            f'{employee["Name"]} is the oldest employee '
            f'with age {employee["Age"]}.'
        )
    


    # -------------------------
    # Lowest Age
    # -------------------------

    if (
        parsed["action"] == "lowest"
        and parsed["column"] == "age"
        and parsed["department"] is None
    ):

        employee = df.loc[df["Age"].idxmin()]

        return (
            f'{employee["Name"]} is the youngest employee '
            f'with age {employee["Age"]}.'
        )
    # -------------------------
    # Lowest Salary
    # -------------------------

    if (
        parsed["action"] == "lowest"
        and
        parsed["column"] == "salary"
    ):

        data = df

        if parsed["department"] is not None:

            data = df[
                df["Department"].str.upper() == parsed["department"]
            ]

            if data.empty:
                return "No employees found."

            employee = data.loc[data["Salary"].idxmin()]

            return (
                f'{employee["Name"]} is the lowest paid employee '
                f'in {parsed["department"]} with a salary of '
                f'₹{employee["Salary"]}.'
            )

        employee = data.loc[data["Salary"].idxmin()]

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

        data = df

        if parsed["department"] is not None:
            data = df[
                df["Department"].str.upper() == parsed["department"]
            ]

            if data.empty:
                return "No employees found."

            average = data["Salary"].mean()

            return f"Average salary in {parsed['department']} is ₹{average:.2f}."

        average = data["Salary"].mean()

        return f"The average salary is ₹{average:.2f}."
    # -------------------------
    # Total Salary
    # -------------------------

    if (
        parsed["action"] == "total"
        and
        parsed["column"] == "salary"
    ):

        data = df

        if parsed["department"] is not None:

            data = df[
                df["Department"].str.upper() == parsed["department"]
            ]

            if data.empty:
                return "No employees found."

            total = data["Salary"].sum()

            return f"Total salary in {parsed['department']} is ₹{total}."

        total = data["Salary"].sum()

        return f"The total salary is ₹{total}."
        # -------------------------
    # Employee Name Search
    # -------------------------
    # print("Checking Name Search")
    if parsed["name"] is not None:

        filtered = df[
            df["Name"].str.lower() == parsed["name"].lower()
        ]

        if filtered.empty:
            return "Employee not found."

        return filtered.to_string(index=False)

    # -------------------------
    # Combined Department + Comparison Filter
    # -------------------------

    if (
        parsed["department"] is not None
        and parsed["comparison"] is not None
        and parsed["column"] in ["salary", "age"]
    ):

        filtered = df[
            df["Department"].str.upper() == parsed["department"]
        ]

        if parsed["column"] == "salary":

            if parsed["comparison"] == "greater_than":
                filtered = filtered[
                    filtered["Salary"] > parsed["value"]
                ]

            elif parsed["comparison"] == "less_than":
                filtered = filtered[
                    filtered["Salary"] < parsed["value"]
                ]

        elif parsed["column"] == "age":

            if parsed["comparison"] == "greater_than":
                filtered = filtered[
                    filtered["Age"] > parsed["value"]
                ]

            elif parsed["comparison"] == "less_than":
                filtered = filtered[
                    filtered["Age"] < parsed["value"]
                ]

        if filtered.empty:
            return "No employees found."

        return filtered.to_string(index=False)


        # -------------------------
    # Department Filter
    # -------------------------

    if parsed["department"] is not None:

        filtered = df[
            df["Department"].str.upper() == parsed["department"]
        ]

        if filtered.empty:
            return "No employees found."

        # Employee Count
        if parsed["action"] == "count":

            count = len(filtered)

            if count == 1:
                return f"There is {count} employee in {parsed['department']}."

            return f"There are {count} employees in {parsed['department']}."

        # Oldest Employee
        if (
            parsed["action"] == "highest"
            and parsed["column"] == "age"
        ):

            emp = filtered.loc[
                filtered["Age"].idxmax()
            ]

            return (
                f'{emp["Name"]} is the oldest employee '
                f'in {parsed["department"]} '
                f'with age {emp["Age"]}.'
            )

        # Youngest Employee
        if (
            parsed["action"] == "lowest"
            and parsed["column"] == "age"
        ):

            emp = filtered.loc[
                filtered["Age"].idxmin()
            ]

            return (
                f'{emp["Name"]} is the youngest employee '
                f'in {parsed["department"]} '
                f'with age {emp["Age"]}.'
            )

        return filtered.to_string(index=False)
   

        # -------------------------
    # Department Salary Analytics
    # -------------------------

    if parsed["department"] is not None:

        dept_df = df[
            df["Department"].str.upper() == parsed["department"]
        ]

        if dept_df.empty:
            return "No employees found."

        # Average Salary
        if (
            parsed["action"] == "average"
            and parsed["column"] == "salary"
        ):

            return (
                f'Average salary in {parsed["department"]} '
                f'is ₹{dept_df["Salary"].mean():.2f}.'
            )

        # Total Salary
        if (
            parsed["action"] == "total"
            and parsed["column"] == "salary"
        ):

            return (
                f'Total salary in {parsed["department"]} '
                f'is ₹{dept_df["Salary"].sum()}.'
            )

        # Highest Salary
        if (
            parsed["action"] == "highest"
            and parsed["column"] == "salary"
        ):

            emp = dept_df.loc[
                dept_df["Salary"].idxmax()
            ]

            return (
                f'{emp["Name"]} has the highest salary '
                f'in {parsed["department"]} '
                f'(₹{emp["Salary"]}).'
            )

        # Lowest Salary
        if (
            parsed["action"] == "lowest"
            and parsed["column"] == "salary"
        ):

            emp = dept_df.loc[
                dept_df["Salary"].idxmin()
            ]

            return (
                f'{emp["Name"]} has the lowest salary '
                f'in {parsed["department"]} '
                f'(₹{emp["Salary"]}).'
            )

                # -------------------------
        # Employee Count
        # -------------------------

        if parsed["action"] == "count":

            count = len(dept_df)

            if count == 1:
                return f"There is {count} employee in {parsed['department']}."

            return f"There are {count} employees in {parsed['department']}."
     # -------------------------
    # List Employee Names
    # -------------------------

    if (
        parsed["action"] == "show"
        and parsed["column"] == "employee"
    ):

        names = "\n".join(df["Name"])

        return f"Employees:\n{names}"
    


    
    # # -------------------------
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

    if (
        "summary" in question
        or "describe" in question
        or "statistics" in question
        or "dataset" in question
        or "info" in question
    ):
        return summary

    return "Sorry, I couldn't understand the query."