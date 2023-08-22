#!/usr/bin/python3
# -------------------------------------------------------------------------------- 
# const.py
#
# Create a new project and bootstrap the Terraform setup.
#
# Kevin Cureton 2023 covered by the gpl-3.0
# -------------------------------------------------------------------------------- 

# -------------------------------------------------------------------------------- 
# Imports
# -------------------------------------------------------------------------------- 

# -----------------------------------------------
# Exit codes
#
# These values reflect what the script returns
# to the invoking shell.
# -----------------------------------------------
EXIT_CODE_SUCCESS = 0
EXIT_CODE_FAILURE = 1

# -----------------------------------------------
# Deployment environments
#
# Environments where infrastructure can be
# deployed.
# -----------------------------------------------
DEPLOYMENT_ENVIRONMENT_DEV = "dev"
DEPLOYMENT_ENVIRONMENT_STAGE = "stage"
DEPLOYMENT_ENVIRONMENT_PROD = "prod"

DEPLOYMENT_ENVIRONMENTS = [
    DEPLOYMENT_ENVIRONMENT_DEV,
    DEPLOYMENT_ENVIRONMENT_STAGE,
    DEPLOYMENT_ENVIRONMENT_PROD,
]

# -----------------------------------------------
# Terminal colors
# -----------------------------------------------

COLOR_BLUE = "\033[0;34m"
COLOR_CYAN = "\033[0;36m"
COLOR_GREEN = "\033[0;32m"
COLOR_PURPLE = "\033[0;35m"
COLOR_RED = "\033[0;31m"
COLOR_YELLOW = "\033[0;33m"

COLOR_OFF = "\033[0;0m"
