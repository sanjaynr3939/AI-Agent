import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from agent import execute_tool

print(execute_tool("calculator", "25+75"))
print(execute_tool("time"))
print(execute_tool("date"))
print(execute_tool("system"))