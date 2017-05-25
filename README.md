# python-on-off-button-RPi
self installing script 
that adds on,off function to Raspberry Pi(RPi)
it uses gpio library that id downloads and unpacks 
from 3rd party website rather than updating and upgrading
current distro. it also alters start up config and deletes
itself and reboots system after it ran.
uses button connected on pins 5 and 6 to create short circuit
and start Rpi.
Shut down and reboot are python issued commands depending 
on how long button has been pressed for on pin 11(gpio)17
led is connected to pin7 (gpio)4 to give visual feedback
schema of connection will be uploaded shortly and some pictures
will follow.
