import serial
import sys
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
	data = ser.readline()
	if data:
		sys.stdout.write(data)
