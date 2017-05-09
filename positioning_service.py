#!/usr/bin/env python

import time

from position import Position
from serial_reader import SerialReader

from serial_reader import MODE_GPS_FIX_DATA

# initial values of constants need to be refined according to experience
# or they can be input variables, if that is considered to be better
NUMBER_OF_SAMPLES = 30.0
SAMPLING_TIME_SECONDS = 1

class PositioningService:

	@staticmethod
	def getActualPosition():
		reader = SerialReader()
		latSum = 0.0
		lonSum = 0.0
		for i in range(0,NUMBER_OF_SAMPLES):
			data = reader.read(MODE_GPS_FIX_DATA)
			parts = [part.strip() for part in data.split(',')]
			latSum = latSum + Position.toDecimal(parts[2], parts[3])
			lonSum = lonSum + Position.toDecimal(parts[4], parts[5])
			time.sleep(SAMPLING_TIME_SECONDS)
		return Position(latSum / NUMBER_OF_SAMPLES, lonSum / NUMBER_OF_SAMPLES)
