from tools.datetime_tools import (
    get_current_time,
    get_current_date
)

from tools.csv_tools import analyze_csv
from tools.web_search import search_web
from tools.memory_tool import search_memory
from tools.calculator import calculate

TOOLS = {

    "TIME": get_current_time,

    "DATE": get_current_date,

    "MEMORY": search_memory,

    "MATH": calculate,

    "CSV": analyze_csv,

    "WEB": search_web

}