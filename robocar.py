#!/usr/bin/env python

#import gps
from motor import MotorFunctions
from position import Position
from route import Route
from positioning_service import PositioningService

# constants need to be refined according to experience
MIN_DISTANCE_BETWEEN_POSITIONS = 1
MAX_DISTANCE_BETWEEN_POSITIONS = 10
MIN_MOVEMENT_DISTANCE = 2
MINIMUM_ANGLE = 30

class Robocar:
	
	def __init__(self, positions = []):
		self.basePositions = positions
	
	def start(self):
		print("Starting route")
		
		actualPosition = PositioningService.getActualPosition()
		route = Route(actualPosition, self.basePositions) # determine path based on actual position
		 
		while not route.done(): # do until the end of the path is reached
			previousPosition = actualPosition
			actualPosition = PositioningService.getActualPosition()
			print("Actual position: %s" % (actualPosition))
			
			# check if the robot could not move in the previous iteration
			if (actualPosition.distanceTo(previousPosition) < MINIMUM_DISTANCE_TO_OTHER_COORD):
				MotorFunctions.dodge() # random dodge, as the robot doesn't know its environment
				continue
			
			closestVisitable = route.getCurrentGoal()
			distanceToGoal = actualPosition.distanceTo(closestVisitable)
			
			if distanceToGoal < MINIMUM_DISTANCE_TO_OTHER_COORD: # actual goal is reached
				route.markCurrentGoalVisited()
			
			# check if the direction is right
			actualAngleToNorth = previousPosition.bearingTo(actualPosition)
			desiredAngleToNorth = actualPosition.bearingTo(route.getCurrentGoal())
			angleDifference = actualAngleToNorth - desiredAngleToNorth
			
			# turn if refinement is needed
			if abs(angleDifference) > MINIMUM_ANGLE:
				if angleDifference < 0:
					MotorFunctions.turnLeft()
				else:
					MotorFunctions.turnRight()
			
			MotorFunctions.moveForward()
		print("Finished route")

