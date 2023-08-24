# --------------------------------------------------------------------------------
# modules/terraform/rds-postgresql-v1/api.tf
#
# Kevin Cureton 2023 covered by the gpl-3.0
# --------------------------------------------------------------------------------

variable "project_name" {}

variable "rds_deployment_region" {}

variable "rds_instance_count" {}

variable "rds_instance_type" {}

variable "rds_security_group_name" {}

variable "rds_master_username" {}

variable "rds_master_password" {}

variable "rds_preferred_maintenance_window" {
  default = "wed:16:00-wed:17:00"
}

variable "rds_monitoring_iam_role" {
  default = "rds-monitoring-role"
}

variable "rds_logs_exports" {
  default = {
    aurora-postgresql = ["postgresql"]
    postgres          = ["postgresql", "upgrade"]
  }
}

variable "rds_instance_monitoring_interval" {
  default = 60
}

variable "rds_backup_retention_period" {
  default = 35
}

variable "rds_skip_final_snapshot" {
  default = false
}
