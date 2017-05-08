#!/usr/bin/env python

import mock

import serial_reader

SERIAL_TEST_INPUT = [
	"$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47",
	"$GPGSA,A,3,04,05,,09,12,,,24,,,,,2.5,1.3,2.1*39",
	"$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A",
	"$GPVTG,054.7,T,034.4,M,005.5,N,010.2,K*48",
	"$GPGSV,2,1,08,01,40,083,46,02,17,308,41,12,07,344,39,14,22,228,45*75"]

class TestSerialReader:

	@mock.patch('serial_reader.Serial', autospec=True)
	def test_init(self, serialMock):
		# when
		reader = serial_reader.SerialReader()
		
		#then
		serialMock.assert_has_calls([mock.call(
			port = '/dev/ttyAMA0',
			baudrate = 9600,
			parity = serial_reader.PARITY_NONE,
			stopbits = serial_reader.STOPBITS_ONE,
			bytesize = serial_reader.EIGHTBITS,
			timeout = 1
		)])

	@mock.patch('serial_reader.Serial', autospec=True)
	def test_read(self, serialMock):
		# given
		reader = serial_reader.SerialReader()
		reader.serial.readline.side_effect = SERIAL_TEST_INPUT
		
		# when
		result = reader.read(serial_reader.MODE_RECOMMENDED_MINIMUM_DATA)
		
		# then
		assert SERIAL_TEST_INPUT[2] == result
