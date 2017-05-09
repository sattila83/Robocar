#!/usr/bin/env python

import time

from position import Position
from serial_reader import SerialReader

from serial_reader import MODE_GPS_FIX_DATA

class PositioningService:

	@staticmethod
	# initial values of input params need to be refined according to experience
	def getActualPosition(numberOfSamples = 30, samplingTimeInSeconds = 1.0):
		reader = SerialReader()
		latSum = 0.0
		lonSum = 0.0
		for i in range(0, numberOfSamples):
			data = reader.read(MODE_GPS_FIX_DATA)
			parts = [part.strip() for part in data.split(',')]
			latSum = latSum + Position.toDecimal(parts[2], parts[3])
			lonSum = lonSum + Position.toDecimal(parts[4], parts[5])
			time.sleep(samplingTimeInSeconds)
		return Position(latSum / numberOfSamples, lonSum / numberOfSamples)
