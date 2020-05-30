#################################################
#
# This Vagrant file creates Ubuntu VMs and
# provisions them with the Ansible vm-setup 
# playbook.
#
#################################################
Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-18.04"
    # port 80 for the api.
    config.vm.network "forwarded_port", guest: 80, host: 80
    # port 5000 for the api.
    config.vm.network "forwarded_port", guest: 5000, host: 5000

    config.ssh.insert_key = false

    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "vm-setup.yml"
    end

end
