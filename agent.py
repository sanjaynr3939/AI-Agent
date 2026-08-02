from tool_registry import TOOLS


def execute_tool(tool_name, *args):
    """
    Execute a registered tool.
    """

    tool = TOOLS.get(tool_name)

    if tool is None:
        return f"Tool '{tool_name}' not found."

    try:
        return tool["function"](*args)

    except Exception as e:
        return f"Error while executing '{tool_name}': {e}"