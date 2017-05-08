#!/usr/bin/env python

import mock

import pwmobject

class TestPWMObject:
	
	@mock.patch('pwmobject.GPIO', autospec=True)
	def test_init(self, gpioMock):
		# given
		port = 42
		
		# when
		pwmInstance = pwmobject.PWMObject(port)
		
		# then
		assert 42 == pwmInstance.port
		gpioMock.setmode.assert_has_calls([mock.call(gpioMock.BCM)])
		gpioMock.setup.assert_has_calls([mock.call(port, gpioMock.OUT)])
		gpioMock.PWM.assert_has_calls([mock.call(port, 50)])
	
	@mock.patch('pwmobject.GPIO', autospec=True)
	def test_toPositive(self, gpioMock):
		# given
		pwmInstance = pwmobject.PWMObject(0)
		calls = self.mockPositiveCalls()
		
		# when
		pwmInstance.toPositive()
		
		# then
		pwmInstance.pwm.start.assert_has_calls([mock.call(7.5)])
		pwmInstance.pwm.ChangeDutyCycle.assert_has_calls(calls)
		assert 1 == pwmInstance.pwm.stop.call_count

	@mock.patch('pwmobject.GPIO', autospec=True)
	def test_toNegative(self, gpioMock):
		# given
		pwmInstance = pwmobject.PWMObject(0)
		calls = self.mockNegativeCalls()
		
		# when
		pwmInstance.toNegative()
		
		# then
		pwmInstance.pwm.start.assert_has_calls([mock.call(7.5)])
		pwmInstance.pwm.ChangeDutyCycle.assert_has_calls(calls)
		assert 1 == pwmInstance.pwm.stop.call_count

	@mock.patch('pwmobject.GPIO', autospec=True)
	def test_cleanup(self, gpioMock):
		# given
		pwmInstance = pwmobject.PWMObject(0)
		
		# when
		pwmInstance.cleanup()
		
		# then
		assert 1 == gpioMock.cleanup.call_count

	def mockPositiveCalls(self):
		calls = []
		for i in range(75,100):
			calls.append(mock.call(i/10.0))
		for i in range(100,75,-1):
			calls.append(mock.call(i/10.0))
		calls.append(mock.call(7.5))
		return calls

	def mockNegativeCalls(self):
		calls = []
		for i in range(75,50,-1):
			calls.append(mock.call(i/10.0))
		for i in range(50,75):
			calls.append(mock.call(i/10.0))
		calls.append(mock.call(7.5))
		return calls