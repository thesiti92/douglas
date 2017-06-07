from Adafruit_MotorHAT import Adafruit_MotorHAT
from RPi.GPIO import setmode, output, setup, OUT, BCM
from serial import Serial
from time import time
setmode(BCM)
ser = Serial('/dev/ttyACM0', 115200)


class steering_motor:
    def __init__(self, controller, pwm_pin, sleep_pin, dir_pin):
        self.MC = controller
        if (pwm_pin < 0) or (pwm_pin > 15):
            raise NameError('PWM pin must be between 0 and 15 inclusive')

        self.pwm_pin = pwm_pin
        self.sleep_pin = sleep_pin
        setup(sleep_pin, OUT)
        self.dir_pin = dir_pin
        setup(dir_pin, OUT)

    def turn(self, degrees, dir=True, speed=200, error=1):
        try:
            start_degrees = float(ser.readline().split()[0])
            start_time = time()
            if dir:
                #True is right, false is left
                output(self.dir_pin, 1)
            else:
                output(self.dir_pin, 0)
            self.setSpeed(speed)
            while(abs(degrees-abs(abs(start_degrees)-abs(float(ser.readline().split()[0]))))>error):
                if time()-start_time>1:
                    self.setSpeed(0)
                    return
        except:
            turn(degrees, dir, speed, error)
        self.setSpeed(0)

    def setSpeed(self, speed):
        if (speed < 0):
            speed = 0
        if (speed > 255):
            speed = 255
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed*16)


mh = Adafruit_MotorHAT()
motor = steering_motor(mh, 15, 0, 22)

def turn(degrees, dir=True, speed=100, error=2):
    motor.turn(degrees, dir, speed, error)
def kill():
    motor.setSpeed(0)
