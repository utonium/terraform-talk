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
import os
import sys

import log

# -------------------------------------------------------------------------------- 
# Public interface
# -------------------------------------------------------------------------------- 
def renderTerraformTemplate(output_path: str, template_file: str, template_options: dict = {}) -> str:
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

# -------------------------------------------------------------------------------- 
# Private interface
# -------------------------------------------------------------------------------- 



# -------------------------------------------------------------------------------- 
# Module test
# -------------------------------------------------------------------------------- 
if __name__ == "__main__":
    module_path = os.path.abspath(__file__)
    print(f"\nTesting {module_path}...")

    project_path = getProjectPath("test_project")
    log.info(f"project_path: {project_path}")

    project_deployment_env_path = getProjectDeploymentEnvironmentPath("test_project", "dev")
    log.info(f"project_deployment_env_path: {project_deployment_env_path}")

    output_path = os.path.join(project_deployment_env_path, "test_file")
    template_file = ""
    template_options = {
        XXX: ""
    }
#    renderTerraformTemplate(output_path, template_path, template_options)

