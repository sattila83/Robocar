#!/usr/bin/env python

from position import Position

class Motor:
	def bypass(self):
		print("Bypassing")
		
	def moveToward(self, targetPosition):
		print("Moving toward %s" % (targetPosition))
