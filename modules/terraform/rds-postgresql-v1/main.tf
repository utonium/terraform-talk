# --------------------------------------------------------------------------------
# modules/terraform/rds-postgresql-v1/main.tf
#
# Kevin Cureton 2023 covered by the gpl-3.0
# --------------------------------------------------------------------------------

locals {
  rds_db_name = replace(var.project_name, "/^[[:digit:]]|[^0-9A-Za-z]+/", "")

  rds_engine = "aurora-postgresql"
  rds_engine_version = "13.4"

  rds_auto_minor_version_upgrade = true
}

#
# Database infrastructure configuration
#
resource "aws_iam_role" "rds-postgresql-monitoring-role" {
  name = var.rds_monitoring_iam_role
}

resource "aws_security_group" "rds-postgresql" {
  count = length(var.rds_security_group_name)

  name = var.rds_security_group_name[count.index]
}

resource "aws_kms_key" "rds-postgresql" {
  description = "${var.project_name} - rds"
}

resource "aws_kms_alias" "rds-postgresql" {
  name          = "alias/wish/tf-${var.project_name}"
  target_key_id = aws_kms_key.rds-postgresql.key_id
}

resource "aws_subnet" "rds-postgresql" {
}

resource "aws_db_subnet_group" "rds-postgresql" {
  name       = var.project_name
  subnet_ids = aws_subnet.rds-postgresql.*.id
}

#
# Database cluster configuration
#
resource "aws_rds_cluster" "rds-postgresql" {
  cluster_identifier           = var.project_name

  database_name                = local.rds_db_name
  engine                       = local.rds_engine
  engine_version               = local.rds_engine_version
  db_subnet_group_name         = aws_db_subnet_group.rds-postgresql.id
  vpc_security_group_ids       = length(var.rds_security_group_name) > 0 ? data.aws_security_group.rds-postgresql.*.id : null
  master_username              = var.rds_master_username
  master_password              = var.rds_master_password
  storage_encrypted            = true
  kms_key_id                   = aws_kms_key.rds-postgresql.arn
  backup_retention_period      = var.rds_backup_retention_period
  preferred_maintenance_window = var.rds_preferred_maintenance_window

  lifecycle {
    ignore_changes = [master_password]
  }

  skip_final_snapshot             = var.rds_skip_final_snapshot
  enabled_cloudwatch_logs_exports = var.rds_logs_exports[var.rds_engine]
}

#
# Database instance configuration
#
resource "aws_rds_cluster_instance" "rds-postgresql" {
  count = var.rds_instance_count

  identifier         = "${var.project_name}-${count.index}"
  cluster_identifier = aws_rds_cluster.rds-postgresql.id
  instance_class     = var.rds_instance_class
  engine             = local.rds_engine
  engine_version     = local.rds_engine_version

#  monitoring_role_arn = data.aws_iam_role.rds-postgresql-monitoring.arn
#  monitoring_interval = var.rds_instance_monitoring_interval

  performance_insights_enabled = true

  preferred_maintenance_window = var.rds_preferred_maintenance_window
  auto_minor_version_upgrade   = local.rds_auto_minor_version_upgrade
}
