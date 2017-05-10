#!/usr/bin/env python

import mock
import math
import time

import robocar
from position import Position

TEST_ROUTE = [Position(0.0, 0.0), Position(2.0, 0.0), Position(2.0, 2.0), Position(0.0, 2.0)]

class TestRobocar:

	@mock.patch('robocar.PositioningService', autospec=True)
	def start(self, PositioningServiceMock):
		# given
		r = robocar.Robocar(TEST_ROUTE)
		mockedPositions = self.mockActualPositions()
		mockedPositions = mockedPositions[:-1] + mockedPositions
		PositioningServiceMock.getActualPosition.side_effect = mockedPositions
		
		# when
		r.start()
		
		# then
		assert True # if loop in Robocar.start() stops, no error happened

	def test_getAngleDifferenceWithNoGoal(self):
		# when
		result = robocar.Robocar.getAngleDifference(Position(0.0, 1.0), Position(1.0, 1.0), None)
		
		# then
		assert 0.0 == result

	def test_getAngleDifferenceBetween180AndMinus180(self):
		# given
		prev = Position(0.0, 1.0)
		act = Position(1.0, 1.0)
		goal = Position(1.0, 2.0)
		expectedResult = act.bearingTo(goal) - prev.bearingTo(act)
		
		# when
		actualResult = robocar.Robocar.getAngleDifference(prev, act, goal)
		
		# then
		assert expectedResult == actualResult

	def test_getAngleDifferenceLessThanMinus180(self):
		# given
		prev = Position(0.0, 1.0)
		act = Position(0.0, 0.0)
		goal = Position(1.0, 0.0)
		expectedResult = (act.bearingTo(goal) - prev.bearingTo(act)) + 360.0
		
		# when
		actualResult = robocar.Robocar.getAngleDifference(prev, act, goal)
		
		# then
		assert expectedResult == actualResult

	def test_getAngleDifferenceMoreThan180(self):
		# given
		prev = Position(0.0, 0.0)
		act = Position(1.0, 0.0)
		goal = Position(1.0, -1.0)
		expectedResult = (act.bearingTo(goal) - prev.bearingTo(act)) - 360.0
		
		# when
		actualResult = robocar.Robocar.getAngleDifference(prev, act, goal)
		
		# then
		assert expectedResult == actualResult

	def mockActualPositions(self):
		actualPosition = Position(1.0, 0.0)
		
		positions = []
		positions.append(actualPosition)
		
		calculatedRoute = []
		calculatedRoute = TEST_ROUTE[1:] + TEST_ROUTE[:1]
		calculatedRoute.append(actualPosition)
		
		for r in calculatedRoute:
			while round(r.distanceTo(actualPosition)) > 0.0:
				if round(actualPosition.lat, 6) < round(r.lat, 6):
					actualPosition = Position(math.degrees(actualPosition.lat) + 0.5, math.degrees(actualPosition.lon))
				elif round(actualPosition.lat, 6) > round(r.lat, 6):
					actualPosition = Position(math.degrees(actualPosition.lat) - 0.5, math.degrees(actualPosition.lon))
				if round(actualPosition.lon, 6) < round(r.lon, 6):
					actualPosition = Position(math.degrees(actualPosition.lat), math.degrees(actualPosition.lon) + 0.5)
				elif round(actualPosition.lon, 6) > round(r.lon, 6):
					actualPosition = Position(math.degrees(actualPosition.lat), math.degrees(actualPosition.lon) - 0.5)
				positions.append(actualPosition)
		return positions
