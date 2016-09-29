# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "bento/centos-7.2"

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.network "private_network", ip: "192.168.99.100"

  config.vm.synced_folder ".", "/vagrant"

  config.vm.provision "shell", path: "vagrant-provision.sh"

end
