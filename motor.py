#!/usr/bin/env python

from pwmobject import PWMObject
from random import randint

class MotorControl:

	def __init__(self):
		self.drive = PWMObject(21)
		self.turn = PWMObject(20)
		
	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.drive.cleanup()
		self.turn.cleanup()


	def dodge(self):
		print("Bypassing obstacle")
		self.drive.toNegative(2)
		left = randint(0,1)
		if left:
			self.turn.toPositive()
		else:
			self.turn.toNegative()
		self.drive.toPositive(2)
		if not left:
			self.turn.toPositive()
		else:
			self.turn.toNegative()

	def moveForward(self, length = 1):
		print("Moving forward")
		self.drive.toPositive(length)

	def moveBackward(self, length = 1):
		print("Moving backward")
		self.drive.toNegative(length)

	def turnLeft(self, length = 0.75):
		print("Turning left")
		self.turn.toPositive(length)

	def turnRight(self, length = 0.75):
		print("Turning right")
		self.turn.toNegative(length)

	
		