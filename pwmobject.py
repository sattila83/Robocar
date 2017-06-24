#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


class PWMObject:
	def __init__(self, port):
		self.port = port
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.port, GPIO.OUT)
		self.pwm = GPIO.PWM(self.port, 50) # 50 Hz (20 ms) - it would be nice to have it as a parameter

	def toPositive(self, length = 1):
		self.pwm.start(7.5)
		for i in range(75,100):
			self.pwm.ChangeDutyCycle(i/10.0)
			time.sleep(length/2.0/25.0)
		for i in range(100,75,-1):
			self.pwm.ChangeDutyCycle(i/10.0)
			time.sleep(length/2.0/25.0)
		self.pwm.ChangeDutyCycle(7.5)
		self.pwm.stop()

	def toNegative(self, length = 1):
		self.pwm.start(7.5)
		for i in range(75,50,-1):
			self.pwm.ChangeDutyCycle(i/10.0)
			time.sleep(length/2.0/25.0)
		for i in range(50,75):
			self.pwm.ChangeDutyCycle(i/10.0)
			time.sleep(length/2.0/25.0)
		self.pwm.ChangeDutyCycle(7.5)
		self.pwm.stop()

	def cleanup(self):
		GPIO.cleanup()

