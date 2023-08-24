# --------------------------------------------------------------------------------
# modules/terraform/aws-vpc-v1/vpc.tf
#
# Kevin Cureton 2023 covered by the gpl-3.0
# --------------------------------------------------------------------------------

variable "vpc_cidr_block_by_region" {
  default = {
    "us-west-2" = "172.30.0.0/16"
  }
}

variable "availabilty_zones_by_region" {
  default = {
    "us-west-2" = [ "a", "b" ]
  }
}


locals {
  vpc_cidr_block = var.vpc_cidr_block_by_region[var.deployment_region]

  availability_zones       = var.availabilty_zones_by_region[var.deployment_region]
  availability_zones_count = length(var.availabilty_zones_by_region[var.deployment_region])
}

resource "aws_vpc" "main" {

  cidr_block = local.vpc_cidr_block

  enable_dns_support   = true
  enable_dns_hostnames = true

  assign_generated_ipv6_cidr_block = true

  tags = {
    Name = "${project_name}-${var.deployment_env}-vpc"
  }

  lifecycle {
    ignore_changes = [
      tags,
      enable_dns_hostnames,
    ]
  }
}
