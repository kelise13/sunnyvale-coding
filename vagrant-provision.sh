sudo yum clean all
sudo yum install -y epel-release 
sudo yum install -y python34
curl -O https://bootstrap.pypa.io/get-pip.py
sudo /usr/bin/python3.4 get-pip.py
sudo ln -s /usr/bin/python3.4 /usr/local/bin/python3
 

