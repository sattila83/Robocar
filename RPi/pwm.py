#!/usr/bin/env python

class PWM:
	def __init__(self):
		print("PWM __init__()")

	def start(self, dutyCycle):
		print("PWM start() - dutyCycle: %s" % dutyCycle)

	def ChangeDutyCycle(self, dutyCycle):
		print("PWM ChangeDutyCycle() - dutyCycle: %s" % dutyCycle)

	def stop(self):
		print("PWM stop()")
