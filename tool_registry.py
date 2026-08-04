from tools.datetime_tools import (
    get_current_time,
    get_current_date,
    get_current_day
)

from tools.csv_tools import analyze_csv
from tools.web_search import search_web
from tools.memory_tool import search_memory
from tools.calculator import calculate


TOOLS = {

    "TIME": {
        "function": get_current_time,
        "args": 0
    },

    "DATE": {
        "function": get_current_date,
        "args": 0
    },

    "DAY": {
        "function": get_current_day,
        "args": 0
    },

    "MEMORY": {
        "function": search_memory,
        "args": 1
    },

    "MATH": {
        "function": calculate,
        "args": 1
    },

    "CSV": {
        "function": analyze_csv,
        "args": 2
    },

    "WEB": {
        "function": search_web,
        "args": 1
    }

}