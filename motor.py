#!/usr/bin/env python

#import Position from position

class Motor:
	def bypass(self):
		print("Bypassing")
		
	def moveToward(self, targetPosition):
		print("Moving toward %s" % (targetPosition))
