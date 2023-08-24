#!/usr/bin/python3
# -------------------------------------------------------------------------------- 
# aws-vpc.py
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
import terraform.project

# -------------------------------------------------------------------------------- 
# Public interface
# -------------------------------------------------------------------------------- 

def addVPC(project_name: str, deployment_env: str, deployment_region: str) -> None:
    """
    Render the code for the AWS VPC module.
    """
    project_deployment_env_path = terraform.project.getProjectDeploymentEnvironmentPath(project_name, deployment_env)

    template_file = "aws-vpc.tf.tmpl"
    template_options = {
        "project_name": project_name,
        "deployment_env": deployment_env,
        "deployment_region": deployment_region,
    }
    output_path = os.path.join(project_deployment_env_path, template_file.replace(".tmpl", ""))
    terraform.common.renderTemplate(output_path, template_file, template_options)

    return


# -------------------------------------------------------------------------------- 
# Private interface
# -------------------------------------------------------------------------------- 



# -------------------------------------------------------------------------------- 
# Module test
# -------------------------------------------------------------------------------- 
if __name__ == "__main__":
    module_path = os.path.abspath(__file__)
    print(f"\nTesting {module_path}...")
