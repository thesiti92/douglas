#Mateen Tabatabaei

import time
from time import sleep
from braking_inputs import HallEffect, Radar


if __name__ == "__main__":
	radar = Radar()
	hallSensor = HallSensor()

	while True:
		print ("Radar Converg Factor is %s and distance is %s" % radar.converg_factor, radar.distance)
		print ("Hall Effect Sensor pulse is %s and mph is %s" % hallSensor.pulse, hallSensor.mph)
		sleep(1)