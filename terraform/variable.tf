variable "region" {
  type    = string
  default = "us-east-1"
}


variable "bucket_prefix" {
  description = "Unique prefix for S3 buckets. Must be globally unique."
  type        = string
}


variable "key_pair_name" {
  type = string
}


variable "allowed_cidr" {
  type        = string
  description = "CIDR allowed to SSH into EC2 (your IP)."
}


variable "instance_type" {
  type    = string
  default = "t3.medium"
}


variable "schedule_expression" {
  type    = string
  default = "cron(0/5 * * * ? *)" # run daily at 06:00 UTC
}
