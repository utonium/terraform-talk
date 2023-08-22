
#!/usr/bin/python3
# -------------------------------------------------------------------------------- 
# args.py
#
# Function for commonly used command line arguments.
#
# Kevin Cureton 2023 covered by the gpl-3.0
# -------------------------------------------------------------------------------- 

# -------------------------------------------------------------------------------- 
# Imports
# -------------------------------------------------------------------------------- 
import os
import sys

import const

# -------------------------------------------------------------------------------- 
# Public interface
# -------------------------------------------------------------------------------- 
def debug(message: str) -> None:
    """
    Log a debug message.
    """
    print(f"{const.COLOR_CYAN}{message}{const.COLOR_OFF}")

def info(message: str) -> None:
    """
    Log an info message.
    """
    print(f"{const.COLOR_GREEN}{message}{const.COLOR_OFF}")

def warn(message: str) -> None:
    """
    Log a warn message.
    """
    print(f"{const.COLOR_YELLOW}{message}{const.COLOR_OFF}")

def error(message: str) -> None:
    """
    Log an error message.
    """
    print(f"{const.COLOR_RED}{message}{const.COLOR_OFF}")

def mock(message: str) -> None:
    """
    Log a mock  message.
    """
    print(f"{const.COLOR_PURPLE}{message}{const.COLOR_OFF}")


# -------------------------------------------------------------------------------- 
# Module test
# -------------------------------------------------------------------------------- 
if __name__ == "__main__":
    module_path = os.path.abspath(__file__)
    print(f"\nTesting {module_path}...")

    debug("This is a debug message")
    info("This is an info message")
    warn("This is a warn message")
    error("This is an error message")
    mock("This is a mock message")
