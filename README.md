# Pronet
A psuedo Linked-In

Installation Guide for Centos 7 Server

#First Install pip and Python 3.X on CentOS 7
sudo yum install python34-setuptools
sudo easy_install pip

#Create venv using python 3.4
python3.4 -m venv py34env
py34env/bin/activate

#Check if django-admin is installed
pip install -U django

#Install Pronet, change myproj to your projects name

$ django-admin.py startproject --template=https://github.com/IantheFlyingHawaiian/Pronet.git --extension=py,md,html,env my_proj
$ cd my_proj
$ pip install -r requirements.txt 
$ cd src
$ cp my_proj/settings/local.sample.env my_proj/settings/local.env
$ python manage.py migrate
$ python manage.py createsuperuser
