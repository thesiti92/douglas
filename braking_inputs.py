import time
from time import sleep
# Import the ADS1x15 module.
import Adafruit_ADS1x15

import RPi.GPIO as GPIO
import time, math

from threading import Thread

class Radar:
	def __init__(self):
		# Create an ADS1115 ADC (16-bit) instance.
		self.adc = Adafruit_ADS1x15.ADS1115()
		self.GAIN = 2
		self.distance = 0
		self.converg_factor = 0.156254768517
		self.thread = Thread(target=self.loop)
		print ('*****    Radar class instantiated! Variables: GAIN = %s, distance = %s, converg factor = %s *****' % self.GAIN, self.distance, self.converg_factor)

	def start(self):
		try:
			self.thread.start()
			print ("Radar thread started.")
		except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
			destroy()

	def get_distance():
		self.adc_num = adc.read_adc(0,self.GAIN)
	   	self.distance = self.adc_num*self.converg_factor/1000
	   	self.distance += 1
	
	def print_distance(): 	
	   	print('Distance is: {0:<6} meters'.format(distance))
	   	print("")

	def loop():
		while True:
			self.get_distance()


class HallSensor:
	def __init__(self):
		self.start_timer = time.time()
		self.radius = 13 #cm
		self.dist_meas = 0.00
		self.km_per_hour = 0
		self.m_per_sec = 0 		#meters per second
		self.mph = 0			#miles per hour
		self.rpm = 0
		self.elapse = 0
		self.sensor = 12
		self.pulse = 0
		init_GPIO()
		init_interrupt()
		self.thread = Thread(target=self.loop)
		print ('$$$$$$	  HallEffect class initiated. Variables: radius, dist_meas,  $$$$$$')
		print ('$$$$$$	  km_per_hour, mph, rpm, elapse, sensor, pulse        $$$$$$')

	def start(self):
		try:
			self.thread.start()
			print ("HallEffect thread started.")
		except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
			destroy()

	def init_GPIO():               # initialize GPIO
 		GPIO.setmode(GPIO.BCM)
   		GPIO.setwarnings(False)
   		GPIO.setup(sensor,GPIO.IN,GPIO.PUD_UP)
   	
   	def init_interrupt():
   		GPIO.add_event_detect(sensor, GPIO.FALLING, callback = calculate_elapse, bouncetime = 20)

   	def calculate_elapse(channel): #ALEX why does this take a paramater called "channel"?
   		self.pulse += 1
   		self.elapse = time.time() - self.start_timer 
   		self.start_timer = time.time()
   		
	def get_speed():
	   if self.elapse !=0:                     # to avoid DivisionByZero error
	      self.rpm = 1/self.elapse * 60
	      self.circ_cm = (2*math.pi)*self.radius        # calculate wheel circumference in CM
	      self.dist_km = self.circ_cm/100000          # convert cm to km
	      self.km_per_sec = self.dist_km / self.elapse      # calculate KM/sec
	      self.m_per_sec = self.km_per_sec * 1000
	      self.km_per_hour = self.km_per_sec * 3600      # calculate KM/h
	      self.mph = self.km_per_hour * 0.62
	      self.dist_meas = (self.dist_km*self.pulse)*1000   # measure distance traverse in meter
	      return self.m_per_sec
		

	def loop():
		while True
			self.get_speed()




