from Adafruit_MotorHAT import Adafruit_MotorHAT
from RPi.GPIO import setmode, output, setup, OUT, BCM
from serial import Serial
from time import time
setmode(BCM)
ser = Serial('/dev/ttyACM0', 115200)


class motor:
    def __init__(self, controller, pwm_pin, dir_pin):
        self.MC = controller
        if (pwm_pin < 0) or (pwm_pin > 15):
            raise NameError('PWM pin must be between 0 and 15 inclusive')
        self.pwm_pin = pwm_pin
        self.sleep_pin = sleep_pin
        setup(sleep_pin, OUT)
        self.dir_pin = dir_pin
        setup(dir_pin, OUT)
    
    def pull_brake():
        speed=100
        time_on=2
        output(self.dir_pin, 0) #decides whether brakiing or unbraking
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        start_time=time()
        while true:
            if time()-start_time>time_on:
                self.MC._pwm.setPWM(self.pwm_pin, 0, 0)
                break
    
    def release_unbrake():
        speed=100
        time_on=2
        output(self.dir_pin, 1) #decides whether brakiing or unbraking
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        start_time=time()
        while true:
            if time()-start_time>time_on:
                self.MC._pwm.setPWM(self.pwm_pin, 0, 0)
                break

    def brake(time)
        speed=100
        time_on=time
        output(self.dir_pin, 0) #decides whether brakiing or unbraking
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        start_time=time()
        while true:
            if time()-start_time>time_on:
                self.MC._pwm.setPWM(self.pwm_pin, 0, 0)
                break # could immediately switch directions and go backwards in this while loop...
    output(self.dir_pin, 1) #decides whether brakiing or unbraking
    self.MC._pwm.setPWM(self.pwm_pin, 0, speed)
        start_time=time()
        while true:
            if time()-start_time>time_on:
                self.MC._pwm.setPWM(self.pwm_pin, 0, 0)
                break


mh = Adafruit_MotorHAT()
brake_motor = motor(mh, 15, 23) #create break motor. pwm pin 14,

def kill():
    motor.setSpeed(0)

#break_motor.brake()
