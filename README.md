# Terraform Talk Assets

This repository goes along with my introductory talk about using
Terraform to create infrastructure in AWS. The tools are written in
Python 3 and Terraform. Jinja2 templates are used to instantiate 
Terraform code for a given Terraform module. The system is easily
expandable to support as many Terraform modules as you'd like.

The Python 3 code is structured so support for new Terraform modules
can easily be added to the `create-project` tool.

The `create-project` is the command line interface for creating a
new Terraform project that has it's own Terraform state. Everything
is vanilla Terraform, it's the only thing you need installed to run
the tools.

`create-project` can also be used to add new Terraform code to an
already existing project.

The link to the Terraform slides is

[Terraform Talk](https://docs.google.com/presentation/d/19xOjTywI4pWPDP43Fkz-_yd1q6-UCI8lWYl3VlQmr1g/edit?usp=sharing)

## AWS setup

For this example to work fully you'll need an Identity and Access Management (IAM) role
configured in AWS. The role must be assumable by the user account you are using to access
AWS. The `aws-provider.tf` file has blank fields for this role called `role_arn`. This role
controls what Terraform can do, so it needs permissions added to it for anything you'd
like to create.

There are also blank fields, `access_key` and `secret_key`, that need to be populated
with AWS access and secret keys for the user account that runs Terraform.

As a matter of security, never commit files to the repository have the access and secret
keys in them. A safer way to do this is using environment variables instead of defining
them in the `aws-provider.tf` file.

