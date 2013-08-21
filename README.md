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
`sudo cp ./apache/httpd.conf /etc/apache2/`  
`sudo cp ./apache/default /etc/apache2/sites-available/`  
`sudo cp ./apache/reqtimeout.conf /etc/apache2/mods-available/`
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

Files
-----

###index.php

The driver station for this robot can be any internet capable device, from a tablet to a laptop, as long as it can access the Pi's webpage. An Apache server running on the Pi serves this webpage to any computer connected to the Pi's Ad Hoc network. This page includes authentication, and will eventually allow the driver to use joysticks, XBox controllers, or the arrow keys through HTML5.

Data in the form of comma-separated values is sent via websocket back to the server. This string will take on different meanings depending on the module in use.

###cgi-bin/data_wsh.py

Whenever Apache recieves a websocket connection, pywebsockets makes it look in cgi-bin for the right handler. In this case, all the handler does is open a socket to `roboserver.py` and pass along the data recieved.

###roboserver.py

First, the script listens for a first time connection from the driver station. After it has recieved the name of the module to use, it proceeds to listening for control strings.

Since the Arduino needs constant supervision to stay active, the control loop resides in `roboserver.py` and listens for the occassional string from `cgi-bin/data_wsh.py`. When first run, it creates a Robot object (from `robot.py`) to handle the parsing of the string, interpretation of commands, and communication with the Arduino. If a second passes without a string being sent from the driver station, `robot.safeMode()` is called to send the shutoff signal to the Arduino and it goes back to listening for a connection.

All this script is doing is juggling sockets, handling timeouts, and passing the control string to the Robot instance.

###robot.py

In the constructor, `self.driverBase` is a new Mecanum drive. The Mecanum class resides in `mecanum.py` and does all the math necessary to turn linear and angular velocities from the controls into motor speeds for each of the wheels. `getInstance(module, usbPort, chip)` comes from modules and allows Robot to flash the Arduino with the right code and get an instance of the correct module class by simply passing a string with the modules name.

All `update` does is take the control string, parse it, interpret it, and communicate the commands to the Arduino using the correct protocol. Sometimes, two strings set from `cgi-bin/data_wsh.py` arrive at `roboserver.py` so quickly that it reads them as one string. To solve this problem, each string is formatted like `x,y,x;` so that double strings will simply be `x,y,z;a,b,c;`. We can then simply split each and every string recieved at each semicolon and handle the strings one by one. However, the python split command will return `['x,y,z', 'a,b,c', '']` for the second example string and `['x,y,z', '']` for the first one so we have to remove the last element of the list in every case.

Then, for each string in the list, it interprets the first two values as instructions for the drive train and uses `self.driveBase.getBytes` to generate the necessary bytes to send to the Arduino. It appends these to a list of bytes. Secondly, if the module was specified, then it also adds the bytes generated by the module (`self.module.getBytes(data)`). In terms of modularity, this means that every module class needs only have a `getBytes` method to function properly. Each module can do whatever it wants internally as long as it has this vital method.

###mecanum.py

The constructor simply takes the extreme values it can expect from the input and the range of values it is allowed to give as output as well as setteing two physical dimensions necessary for the math to work out. `getVelocities` converts the ideal robot velocities into motor speeds which always proceed to be scaled by `scaleVelocities` so that no speed exceeds the maximum given to the constructor. `getBytes` runs `getVelocities` and `scaleVelocities` and then returns the values in byte form to be sent to the Arduino.

###modules/__init__.py

Primarily, this file is required for python to see this directory as a module, but it's also a nice place to put general functions that will be included when any other script runs `import modules` that are independent of any of the submodules. `flashArduino` finds the right code for the specified module name and flashes it to the Arduino, and it is called by `getInstance` which also returns an instance of the class corresponding to the module name specified. `getModules` simply lists out the available modules.

This is the part that allows for the easy development of more modules. Each module requires an Ino project in the correct location with the right name to run the Arduino, a class in `modules` by the right name with a `getBytes` method, an `elif` line in `getInstance`, and its name in `getModules`.

###modules/arm.py

Empty module class to be written later.

###modules/shooter.py

Empty module class to be written later.
