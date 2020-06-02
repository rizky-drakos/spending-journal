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
    ami = "ami-0615132a0f36d24f4"
    instance_type = "t2.micro"
    key_name = "SpendingJournalAWS"
    vpc_security_group_ids = ["sg-5d14ae2e"]
    tags = {
        Name = "spending-journal"
    }

    # local-exec provisioner will not wait till the ssh connection is established,
    # but remote-exec does.
    provisioner "remote-exec" {
      connection {
        type = "ssh"
        host = self.public_ip
        user = "ec2-user"
        private_key = file("SpendingJournalAWS.pem")
      }
    }

    provisioner "local-exec" {
        command = "echo '${self.public_ip}' > inventory"
    }

    provisioner "local-exec" {
        command = "ansible-playbook --private-key SpendingJournalAWS.pem -u ec2-user -i inventory ec2-setup.yml"
    }
}

output "public_ip" {
    value = "${aws_instance.spending-journal-server.public_ip}"
}