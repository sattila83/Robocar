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
