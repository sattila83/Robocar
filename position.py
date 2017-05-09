#!/usr/bin/env python

import math

EARTH_RADIUS = 6371e3;

class Position:
	def __init__(self, lat = 0.0, lon = 0.0):
		self.lat = math.radians(float(lat))
		self.lon = math.radians(float(lon))

	def __cmp__(self, other):
		if 0.0 == self.distanceTo(other):
			return 0
		elif self.bearingTo(other) < other.bearingTo(self):
			return -1
		else:
			return 1

	def __repr__(self):
		return "(%(lat)f,%(lon)f)" % { 'lat': self.lat, 'lon': self.lon }

	def __str__(self):
		return "(%(lat)f,%(lon)f)" % { 'lat': math.degrees(self.lat), 'lon': math.degrees(self.lon) }

	@staticmethod
	def toDecimal(value, direction):
		parts = value.split('.')
		decimal = float("0." + parts[1]) / 60.0 # convert seconds
		decimal = decimal + (float(parts[0][-2:]) / 60.0) # convert minutes
		decimal = decimal + float(parts[0][:-2]) # convert hours
		if 'N' == direction or 'E' == direction:
			return decimal
		else:
			return 0.0 - decimal

	def distanceTo(self, otherPosition):
		deltaLat = otherPosition.lat - self.lat
		deltaLon = otherPosition.lon - self.lon
		squareOfHalfChordLength = math.sin(deltaLat / 2) * math.sin(deltaLat / 2) + math.cos(self.lat) * math.cos(otherPosition.lat) * math.sin(deltaLon / 2) * math.sin(deltaLon / 2)
		return EARTH_RADIUS * 2 * math.atan2(math.sqrt(squareOfHalfChordLength), math.sqrt(1 - squareOfHalfChordLength))

	def bearingTo(self, otherPosition):
		deltaLon = otherPosition.lon - self.lon
		beeringInRadians = math.atan2(math.sin(deltaLon) * math.cos(otherPosition.lat), math.cos(self.lat) * math.sin(otherPosition.lat) - math.sin(self.lat) * math.cos(otherPosition.lat) * math.cos(deltaLon))
		return (math.degrees(beeringInRadians) + 360.0) % 360.0

