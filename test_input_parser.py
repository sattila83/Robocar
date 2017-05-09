#!/usr/bin/env python

import mock
import math

import input_parser

TEST_FILE = "testpath/testfile"
TEST_LAT_1 = 47.47280197178266
TEST_LON_1 = 19.06173124909401
TEST_LAT_2 = 47.47157893570410
TEST_LON_2 = 19.061355739831924
TEST_FILE_CONTENT = "  %s,  \t  %s  \n\t  %s\t  ,%s\t " % (TEST_LAT_1, TEST_LON_1, TEST_LAT_2, TEST_LON_2)

class TestInputParser:

	@mock.patch('__builtin__.open')
	def test_parse(self, openMock):
		# given
		contentMock = openMock.return_value
		contentMock.__enter__ = lambda s: s
		contentMock.__exit__ = mock.Mock()
		contentMock.read.return_value = TEST_FILE_CONTENT
			
		# when
		result = input_parser.InputParser.parse(TEST_FILE)
		
		# then
		openMock.assert_called_once_with(TEST_FILE, 'r')
		assert 1 == contentMock.read.call_count
		assert 2 == len(result)
		assert round(TEST_LAT_1, 10) == round(math.degrees(result[0].lat), 10)
		assert round(TEST_LON_1, 10) == round(math.degrees(result[0].lon), 10)
		assert round(TEST_LAT_2, 10) == round(math.degrees(result[1].lat), 10)
		assert round(TEST_LON_2, 10) == round(math.degrees(result[1].lon), 10)
