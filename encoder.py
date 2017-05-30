
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from threading import Thread


class Encoder:
	def __init__(self, RoAPin = 24, RoBPin=25):
		GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
		GPIO.setup(RoAPin, GPIO.IN)    # input mode
		GPIO.setup(RoBPin, GPIO.IN)
		self.RoAPin = RoAPin
		self.RoBPin = RoBPin
		self.AState = False
		self.BState = False
		self.globalCounter = 0
		self.flag = 0
		self.Last_RoB_Status = 0
		self.Current_RoB_Status = 0
		self.deg_per_cycle = 0.215827338
	def start(self):
		try:
			self.thread.start()
		except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
			destroy()
	def getAngle(self):
		return self.deg_per_cycle*self.globalCounter
	def rotaryDeal(self):
		self.Last_RoB_Status = GPIO.input(self.RoBPin)
		while(not GPIO.input(self.RoAPin)):
			self.Current_RoB_Status = GPIO.input(self.RoBPin)
			self.flag = 1
		if self.flag == 1:
			self.flag = 0
			if (self.Last_RoB_Status == 0) and (self.Current_RoB_Status == 1):
				self.globalCounter = self.globalCounter + 1
				# print 'globalCounter = %d' % self.globalCounter
			if (self.Last_RoB_Status == 1) and (self.Current_RoB_Status == 0):
				self.globalCounter = self.globalCounter - 1
				# print 'globalCounter = %d' % self.globalCounter

	def clear(self,ev=None):
	        self.globalCounter = 0
		# print 'globalCounter = %d' % self.globalCounter
		time.sleep(1)

	def loop(self):
		while True:
			self.rotaryDeal()
	#		print 'globalCounter = %d' % globalCounter
	def watch(self):
		while True:
			print self.getAngle()
			time.sleep(.5)
	def destroy(self):
		GPIO.cleanup()             # Release resource
