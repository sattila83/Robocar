#!/usr/bin/env python

import math
import mock

import positioning_service

TEST_SERIAL_DATA = [
	"$GPGGA,123519,4730.500,N,01859.600,E,1,08,0.9,545.4,M,46.9,M,,*47",
	"$GPGGA,123519,4730.600,N,01900.600,E,1,08,0.9,545.4,M,46.9,M,,*47",
	"$GPGGA,123519,4730.700,N,01901.600,E,1,08,0.9,545.4,M,46.9,M,,*47"]

class TestPositioningService:

	@mock.patch('positioning_service.SerialReader', autospec=True)
	def test_getActualPosition(self, serialMock):
		# given
		readerMock = positioning_service.SerialReader.return_value
		readerMock.read.side_effect = TEST_SERIAL_DATA
		
		# when
		position = positioning_service.PositioningService.getActualPosition(numberOfSamples = 3, samplingTimeInSeconds = 0.0)
		
		# then
		assert 1 == serialMock.call_count
		readerMock.read.assert_called_with(positioning_service.MODE_GPS_FIX_DATA)
		assert 47.51 == round(math.degrees(position.lat), 6)
		assert 19.01 == round(math.degrees(position.lon), 6)
