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
* Ino

Installation
------------

1. Install the dependencies with `sudo apt-get install libapache2-mod-python python-mod-pywebsocket python-serial arduino`
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
8. Download the latest version of Ino with `wget https://pypi.python.org/packages/source/i/ino/ino-0.3.5.tar.gz`
9. Unpack with `tar -xzf ./ino-0.3.5.tar.gz`
10. Move into directory with `cd ./ino-0.3.5`
11. Install with `sudo python setup.py install`
12. cd into your local copy of KITTY
13. `cd ./robocontrol/`
14. Run `ino list-models` and find your Arduino's model in the list
15. Build the .hex for the Arduino for you model (in this case an Arduino Duemilanove) with `ino build -m atmega328` after replacing `atmega328` with your Arduino's model
16. Upload to the Arduino with `ino upload -m atmega328`, again replacing `atmega328` with your model
17. cd into your local copy of KITTY
18. Start the KITTY server with `python ./roboserver.py`
19. Hook up PWM controllers to the appropriate Arduino ports
20. Browse to the Pi's IP address from another computer and enjoy controlling your robot!
