#!/usr/bin/env python

from pwmobject import PWMObject
from random import randint

class MotorFunctions:
	def dodge(self):
		print("Bypassing obstacle")
		drive = PWMObject(21) # port 21 for driving
		turn = PWMObject(20) # port 20 for turning
		drive.toNegative()
		left = random.randint(0,1)
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

	def moveForward(self):
		print("Moving forward")
		drive = PWMObject(21) # port 21 for driving
		drive.toPositive()

	def moveBackward(self):
		print("Moving backward")
		drive = PWMObject(21) # port 21 for driving
		drive.toNegative()

	def turnLeft(self):
		print("Turning left")
		turn = PWMObject(20) # port 20 for turning
		turn.toPositive()

	def turnRight(self):
		print("Turning right")
		turn = PWMObject(20) # port 20 for turning
		turn.toNegative()
