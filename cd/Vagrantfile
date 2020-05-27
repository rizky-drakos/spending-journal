Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-18.04"

    config.ssh.insert_key = false

    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "vm-setup.yml"
    end

end
