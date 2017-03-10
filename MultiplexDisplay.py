#!/usr/bin/python

# This is just a simple countdown timer which counts down from
# 50 to 1. This is just kept for reference because, there are
# functions zero(), one() etc. which I do not want to write ever.

import RPi.GPIO as GPIO
import sys
import time
import signal
import warnings

startFrom = 50
a = 5
b = 6
c = 13
d = 19
e = 20
f = 21
g = 26
e0 = 12
e1 = 16
on = 1
off = 0

def setGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(a, GPIO.OUT)
    GPIO.setup(b, GPIO.OUT)
    GPIO.setup(c, GPIO.OUT)
    GPIO.setup(d, GPIO.OUT)
    GPIO.setup(e, GPIO.OUT)
    GPIO.setup(f, GPIO.OUT)
    GPIO.setup(g, GPIO.OUT)
    GPIO.setup(e0, GPIO.OUT)
    GPIO.setup(e1, GPIO.OUT)

def zero():
    GPIO.output(a, on)
    GPIO.output(b, on)
    GPIO.output(c, on)
    GPIO.output(d, on)
    GPIO.output(e, on)
    GPIO.output(f, on)
    GPIO.output(g, off)

def one():
    GPIO.output(a, off)
    GPIO.output(b, on)
    GPIO.output(c, on)
    GPIO.output(d, off)
    GPIO.output(e, off)
    GPIO.output(f, off)
    GPIO.output(g, off)

def two():
    GPIO.output(a, on)
    GPIO.output(b, on)
    GPIO.output(c, off)
    GPIO.output(d, on)
    GPIO.output(e, on)
    GPIO.output(f, off)
    GPIO.output(g, on)

def three():
    GPIO.output(a, on)
    GPIO.output(b, on)
    GPIO.output(c, on)
    GPIO.output(d, on)
    GPIO.output(e, off)
    GPIO.output(f, off)
    GPIO.output(g, on)

def four():
    GPIO.output(a, off)
    GPIO.output(b, on)
    GPIO.output(c, on)
    GPIO.output(d, off)
    GPIO.output(e, off)
    GPIO.output(f, on)
    GPIO.output(g, on)

def five():
    GPIO.output(a, on)
    GPIO.output(b, off)
    GPIO.output(c, on)
    GPIO.output(d, on)
    GPIO.output(e, off)
    GPIO.output(f, on)
    GPIO.output(g, on)

def six():
    GPIO.output(a, on)
    GPIO.output(b, off)
    GPIO.output(c, on)
    GPIO.output(d, on)
    GPIO.output(e, on)
    GPIO.output(f, on)
    GPIO.output(g, on)

def seven():
    GPIO.output(a, on)
    GPIO.output(b, on)
    GPIO.output(c, on)
    GPIO.output(d, off)
    GPIO.output(e, off)
    GPIO.output(f, off)
    GPIO.output(g, off)

def eight():
    GPIO.output(a, on)
    GPIO.output(b, on)
    GPIO.output(c, on)
    GPIO.output(d, on)
    GPIO.output(e, on)
    GPIO.output(f, on)
    GPIO.output(g, on)

def nine():
    GPIO.output(a, on)
    GPIO.output(b, on)
    GPIO.output(c, on)
    GPIO.output(d, on)
    GPIO.output(e, off)
    GPIO.output(f, on)
    GPIO.output(g, on)

def enable(state):
    GPIO.output(e0, state)
    GPIO.output(e1, not(state))

def aa():
    print("hello")

def printNumber(num):
    tens = num / 10;
    ones = num % 10;
    func_map = {
        '1': one,
        '2': two,
        '3': three,
        '4': four,
        '5': five,
        '6': six,
        '7': seven,
        '8': eight,
        '9': nine,
        '0': zero
    }

    enable(1)
    func_map[str(tens)]()
    time.sleep(0.01)
    enable(0)
    func_map[str(ones)]()
    time.sleep(0.01)

def showNum():
    setGPIO()
    for num in range(startFrom,0,-1):
        for i in range(1, 50):
            printNumber(num)
            time.sleep(0.001)
    cleanup()

with warnings.catch_warnings():
    GPIO.cleanup()

def ctrlCHandler(signal, frame):
    print('Exiting...')
    cleanup()
    sys.exit(0)

def cleanup():
    GPIO.cleanup()

signal.signal(signal.SIGINT, ctrlCHandler)

if __name__ == "__main__":
    showNum()
