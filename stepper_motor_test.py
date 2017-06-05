from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
#mh = Adafruit_MotorHAT()

#throttle = mh.getStepper(200, 1)  # 200 steps/rev, port (1 or 2)
#throttle.setSpeed(40)  # 30 RPM

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


def setRpm(rpm):
    throttle.setSpeed(rpm)  # 30 RPM

def testRotate(self):
    print("Single coil steps")
    throttle.step(200, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
    throttle.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

def testSingle(self, steps):
    throttle.step(self, steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

def setRpm(rpm):
    throttle.setSpeed(rpm)

def testBackSingle(self, steps):
    throttle.step(self, steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

def testBackDouble(self, steps):
    throttle.step(self, steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

def testDouble(self, steps):
    throttle.step(self, steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

# Loop to test the brake and acceleration stepper motors with a manual control

# motor = stepper
#steps = 30
#direct = raw_input("f or b?")
#steps = int(raw_input("How many steps? "))
#if direct == f:
#    throttle.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
#if direct == b:
#    throttle.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
# steps = raw_input("How many steps backwards? ")
#throttle.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
