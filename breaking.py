from Adafruit_MotorHAT import Adafruit_MotorHAT
from RPi.GPIO import setmode, output, setup, OUT, BCM
import RPi.GPIO as GPIO
from time import sleep
setmode(BCM)


class braking_motor:
    def __init__(self, controller, pwm_pin, dir_pin):
        self.MC = controller
        if (pwm_pin < 0) or (pwm_pin > 15):
            raise NameError('PWM pin must be between 0 and 15 inclusive')
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin
        GPIO.setwarnings(False)
        setup(dir_pin, OUT)

    def pull_brake(self, speed=1000, time_on=1):

        output(self.dir_pin, 0) #decides whether braking or unbraking
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        sleep(time_on)
        self.MC._pwm.setPWM(self.pwm_pin, 0, 0)

    def release_brake(self, speed=1000, time_on=1):
        output(self.dir_pin, 1) #decides whether brakiing or unbraking
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        sleep(time_on)
        self.MC._pwm.setPWM(self.pwm_pin, 0, 0)

##ELI HAS THE SPEDS
    #  def brake(self, speed=200, time_on=1):
    #      speed = int(raw_input ("Speed?"))
    #      output(self.dir_pin, 0) #decides whether brakiing or unbraking
    #      self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
    #      sleep(time_on)
    #      self.MC._pwm.setPWM(self.pwm_pin, 0, 0)
    #      output(self.dir_pin, 1) #decides whether brakiing or unbraking
    #      self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
    #      sleep(time_on)
    #      self.MC._pwm.setPWM(self.pwm_pin, 0, 0)

    def kill(self):
        self.MC._pwm.setPWM(self.pwm_pin, 0, 0)

mh = Adafruit_MotorHAT()
brake_motor = braking_motor(mh, 14, 19) #create break motor. pwm pin 14,
output(brake_motor.dir_pin, 0)
def brake(speed = 1000, time_on=1):
    brake_motor.pull_brake(speed, time_on)
def unbrake(speed = 1000, time_on=1):
    brake_motor.release_brake(speed, time_on)

if __name__ == "__main__":
    #testing the motor
    brake_motor.pull_brake()
    brake_motor.release_brake()
