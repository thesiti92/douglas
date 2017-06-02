from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


class Stepper(portNum):
    def __init__(self):
        atexit.register(turnOffMotors)
        degrees_per_step = 1.8

        self = mh.getStepper(200, portNum)  # 200 steps/rev, port (1 or 2)
        self.setSpeed(40)  # 30 RPM

    def setRpm(rpm):
        self.setSpeed(rpm)  # 30 RPM

    def testRotate(self):
        print("Single coil steps")
        self.step(200, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
        self.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

    def testSingle(steps):
        self.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

    def setRpm(rpm):
        self.setSpeed(rpm)

    def testBackSingle(steps):
        self.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

    def testBackDouble(steps):
        self.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

    def testDouble(steps):
        self.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

step[0] = Stepper(1)
step[1] = Stepper(2)

#Loop to test the brake and acceleration stepper motors with a manual control
while True:

    motorChoice = raw_input("Which motor? (0 = acc, 1 = brake)")
    motor = step[motorChoice]

    steps = raw_input("How many steps forward? ")
    motor.testDouble(steps)

    steps = raw_input("How many steps backwards? ")
    motor.testBackDouble(steps)