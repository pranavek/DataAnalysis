#Python
##Install version 3.4.3
sudo apt-get install python 3.4.3

##IPython
sudo apt-get install ipython-notebook

or

pip insatll 'ipython[all]'


cd /home/prnv/PythonStuffs

ipython notebook

##Anaconda
conda create -n name_project anaconda

activate name_project

###Adding and removing default packages -

conda config --add create_default_packages ipython

conda config --force --remove create_default_packages ipython

