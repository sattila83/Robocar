#!/usr/bin/env python

#import gps
#import motor
#import path
#import position

class Robocar:
	# constants need to be refined according to experience
	MIN_DISTANCE_BETWEEN_POSITIONS = 1
	MAX_DISTANCE_BETWEEN_POSITIONS = 10
	MIN_MOVEMENT_DISTANCE = 2
	
	def main(self):
		print("Starting route")
#		self.currentPosition = gps.getStable()
#		self.path = Path(self.refinedPositions, self.currentPosition)
#		self.targetPosition = self.path.next()
		
#		while True:
#			self.prevPosition = self.currentPosition
#			self.currentPosition = gps.update()
#			print("Actual position: %s" % (self.currentPosition))
			
			# when robot cannot move forward, bypass the obstacle
#			if self.currentPosition.distanceTo(self.prevPosition) < MIN_MOVEMENT_DISTANCE:
#				motor.bypass()
#			else:
#				motor.moveToward(self.targetPosition)
			
			# set target position to next when robot reached current target
#			if self.targetPosition.distanceTo(self.currentPosition) < MIN_DISTANCE_BETWEEN_POSITIONS:
#				self.targetPosition = self.path.next()

			# stop robot when it finished its route
#			if self.path.done() == True:
#				break
		print("Finished route")

	def __init__(self):
		self.milestones = []
#		self.milestones.extend(Position(47.47280197178266, 19.06173124909401))
#		self.milestones.extend(Position(47.47157893570410, 19.061355739831924))
#		self.milestones.extend(Position(47.471540474988444, 19.06233474612236))
#		self.milestones.extend(Position(47.47172508616688, 19.063498824834824))
#		self.milestones.extend(Position(47.47303529409086, 19.06308576464653))
		
#		self.refinedPositions = self.calculateRefinedPositions(MAX_DISTANCE_BETWEEN_POSITIONS)
