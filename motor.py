#!/usr/bin/env python

from pwmobject import PWMObject
from random import randint

class MotorFunctions:

	@staticmethod
	def dodge():
		print("Bypassing obstacle")
		drive = PWMObject(21) # port 21 for driving
		turn = PWMObject(20) # port 20 for turning
		drive.toNegative()
		left = randint(0,1)
		if left:
			turn.toPositive()
		else:
			turn.toNegative()
		drive.toPositive()
		if not left:
			turn.toPositive()
		else:
			turn.toNegative()
		drive.cleanup()
		turn.cleanup()

	@staticmethod
	def moveForward():
		print("Moving forward")
		drive = PWMObject(21) # port 21 for driving
		drive.toPositive()
		drive.cleanup()

	@staticmethod
	def moveBackward():
		print("Moving backward")
		drive = PWMObject(21) # port 21 for driving
		drive.toNegative()
		drive.cleanup()

	@staticmethod
	def turnLeft():
		print("Turning left")
		turn = PWMObject(20) # port 20 for turning
		turn.toPositive()
		turn.cleanup()

	@staticmethod
	def turnRight():
		print("Turning right")
		turn = PWMObject(20) # port 20 for turning
		turn.toNegative()
		turn.cleanup()
