from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

mh = Adafruit_MotorHAT()
throttle = mh.getStepper(200, 1)  # 200 steps/rev, port (1 or 2)
throttle.setSpeed(40)  # 40 RPM
steps = 30

throttle.step(throttle.step(self, steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE))