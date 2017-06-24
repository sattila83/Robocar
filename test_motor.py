#!/usr/bin/env python

import mock

from motor import MotorControl

class TestMotorControl:

	@mock.patch('motor.PWMObject', autospec=True)
	def test_dodge(self, pwmObjectMock):
		pwmInstance = None
		with MotorControl() as motor:
			# given
			pwmInstance = pwmObjectMock.return_value
			
			# when
			motor.dodge()
			
			# then
			assert 2 == pwmObjectMock.call_count
			pwmObjectMock.assert_has_calls([mock.call(20), mock.call(21)], any_order=True)
			assert 2 == pwmInstance.toPositive.call_count
			assert 2 == pwmInstance.toNegative.call_count
			
		assert 2 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_moveForward(self, pwmObjectMock):
		with MotorControl() as motor:
			# given
			pwmInstance = pwmObjectMock.return_value
			
			# when
			motor.moveForward()
			
			# then
			pwmObjectMock.assert_has_calls([mock.call(20), mock.call(21)], any_order=True)
			assert 1 == pwmInstance.toPositive.call_count
			assert 0 == pwmInstance.toNegative.call_count

		assert 2 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_moveBackward(self, pwmObjectMock):
		with MotorControl() as motor:
			# given
			pwmInstance = pwmObjectMock.return_value
			
			# when
			motor.moveBackward()
			
			# then
			pwmObjectMock.assert_has_calls([mock.call(20), mock.call(21)], any_order=True)
			assert 0 == pwmInstance.toPositive.call_count
			assert 1 == pwmInstance.toNegative.call_count

		assert 2 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_turnLeft(self, pwmObjectMock):
		with MotorControl() as motor:
			# given
			pwmInstance = pwmObjectMock.return_value
			
			# when
			motor.turnLeft()
			
			# then
			pwmObjectMock.assert_has_calls([mock.call(20), mock.call(21)], any_order=True)
			assert 1 == pwmInstance.toPositive.call_count
			assert 0 == pwmInstance.toNegative.call_count
			
		assert 2 == pwmInstance.cleanup.call_count

	@mock.patch('motor.PWMObject', autospec=True)
	def test_turnRight(self, pwmObjectMock):
		with MotorControl() as motor:
			# given
			pwmInstance = pwmObjectMock.return_value
			
			# when
			motor.turnRight()
			
			# then
			pwmObjectMock.assert_has_calls([mock.call(20), mock.call(21)], any_order=True)
			assert 0 == pwmInstance.toPositive.call_count
			assert 1 == pwmInstance.toNegative.call_count
		
		assert 2 == pwmInstance.cleanup.call_count
