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
import argparse
import os
import sys

import const

# -------------------------------------------------------------------------------- 
# Public interface
# -------------------------------------------------------------------------------- 
def addProjectArgs(parser: argparse.ArgumentParser) -> None:
    """
    Register the --project argument.
    """
    parser.add_argument("--project",
        action="store",
        help="The name of the project to target")

def addDeploymentEnvironmentArgs(parser: argparse.ArgumentParser) -> None:
    """
    Register the --denv  argument.
    """
    parser.add_argument("--deploy-env",
        action="store",
        metavar="DEPLOYMENT_ENVIRONMENT",
        required=True,
        choices=const.DEPLOYMENT_ENVIRONMENTS,
        help="The deployment environment to target")

def addMockArgs(parser: argparse.ArgumentParser) -> None:
    """
    Register the --mock argument.
    """
    parser.add_argument("--mock",
        action="store_true",
        help="Run the script in MOCK mode, making no changes, just show what it would do")

# -------------------------------------------------------------------------------- 
# Private interface
# -------------------------------------------------------------------------------- 


# -------------------------------------------------------------------------------- 
# Module test
# -------------------------------------------------------------------------------- 
if __name__ == "__main__":
    module_path = os.path.abspath(__file__)
    print(f"\nTesting {module_path}...")

    parser = argparse.ArgumentParser(description=f"Testing")
    addProjectArgs(parser)
    addDeploymentEnvironmentArgs(parser)
    addMockArgs(parser)
    parsed_args = parser.parse_args()
