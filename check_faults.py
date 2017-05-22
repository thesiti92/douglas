import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    time.sleep(1)
    if GPIO.input(24):
        print("Fault is HIGH")
    else:
        print("Fault is LOW")
