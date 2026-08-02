import sys
import os

# Add the Project folder to Python's import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from prompt_loader import load_system_prompt

print(load_system_prompt())