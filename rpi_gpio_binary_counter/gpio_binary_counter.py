#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

# Set pin assignment and the starting binary number with pinArray:
pinArray = [ [12,0] , [16,0] , [23,0] , [24,0] , [25,0] , [20,0] , [26,0] , [21,0] ]

GPIO.setmode(GPIO.BCM)

# Set up GPIO pins defined in pinArray LOW:
for i in pinArray:

	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.LOW)

sleep(1) 	# Wait a second...

# Set status of given GPIO pin to status:
def setPin(pin, status): 
	if status == 1:
		GPIO.output(pin, GPIO.HIGH)
	else:
		GPIO.output(pin, GPIO.LOW)

# Print the pinArray status to GPIO:
def printArray(array1):

	for i in range(0,len(array1)):
	
		setPin(array1[i][0], array1[i][1])

# Increment the binary component of array1. 
# array1 should be formatted as '[[pin0, bool0],..,[nx, boolx]]'
# e.g. input of [[23,1] , [24,1] , [25,0]] returns [[23,0] , [24,0] , [25,1]]:
def incArray(array1):

	pinArrayTemp1 = []

	# Converts the 3D array of pins and their binary component to a 2D array of binary:
	for i in range(0, len(array1)):
	
		pinArrayTemp1.append(array1[i][1])

	temp = 1	# Necessary to increment the array on first loop iteration.

	# Increments 2D binary array
	for i in range(0, len(pinArrayTemp1)):

		if temp == 1:

			if pinArrayTemp1[i] == 1:

				pinArrayTemp1[i] = 0
				temp = 1

			else:

				pinArrayTemp1[i] = 1
				temp = 0

	# Writes binary 2D array back to 3D array:
	for i in range(0, len(array1)):

		array1[i][1] = pinArrayTemp1[i]

# Run it baby!
try:

	while 1:
		
		printArray(pinArray)
		incArray(pinArray)
		sleep(.05) 	# Don't delete this!

except KeyboardInterrupt:

	GPIO.cleanup()
