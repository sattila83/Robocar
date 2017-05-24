#!/usr/bin/env python

import time

from position import Position
from serial_reader import SerialReader

from serial_reader import MODE_GPS_FIX_DATA

class PositioningService:

	@staticmethod
	# initial values of input params need to be refined according to experience
	def getActualPosition(numberOfSamples = 5, samplingTimeInSeconds = 1.0):
		print "Reading GPS data for " + numberOfSamples * samplingTimeInSeconds + " seconds"
		reader = SerialReader()
		latSum = 0.0
		lonSum = 0.0
		validSampleCount = 0
		for i in range(0, numberOfSamples):
			data = reader.read(MODE_GPS_FIX_DATA)
			parts = [part.strip() for part in data.split(',')]
			if len(parts) > 5 and len(parts[2]) > 0 and len(parts[3]) > 0 and len(parts[4]) > 0 and len(parts[5]) > 0:
				validSampleCount += 1
				latSum = latSum + Position.toDecimal(parts[2], parts[3])
				lonSum = lonSum + Position.toDecimal(parts[4], parts[5])
			else:
				print data
			time.sleep(samplingTimeInSeconds)
		if validSampleCount == 0:
			return Position(0, 0)
		return Position(latSum / validSampleCount, lonSum / validSampleCount)
