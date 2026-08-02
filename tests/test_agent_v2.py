import sys
import os

# Add the project folder to Python's path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from agent import execute_tool

print(execute_tool("calculator", "10+20"))
print(execute_tool("time"))
print(execute_tool("date"))
print(execute_tool("system"))