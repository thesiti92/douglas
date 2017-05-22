from RPi import GPIO
from time import sleep

pin_24 = 24
pin_25 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin_25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(pin_24)

try:
    while True:
        state_24 = GPIO.input(pin_24)
        state_25 = GPIO.input(pin_25)
        # if clkState != clkLastState:
        #     if dtState != clkState:
        #         counter += 1
        #     else:
        #         counter -= 1
        #         print counter
        # clkLastState = clkState
        print(state_24, ", ", state_25)
        sleep(0.01)
finally:
    GPIO.cleanup()
