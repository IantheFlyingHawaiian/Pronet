# Pronet
A psuedo Linked-In

Installation Guide for Centos 7 Server

#First Install pip and Python 3.X on CentOS 7
sudo apt-get install python-virtualenv </br>
virtualenv -p python3 myvenv </br>

#Create venv using python 3.4
python3.4 -m venv py34env </br>
py34env/bin/activate </br>

#Check if django-admin is installed
pip install -U django </br>

#Install Pronet, change myproj to your projects name

django-admin.py startproject --template=https://github.com/IantheFlyingHawaiian/Pronet.git --extension=py,md,html,env my_proj </br>
cd my_proj </br>
pip install -r requirements.txt  </br>
cd src  </br>
cp my_proj/settings/local.sample.env my_proj/settings/local.env  </br>
python manage.py migrate  </br>
python manage.py createsuperuser  </br>
