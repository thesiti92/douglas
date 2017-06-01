import serial
import sys
import datetime

def captureData():

	# Saves data to new file (not sure if we need this)
	ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 0)

	while True:
		data = ser.readline()
		if data:
			sys.stdout.write(data.split())
			encoder = data.split()[0]
			speed = data.split()[1]
			return encoder, speed




