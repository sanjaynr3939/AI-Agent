from tools.calculator import calculate
from tools.datetime_tools import get_current_time, get_current_date
from tools.system_tools import system_info
from tools.csv_tools import analyze_csv

GEMINI_TOOLS = [
    calculate,
    get_current_time,
    get_current_date,
    system_info,
    analyze_csv
]