import serial
import sys
import datetime


# Saves data to new file (not sure if we need this)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 0)

while True:
	print ser.readline()
