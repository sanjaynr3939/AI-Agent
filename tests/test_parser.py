import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from query_parser.parser import parse_query

question = input("Question: ")

result = parse_query(question)

print(result)