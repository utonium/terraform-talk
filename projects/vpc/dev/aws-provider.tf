# -------------------------------------------------------------------------------- 
# aws-provider.tf.tmpl
#
# DO NOT EDIT THIS FILE!!!! It is regenerated whenever `create-project` is run.
# Any change you make will be lost. If you need to change it, update the template
# for this file, located in <terraform-talk>/modules/python/terraform/templates
#
# Kevin Cureton 2023 covered by the gpl-3.0
# -------------------------------------------------------------------------------- 

terraform {
  required_providers {
    aws = {
      version = "5.13.1"
    }
  }
}

provider "aws" {
  region = "us-west-2"
  assume_role {
    role_arn = ""
    session_name = "terraform-vpc-us-west-2"
  }
}
