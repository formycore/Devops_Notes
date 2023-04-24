resource "aws_instance" "web" {
    ami = "ami-08df646e18b182346"
    instance_type = "t2.micro"
    key_name = "xxx" # only pem file name without .pem extension
    subnet_id = aws_subnet.public-subnet[count.index].id
    vpc_security_group_ids = [aws_security_group.allow_demo.id]
    associate_public_ip_address = true
    count = 2

    tags = {
        Name = "WebServer"
    }

    provisioner "file" {
        source = "/home/ubuntu/xxxxx.pem"
        destination = "/home/ec2-user/xxxxx.pem"

        connection {
            type = "ssh"
            host = self.public_ip
            user = "ec2-user"
            private_key = "${file("/home/ubuntu/xxxxx.pem")}"
            #private_key = "${file("./xxxxx.pem")}"
        }
    }
}

# resource for the db with public ip
resource "aws_instance" "db" {
    ami = "ami-08df646e18b182346"
    instance_type = "t2.micro"
    key_name = "xxxxx"
    subnet_id = aws_subnet.private-subnet.id
    vpc_security_group_ids =  [aws_security_group.allow_demo.id]
    
    tags = {
        Name = "DB_Server"
    }
}