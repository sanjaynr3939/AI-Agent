import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tool_registry import TOOLS

print("Available Tools:\n")

for name in TOOLS:
    print(name)