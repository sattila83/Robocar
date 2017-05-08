#!/usr/bin/env python

from serial import Serial
from serial import PARITY_NONE
from serial import STOPBITS_ONE
from serial import EIGHTBITS

MODE_GPS_FIX_DATA = "GPGGA"
MODE_OVERALL_SATELLITE_DATA = "GPGSA"
MODE_RECOMMENDED_MINIMUM_DATA = "GPRMC"
MODE_VECTOR_TRACK_SPEED_OVER_GROUND = "GPVTG"
MODE_DETAILED_SATELLITE_DATA = "GPGSV"

class SerialReader:
	def __init__(self):
		self.serial = Serial(
			port = '/dev/ttyAMA0',
			baudrate = 9600,
			parity = PARITY_NONE,
			stopbits = STOPBITS_ONE,
			bytesize = EIGHTBITS,
			timeout = 1
		)

	def read(self, mode):
		value = None
		while None == value:
			line = self.serial.readline()
			if mode in line:
				value = line
		return value
