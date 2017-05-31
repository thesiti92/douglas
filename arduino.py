import serial
import sys
import datetime

def capture():

	# Saves data to new file (not sure if we need this)
	filename = "arduinoData.log"
	text_file = open(filename, "a")

	ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 0)

	while True:
		data = ser.readline()
		if data:
			sys.stdout.write(data.split()[0])

			text_file.write(data)
			
	text_file.close()



