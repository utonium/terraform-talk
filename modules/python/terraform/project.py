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

def createProject(project_name: str, deployment_env: str) -> str:
    """
    Create a project directory.
    """
    project_deployment_env_path = getProjectDeploymentEnvironmentPath(project_name, deployment_env)

    if not os.path.exists(project_deployment_env_path):
        os.makedirs(project_deployment_env_path)

    return project_deployment_env_path

def renderTemplate(output_path: str, template_file: str, template_options: dict = {}) -> str:
    """
    Render out Terraform code using a templatepath and template options.
    """
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    fsl = jinja2.FileSystemLoader(template_dir)
    env = jinja2.Environment(loader=fsl)
    template = env.get_template(template_file)
    output = template.render(service=template_options)

    log.info(f"Writing {output_path}...")
    with open(output_path, "w") as fh:
        fh.write(output)
        fh.close()

    return output


# -------------------------------------------------------------------------------- 
# Private interface
# -------------------------------------------------------------------------------- 



# -------------------------------------------------------------------------------- 
# Module test
# -------------------------------------------------------------------------------- 
if __name__ == "__main__":
    module_path = os.path.abspath(__file__)
    print(f"\nTesting {module_path}...")

    project_name = "test_project"
    deployment_env = "dev"

    project_path = getProjectPath(project_name)
    log.info(f"project_path: {project_path}")

    project_deployment_env_path = getProjectDeploymentEnvironmentPath(project_name, deployment_env)
    log.info(f"project_deployment_env_path: {project_deployment_env_path}")

    createProject(project_name, deployment_env)

    output_path = os.path.join(project_deployment_env_path, "test_file")
    template_file = "aws-rds-postgres.tmpl"
    template_options = {
        "project_name": project_name,
        "instance_count": 2,
        "instance_type": "db.t4g.micro",
        "deployment_region": "us-west-2",
        "master_username": "admin",
        "master_password": "alsdwheh*$#*#@lkajdfie"
    }
    renderTemplate(output_path, template_file, template_options)
