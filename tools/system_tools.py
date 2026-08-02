import platform
import os

def system_info():
    """Return information about the current system."""
    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Current Folder": os.getcwd()
    }