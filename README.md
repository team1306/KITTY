KITTY
=====
Kickass Interface Through Timed Yodeling

Dependencies
------------

* Apache2
* Mod_python
* Mod_pywebsockets
* pySerial
* Python 2.7
* Arduino IDE

Installation
------------

1. Install the dependencies with `sudo apt-get install libapache2-mod-python python-mod-pywebsocket python-serial`
2. Create a local copy of KITTY with `git clone http://github.com/quadthagoras/KITTY`
3. Move into the directory with `cd ./KITTY`
4. Update your apache configuration files:  
`sudo cp ./httpd.conf /etc/apache2/`  
`sudo cp ./default /etc/apache2/sites-available/`  
`sudo cp ./reqtimeout.conf /etc/apache2/mods-available/`
5. Restart the apache server with `sudo /etc/init.d/apache2 restart`
6. Move the pywebsocket handlers into the root apache directory with `sudo cp -r ./cgi-bin /var/www`
7. Move the rest of the necessary files into the same directory:  
`sudo cp ./index.php /var/www`  
`sudo cp ./index.js /var/www`  
`sudo cp ./roboserver.py /var/www`
8. 
