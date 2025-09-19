resource "aws_instance" "my_ec2" {
  ami           = "ami-0360c520857e3138f" # Amazon Linux 2 AMI ID (example)
  instance_type = "t2.micro"
  key_name      = "aws_key_laptop" # Your EC2 key pair

  tags = {
    Name = "MyEC2Instance"
  }
}