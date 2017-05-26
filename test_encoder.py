
#!/usr/bin/env python
# import RPi.GPIO as GPIO
import time
from threading import Thread


class Encoder:
	def __init__(self, RoAPin = 24, RoBPin=25):

		self.RoAPin = RoAPin
		self.RoBPin = RoBPin
		self.globalCounter = 0
		self.flag = 0
		self.Last_RoB_Status = 0
		self.Current_RoB_Status = 0
		self.thread = Thread(target=self.loop)
		self.deg_per_cycle = 0.215827338
	def start(self):
		try:
			self.thread.start()
		except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
			pass
	def getAngle(self):
		return self.deg_per_cycle*self.globalCounter
	def rotaryDeal(self):
		self.globalCounter+=1
        time.sleep(.5)

	def clear(self,ev=None):
	        self.globalCounter = 0
		# print 'globalCounter = %d' % self.globalCounter
		time.sleep(1)

	def loop(self):
		while True:
			self.rotaryDeal()
	#		print 'globalCounter = %d' % globalCounter
    #
	# def destroy(self):
	# 	GPIO.cleanup()             # Release resource
