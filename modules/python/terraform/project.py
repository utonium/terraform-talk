#!/usr/bin/python3
# -------------------------------------------------------------------------------- 
# project.py
#
# Create Terraform projects.
#
# Kevin Cureton 2023 covered by the gpl-3.0
# -------------------------------------------------------------------------------- 

# -------------------------------------------------------------------------------- 
# Imports
# -------------------------------------------------------------------------------- 
import jinja2
import os
import sys

import log
import terraform.common

# -------------------------------------------------------------------------------- 
# Public interface
# -------------------------------------------------------------------------------- 
def getProjectPath(project_name: str) -> str:
    """
    Get the path to the project.
    """
    the_path = os.path.abspath(os.path.join(__file__, "../../../../projects", project_name))
    return the_path

def getProjectDeploymentEnvironmentPath(project_name: str, deployment_env: str) -> str:
    """
    Get the path to the project's deployment environment.
    """
    project_path = getProjectPath(project_name)
    the_path = os.path.abspath(os.path.join(project_path, deployment_env))
    return the_path

def createAWSProject(project_name: str, deployment_env: str, deployment_region: str) -> str:
    """
    Create an AWS project directory.
    """
    project_deployment_env_path = getProjectDeploymentEnvironmentPath(project_name, deployment_env)

    if not os.path.exists(project_deployment_env_path):
        os.makedirs(project_deployment_env_path)

    template_file = "aws-provider.tf.tmpl"
    template_options = {
        "project_name": project_name,
        "deployment_region": deployment_region
    }
    output_path = os.path.join(project_deployment_env_path, template_file.replace(".tmpl", ""))
    terraform.common.renderTemplate(output_path, template_file, template_options)

    return project_deployment_env_path


# -------------------------------------------------------------------------------- 
# Private interface
# -------------------------------------------------------------------------------- 



# -------------------------------------------------------------------------------- 
# Module test
# -------------------------------------------------------------------------------- 
if __name__ == "__main__":
    module_path = os.path.abspath(__file__)
    print(f"\nTesting {module_path}...")
