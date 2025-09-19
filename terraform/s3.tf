resource "aws_s3_bucket" "my_bucket" {
  bucket = "suresh-sports-pipeline-bucket"
  acl    = "private"
}
