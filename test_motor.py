#!/usr/bin/env python

import mock

import motor

class TestMotorFunctions:

	@mock.patch('motor.PWMObject', autospec=True)
	def test_dodge(self, pwmObjectMock):
		# given
		pwmInstance = pwmObjectMock.return_value
		
		# when
		motor.MotorFunctions.dodge()
		
		# then
		assert 2 == pwmObjectMock.call_count
		pwmObjectMock.assert_has_calls([mock.call(20), mock.call(21)], any_order=True)
		assert 2 == pwmInstance.toPositive.call_count
		assert 2 == pwmInstance.toNegative.call_count
		assert 2 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_moveForward(self, pwmObjectMock):
		# given
		pwmInstance = pwmObjectMock.return_value
		
		# when
		motor.MotorFunctions.moveForward()
		
		# then
		pwmObjectMock.assert_called_with(21)
		assert 1 == pwmInstance.toPositive.call_count
		assert 0 == pwmInstance.toNegative.call_count
		assert 1 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_moveBackward(self, pwmObjectMock):
		# given
		pwmInstance = pwmObjectMock.return_value
		
		# when
		motor.MotorFunctions.moveBackward()
		
		# then
		pwmObjectMock.assert_called_with(21)
		assert 0 == pwmInstance.toPositive.call_count
		assert 1 == pwmInstance.toNegative.call_count
		assert 1 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_turnLeft(self, pwmObjectMock):
		# given
		pwmInstance = pwmObjectMock.return_value
		
		# when
		motor.MotorFunctions.turnLeft()
		
		# then
		pwmObjectMock.assert_called_with(20)
		assert 1 == pwmInstance.toPositive.call_count
		assert 0 == pwmInstance.toNegative.call_count
		assert 1 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_turnRight(self, pwmObjectMock):
		# given
		pwmInstance = pwmObjectMock.return_value
		
		# when
		motor.MotorFunctions.turnRight()
		
		# then
		pwmObjectMock.assert_called_with(20)
		assert 0 == pwmInstance.toPositive.call_count
		assert 1 == pwmInstance.toNegative.call_count
		assert 1 == pwmInstance.cleanup.call_count
