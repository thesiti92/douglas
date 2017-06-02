from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

port=int(raw_input("what motor port?"))

myStepper = mh.getStepper(200, port)  # 200 steps/rev, port (1 or 2)
myStepper.setSpeed(40)  # 30 RPM

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


def setRpm(rpm):
    myStepper.setSpeed(rpm)  # 30 RPM

def testRotate(self):
    print("Single coil steps")
    myStepper.step(200, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
    myStepper.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

def testSingle(self, steps):
    myStepper.step(self, steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

def setRpm(rpm):
    myStepper.setSpeed(rpm)

def testBackSingle(self, steps):
    myStepper.step(self, steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

def testBackDouble(self, steps):
    myStepper.step(self, steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

def testDouble(self, steps):
    myStepper.step(self, steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

# Loop to test the brake and acceleration stepper motors with a manual control

# motor = stepper
steps = 30
direct = raw_input("f or b?")
steps = int(raw_input("How many steps? "))
if direct == f:
    myStepper.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
if direct == b:
    myStepper.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
# steps = raw_input("How many steps backwards? ")
#myStepper.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
