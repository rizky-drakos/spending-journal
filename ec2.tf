#################################################
#
# This Terraform file helps to create ec2 
# instances of the t2.micro instance type. The 
# security group being used has an inbound for 
# port 22, which allows us to connect to the 
# instances via SSH.
# The public IP address of the instance is added 
# to the inventory file, which can be further 
# used in provisioning the instance.
#
#################################################
provider "aws" {
    region = "ap-southeast-1"
}

resource "aws_instance" "spending-journal-server" {
    ami = "ami-08569b978cc4dfa10"
    instance_type = "t2.micro"
    key_name = "SpendingJournalAWS"
    vpc_security_group_ids = ["sg-5d14ae2e"]
    tags = {
        Name = "spending-journal"
    }

    provisioner "local-exec" {
        command = "echo '${self.public_ip}' > inventory"
    }
}

output "public_ip" {
    value = "${aws_instance.spending-journal-server.public_ip}"
}