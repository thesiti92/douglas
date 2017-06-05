from Adafruit_MotorHAT import Adafruit_MotorHAT

mh = Adafruit_MotorHAT()
throttle = mh.getStepper(200, 1)
throttle.setSpeed(40)
steps = int(raw_input("How many Steps"))
dir = raw_input("What direction? f/b")
if dir == "f":
    throttle.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
if dir == "b":
    throttle.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
