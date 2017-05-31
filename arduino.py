import serial

ser = serial.Serial('/dev/ttyACM1', 115200)
while True:
	print str(ser.readline())
