from query_parser.parser import parse_query

question = input("Question: ")

print(parse_query(question))