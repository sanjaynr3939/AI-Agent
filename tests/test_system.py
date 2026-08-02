import sys
import os

# Add the project folder to Python's search path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from system_tools import system_info
from tools.system_tools import system_info

print(system_info())