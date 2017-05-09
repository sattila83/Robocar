#!/usr/bin/env python

import math

from position import Position
from route import Route

TEST_ACTUAL_POSITION = Position(1.4, 2.0)
TEST_ACTUAL_POSITION_2 = Position(1.9, 1.0)
TEST_ROUTE = [Position(0.5, 1.0), Position(1.0, 1.0), Position(2.0, 1.0), Position(3.0, 1.0)]
EXPECTED_ROUTE = [Position(2.0, 1.0), Position(3.0, 1.0), Position(0.5, 1.0), Position(1.0, 1.0), Position(1.4, 2.0)]
EXPECTED_ROUTE_2 = [Position(2.0, 1.0), Position(3.0, 1.0), Position(0.5, 1.0), Position(1.0, 1.0), Position(1.9, 1.0)]

class TestRoute:
	def test_argmin(self):
		testArray = [3.2, 1.0, 2.5, 1.1]
		minIndex = Route._argmin(testArray)
		assert 1 == minIndex

	def test_initWithWideAngle(self):
		# when
		actual = Route(TEST_ACTUAL_POSITION, TEST_ROUTE)
		
		# then
		for i in range(0, len(actual.ordered_coordinates)):
			assert actual.ordered_coordinates[i] == EXPECTED_ROUTE[i]

	def test_initWithNarrowAngle(self):
		# when
		actual = Route(TEST_ACTUAL_POSITION_2, TEST_ROUTE)
		
		# then
		for i in range(0, len(actual.ordered_coordinates)):
			assert actual.ordered_coordinates[i] == EXPECTED_ROUTE_2[i]

	def test_getCurrentGoal(self):
		# given
		route = Route(TEST_ACTUAL_POSITION, TEST_ROUTE)
		
		# when
		actualGoal = route.getCurrentGoal()
		
		# then
		assert EXPECTED_ROUTE[0] == actualGoal

	def test_markCurrentGoalVisited(self):
		# given
		route = Route(TEST_ACTUAL_POSITION, TEST_ROUTE)
		expectedNumberOfPositions = len(route.ordered_coordinates) - 1
		
		# when
		route.markCurrentGoalVisited()
		
		# then
		assert len(route.ordered_coordinates) == expectedNumberOfPositions

	def test_done(self):
		# given
		route = Route(TEST_ACTUAL_POSITION, TEST_ROUTE)
		
		# when
		for i in range(0, len(EXPECTED_ROUTE)):
			route.markCurrentGoalVisited()
		
		# then
		assert route.done()
