#!/usr/bin/env python

from position import Position

class TestPosition:
	def test_init(self):
		# given
		p = Position(1.234567, 7.654321)
		# when
		
		# then
		assert 0.021547258986468833 == p.lat
		assert 0.1335931034545449 == p.lon

	def test_cmp_equals(self):
		# given
		p1 = Position(1.0, 1.0)
		p2 = Position(1.0, 1.0)
		
		# when
		cmp = p1 == p2
		
		# then
		assert True == cmp

	def test_cmp_greater(self):
		# given
		p1 = Position(1.0, 1.0)
		p2 = Position(0.0, 1.0)
		
		# when
		cmp = p1 > p2
		
		# then
		assert True == cmp

	def test_cmp_less(self):
		# given
		p1 = Position(1.0, 1.0)
		p2 = Position(2.0, 1.0)
		
		# when
		cmp = p1 < p2
		
		# then
		assert True == cmp

	def test_str(self):
		# given
		p = Position(1.234567, 7.654321)
		
		# when
		s = str(p)
		
		# then
		assert "(1.234567,7.654321)" == s

	def test_repr(self):
		# given
		p = Position(1.234567, 7.654321)
		
		# when
		s = repr(p)
		
		# then
		assert "(0.021547,0.133593)" == s

	def test_toDecimal(self):
		# given
		directions = [["N", 1], ["S", -1], ["E", 1], ["W", -1]]
		
		for direction in directions:
			# when
			actualDecimal = Position.toDecimal("00114.07402", direction[0])
		
			# then
			assert direction[1] * 1.234567 == actualDecimal

	def test_distanceTo(self):
		#given
		budapest = Position(47.49791, 19.04023)
		debrecen = Position(47.53160, 21.62731)
		
		# when
		distance = budapest.distanceTo(debrecen)
		
		# then
		assert 194 == int(round(distance / 1000))

	def test_bearingTo(self):
		# given
		basePos = Position(0.0, 0.0)
		
		# when
		northPos = Position(1.0, 0.0)
		southPos = Position(-1.0, 0.0)
		eastPos = Position(0.0, 1.0)
		westPos = Position(0.0, -1.0)
		
		# then
		assert 0.0 == basePos.bearingTo(northPos)
		assert 180.0 == basePos.bearingTo(southPos)
		assert 90.0 == basePos.bearingTo(eastPos)
		assert 270.0 == basePos.bearingTo(westPos)
