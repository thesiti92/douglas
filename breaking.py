from Adafruit_MotorHAT import Adafruit_MotorHAT
#from RPi.GPIO import setmode, output, setup, OUT, BCM
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

    def pull_brake(self, speed=100, time_on=1):
        output(self.dir_pin, 0) #decides whether brakiing or unbraking
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        sleep(time_on)
        self.MC._pwm.setPWM(self.pwm_pin, 0, 0)

    def release_brake(self, speed=100, time_on=1):
        output(self.dir_pin, 1) #decides whether brakiing or unbraking
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        sleep(time_on)
        self.MC._pwm.setPWM(self.pwm_pin, 0, 0)

###ELI HAS THE SPEDS
    # def brake(self, time):
    #     speed=100
    #     time_on=time
    #     output(self.dir_pin, 0) #decides whether brakiing or unbraking
    #     self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
    #     start_time=time()
    #     while true:
    #         if time()-start_time>time_on:
    #             self.MC._pwm.setPWM(self.pwm_pin, 0, 0)
    #             break # could immediately switch directions and go backwards in this while loop...
    #     output(self.dir_pin, 1) #decides whether brakiing or unbraking
    #     self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
    #     start_time=time()
    #     while true:
    #         if time()-start_time>time_on:
    #             self.MC._pwm.setPWM(self.pwm_pin, 0, 0)
    #             break

    def kill(self):
        self.MC._pwm.setPWM(self.pwm_pin, 0, 0)

mh = Adafruit_MotorHAT()
brake_motor = braking_motor(mh, 14, 23) #create break motor. pwm pin 14,
if __name__ == "__main__":
    #testing the motor
    brake_motor.pull_brake()
    brake_motor.release_brake()
