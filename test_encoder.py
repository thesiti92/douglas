
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
		self.direction = 1
	def start(self):
		try:
			self.thread.start()
		except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
			pass
	def getAngle(self):
		return self.deg_per_cycle*self.globalCounter
	def rotaryDeal(self):
		if self.globalCounter==1668:
			self.direction = -1
		elif self.globalCounter==-1668:
			self.direction = 1
		self.globalCounter+=(1*self.direction)
		# time.sleep(.5)
	def clear(self,ev=None):
		self.globalCounter=0
		time.sleep(1)

	def loop(self):
		while True:
			self.rotaryDeal()

def testTurn(encoder, error=5, degrees=90):
    current_degrees = encoder.getAngle()
    print "Turning!"
    while(abs(degrees-abs(current_degrees-encoder.getAngle()))>error):
        current_degrees=encoder.getAngle()
    print "done!"
