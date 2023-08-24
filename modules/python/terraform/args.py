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

# -------------------------------------------------------------------------------- 
# Public interface
# -------------------------------------------------------------------------------- 
def addTerraformArgs(parser: argparse.ArgumentParser) -> None:
    """
    Register arguments used for Terraform setups.
    """
    parser.add_argument("--add-postgres-db",
        action="store_true",
        dest="add_postgresql_db",
        help="Add a Postgres DB setup to a project")

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
    addTerraformArgs(parser)
    parsed_args = parser.parse_args()
