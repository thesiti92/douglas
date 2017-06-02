# Mateen Tabatabaei

import time
from time import sleep
import RPi.GPIO as GPIO
import arduino, steppertest

accStep = Stepper(1)
brakeStep = Stepper(2)

# Number of steps required to keep the throttle cable pulled down (idk if 5 is the right num)
accStepNum = 5

# Num steps required to slow or stop the cart (needs testing for actual num)
slowStepNum = 3
brakeStepNum = 5

# Keeps track of whether the brake pedal is being pulled (0 means not at all)
brakeStepCount = 0
sensor = 12


def stop():
    print('HARD STOP: OBJECT DETECTED IN {0:<3} METERS'.format(dist))
    if brakeStepCount != 0:
        brakeStep.testDouble(brakeStepNum)

        # Takes off brakes and accelerates to 3mph


def cruise():
    print('No object detected. Smooth sailing!')
    data = captureData()
    mph = data[1]
    if brakeStepCount != 0:
        brakeStep.testBackDouble(brakeStepCount)
    if mph < 3:
        accStep.testDouble(accStepNum)  # Need to test direction + accStepNum value


def init_GPIO():  # initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)

def init_interrupt():
    GPIO.add_event_detect(sensor, GPIO.FALLING, callback=calculate_elapse, bouncetime=2)

if __name__ == "__main__":
    init_GPIO()
    init_interrupt()

    while True:
        if (True):
            stop()
        else:
            cruise()
        sleep(0.5)

