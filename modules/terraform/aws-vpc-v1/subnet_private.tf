# --------------------------------------------------------------------------------
# modules/terraform/aws-vpc-v1/subnet_private.tf
#
# Kevin Cureton 2023 covered by the gpl-3.0
# --------------------------------------------------------------------------------

variable "subnet_private_cidr_blocks_by_region" {
  default = {
    "us-west-2" = {
      "us-west-2a" = "172.30.0.0/20"
      "us-west-2b" = "172.30.16.0/20"
      "us-west-2c" = "172.30.32.0/20"
    }
  }
}

locals {
  subnet_private_cidr_blocks = var.subnet_private_cidr_blocks_by_region[var.deployment_region]
}

#
# Create private subnet
#
resource "aws_subnet" "private" {
  for_each = local.subnet_private_cidr_blocks

  vpc_id = aws_vpc.main.id

  cidr_block        = each.value
  availability_zone = each.key

  map_public_ip_on_launch = false

  depends_on = [ aws_vpc.main ]

  tags = {
    Name = format("private-subnet-%s", replace(each.key, var.deployment_region, "")),
  }
}
