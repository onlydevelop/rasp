#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time

redLight = 20
greenLight = 21
buzzer = 16
on = 1
state = 1
numTimes = 5
redLightWait = 3
greenLightWait = 2

def run():
	setGPIO()
	arg = getArgument()
	if (arg == 'red'):
		showRed()
	elif (arg == 'green'):
		showGreen()
	else:
		runAuto()
	cleanup()
	
def getArgument():
	if len(sys.argv) > 1:
		return sys.argv[1]
	else:
		return 'auto'

def setGPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(redLight, GPIO.OUT)
	GPIO.setup(greenLight, GPIO.OUT)
	GPIO.setup(buzzer, GPIO.OUT)

def runAuto():
	global state
	for i in range(0, numTimes):
		GPIO.output(redLight, state)
		GPIO.output(greenLight, not(state))
		if(state):
			time.sleep(redLightWait)
		else:
			time.sleep(greenLightWait)
		state = not(state)
		beep()

def showRed():
	GPIO.output(redLight, on)
	GPIO.output(greenLight, not(on))
	time.sleep(redLightWait)
	beep()

def showGreen():
	GPIO.output(greenLight, on)
	GPIO.output(redLight, not(on))
	time.sleep(greenLightWait)
	beep()

def beep():
	for i in range(0, 1):
		GPIO.output(buzzer, 1);
		time.sleep(0.2);
		GPIO.output(buzzer, 0);
		time.sleep(0.2);

def cleanup():
	GPIO.cleanup()

if __name__ == "__main__":
	run()
