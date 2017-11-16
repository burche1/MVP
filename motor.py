""" Script to control the motors
Usage: 
Call: sudo python3 motor.py 1 7
In the call, must be passed 2 pins to control the specific motor
1,7 - m1
1,8 - m2
1,9 - m3
1,10 - m4
...
"""

import RPi.GPIO as GPIO
from time import sleep
import sys

# Setting GPIO
GPIO.setmode(GPIO.BOARD)

def set():
    # Setting pins
    # TODO: check the pins
    pin1 = 16
    pin2 = 18
    pin3 = 22
    pin4 = 16
    pin5 = 18
    pin6 = 22
    pin7 = 16
    pin8 = 18
    pin9 = 22
<<<<<<< HEAD
=======
    pin10 = 16
    pin11 = 18
    pin12 = 22
>>>>>>> 3134ad44e2ae4e331954ea713cef53cc01ffd19b

    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    GPIO.setup(pin4, GPIO.OUT)
    GPIO.setup(pin5, GPIO.OUT)
    GPIO.setup(pin6, GPIO.OUT)
    GPIO.setup(pin7, GPIO.OUT)
    GPIO.setup(pin8, GPIO.OUT)
    GPIO.setup(pin9, GPIO.OUT)
<<<<<<< HEAD
=======
    GPIO.setup(pin10, GPIO.OUT)
    GPIO.setup(pin11, GPIO.OUT)
    GPIO.setup(pin12, GPIO.OUT)
>>>>>>> 3134ad44e2ae4e331954ea713cef53cc01ffd19b

def motor(p1, p2, t):
    """ Moving some specific motor for t seconds
    Parameters:
    -----------
    Inputs:
        motor (int): the specific motor
        t (int): seconds
    Returns:
    None
    """

    GPIO.output(p1, GPIO.HIGH)
<<<<<<< HEAD
   GPIO.output(p2, GPIO.HIGH)
	# Setting pins
	# TODO: check the pins
	pin1 = 16
	pin2 = 18
	pin3 = 22
	pin4 = 16
	pin5 = 18
	pin6 = 22
	pin7 = 16
	pin8 = 18
	pin9 = 22

	GPIO.setup(pin1, GPIO.OUT)
	GPIO.setup(pin2, GPIO.OUT)
	GPIO.setup(pin3, GPIO.OUT)
	GPIO.setup(pin4, GPIO.OUT)
	GPIO.setup(pin5, GPIO.OUT)
	GPIO.setup(pin6, GPIO.OUT)
	GPIO.setup(pin7, GPIO.OUT)
	GPIO.setup(pin8, GPIO.OUT)
	GPIO.setup(pin9, GPIO.OUT)

def motor(p1, p2, t):
	""" Moving some specific motor for t seconds
	Parameters:
	-----------
	Inputs:
		motor (int): the specific motor
		t (int): seconds
	Returns:
		None
	"""

    GPIO.output(p1, GPIO.HIGH)
   	GPIO.output(p2, GPIO.HIGH)
=======
    GPIO.output(p2, GPIO.HIGH)
>>>>>>> 3134ad44e2ae4e331954ea713cef53cc01ffd19b
    # print("Moving motor {}".format(motor))
    time.sleep(t) # must calibrate for the specific time
    GPIO.cleanup()

def main():
    """Main function, responsable for setting all the pins and passing 2 pins to control the motor
    Parameters:
    -----------
    None
    """

    set()
    p1, p2 = sys.argv[0], sys.argv[1] # Getting 2 pins for the matrix logic
    motor(p1, p2)

if __name__ == "__main__":
    main()
<<<<<<< HEAD
	"""Main function, responsable for setting all the pins and passing 2 pins to control the motor
	Parameters:
	-----------
	None
	"""

	set()
	p1, p2 = sys.argv[0], sys.argv[1] # Getting 2 pins for the matrix logic
	motor(p1, p2)

if __name__ == "__main__":
	main()
=======
>>>>>>> 3134ad44e2ae4e331954ea713cef53cc01ffd19b
