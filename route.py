#!/usr/bin/env python

class Route:

	def __init__(self, actual_position, route_coordinates):
		# order the route_coordinates based on the actual_position
		distances = [actual_position.distanceTo(visitable_coordinate) for visitable_coordinate in route_coordinates]
		min_idx = Route._argmin(distances)
		
		self.ordered_coordinates = route_coordinates[min_idx:] + route_coordinates[0:min_idx]
		
		# if the first needs a turn greater than 90.0 degrees, set the next one to be first to avoid going backward
		angle_diff = abs(self.ordered_coordinates[0].bearingTo(self.ordered_coordinates[1]) - actual_position.bearingTo(self.ordered_coordinates[0]))
		if angle_diff > 90.0:
			firstToLast = self.ordered_coordinates[:1][0]
			self.ordered_coordinates = self.ordered_coordinates[1:]
			self.ordered_coordinates.append(firstToLast)
			
		# add actual position as last position to complete route
		self.ordered_coordinates.append(actual_position)

	@staticmethod
	def _argmin(array):
		array = list(array)
		return array.index(min(array))

	def getCurrentGoal(self):
		return self.ordered_coordinates[0]

	def markCurrentGoalVisited(self):
		self.ordered_coordinates = self.ordered_coordinates[1:]

	def done(self):
		return 0 == len(self.ordered_coordinates)
