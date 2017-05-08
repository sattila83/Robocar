#!/usr/bin/env python

# Dummy class for development

from pwm import PWM as DummyPWM

BCM = "BCM"
BOARD = "BOARD"
IN = "INPUT"
OUT = "OUTPUT"

def setmode(mode):
	print("GPIO setmode() - pin mode: %s" % mode)

def setup(port, mode):
	print("GPIO setup() - port: %s, io mode: %s" % (port, mode))

def PWM(port, frequency):
	print("GPIO PWM() - port: %s, frequency: %s Hz" %  (port, frequency))
	return DummyPWM()

def cleanup():
	print("GPIO cleaning up")