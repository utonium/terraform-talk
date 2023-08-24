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
