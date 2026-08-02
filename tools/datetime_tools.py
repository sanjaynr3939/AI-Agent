from datetime import datetime


def get_current_time() -> str:
    """
    Get the current local system time.

    Use this function whenever the user asks for:
    - current time
    - what time it is
    - time now
    - whats the time now

    Do not estimate or guess the current time.
    Always call this function.
    """
    
    return datetime.now().strftime("%I:%M:%S %p")


def get_current_date() -> str:
    """
    Get today's local system date.

    Use this function whenever the user asks for:
    - today's date
    - current date
    - what day it is today

    Do not estimate or guess the date.
    Always call this function.
    """
    
    return datetime.now().strftime("%d-%m-%Y")