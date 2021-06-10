1.Install Anaconda Python 3.8 64-Bit (x86) Installer (529 MB) 2.6.0
put folder in  Home directory

2.Change to course folder 
$cd djangov

3.Create the course environment
$conda env create

4.Activate the environment (Mac/Linux)
$conda activate djangov

5.Check that your prompt changed to
(djangov) $cd ~

6.start the web server by running command-line
$cd ~/djangov/mysite/
$python manage.py runserver 0.0.0.0:8000

7.Open your browser on host(Firefox, Chrome or whatever you use) 
and enter this address:
http://192.168.109.129:8000/

**Not a necessary step**
8.deactivate the environment (Mac/Linux):
$conda deactivate

9.delete the environment
$conda remove -y -n djangov --all

These instructions have been tested on:
VM Ubuntu 20.04
Host Win10 20H2


