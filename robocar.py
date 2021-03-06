#!/usr/bin/env python

from motor import MotorControl
from position import Position
from route import Route
from positioning_service import PositioningService

# constants need to be refined according to experience
MIN_DISTANCE_BETWEEN_POSITIONS = 4    #07.05
MAX_DISTANCE_BETWEEN_POSITIONS = 10
MIN_MOVEMENT_DISTANCE = 1
MINIMUM_ANGLE = 30

class Robocar:
	
	def __init__(self, positions = []):
		self.basePositions = positions
	
	def start(self):
		with MotorControl() as motor:
			print("Starting route")
			
			actualPosition = PositioningService.getActualPosition()
			print("Actual position: %s" % (actualPosition))
			route = Route(actualPosition, self.basePositions) # determine path based on actual position
			print("Planned route: %s" % (Position.positionListToStr(route.ordered_coordinates)))
			 
			while not route.done(): # do until the end of the path is reached
				motor.moveForward(3) #07.05
				previousPosition = actualPosition
				actualPosition = PositioningService.getActualPosition()
				print("Actual position: %s" % (actualPosition))
				if actualPosition.isNull():
					print 'No GPS'
					break				

				# check if the robot could not move in the previous iteration
				#if (actualPosition.distanceTo(previousPosition) < MIN_MOVEMENT_DISTANCE):
				#	motor.dodge() # random dodge, as the robot doesn't know its environment
				#	continue
				
				closestVisitable = route.getCurrentGoal()
				print("Current goal: %s" % (closestVisitable))
				distanceToGoal = actualPosition.distanceTo(closestVisitable)
				print("Distance to goal: %s meters" % (distanceToGoal))
				
				if distanceToGoal < MIN_DISTANCE_BETWEEN_POSITIONS: # actual goal is reached
					route.markCurrentGoalVisited()
				
				# check if the direction is right
				closestVisitable = route.getCurrentGoal()
				angleDifference = Robocar.getAngleDifference(previousPosition, actualPosition, closestVisitable)
				print("Angle difference: %s" % (angleDifference))
				
				# turn if refinement is needed
				if abs(angleDifference) > MINIMUM_ANGLE:
					if angleDifference < 0:
						motor.turnLeft(0.5)
					else:
						motor.turnRight(0.5)
		print("Finished route")

	@staticmethod
	def getAngleDifference(previousPosition, actualPosition, goalPosition):
		# when the last goal is reached no more refinement is needed
		if goalPosition is None:
			return 0.0
			
		actualAngleToNorth = previousPosition.bearingTo(actualPosition)
		desiredAngleToNorth = actualPosition.bearingTo(goalPosition)
		difference = desiredAngleToNorth - actualAngleToNorth
		# if angle difference is wider than 180 degrees, turn to opposite direction
		if difference > 180.0:
			return difference - 360.0
		elif difference < -180.0:
			return difference + 360.0
		else:
			return difference
