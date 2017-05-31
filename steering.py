from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time
import RPi.GPIO as GPIO
import serial
GPIO.setmode(GPIO.BCM)
ser = serial.Serial('/dev/ttyACM0', 115200)


class steering_motor:
    def __init__(self, controller, pwm_pin, sleep_pin, dir_pin):
        self.MC = controller
        if (pwm_pin < 0) or (pwm_pin > 15):
            raise NameError('PWM pin must be between 0 and 15 inclusive')

        self.pwm_pin = pwm_pin
        self.sleep_pin = sleep_pin
        GPIO.setup(sleep_pin, GPIO.OUT)
        self.dir_pin = dir_pin
        GPIO.setup(dir_pin, GPIO.OUT)

    def turn(self, degrees, dir="r", speed=100, error=1):
        start_degrees = ser.readline()
        if dir=="r":
            GPIO.output(self.dir_pin, 1)
        elif dir=="l":
            GPIO.output(self.dir_pin, 0)
        self.setSpeed(speed)
        print "Turning!"

        while(abs(degrees-abs(abs(start_degrees)-abs(ser.readline())))>error):
            print abs(degrees-abs(abs(start_degrees)-abs(ser.readline())))
            pass
        print "done!"
        self.setSpeed(0)

    def setSpeed(self, speed):
        if (speed < 0):
            speed = 0
        if (speed > 255):
            speed = 255
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed*16)
    def testSpeed(self, speed, delay=1):
        self.setSpeed(speed)
        time.sleep(delay)
        self.setSpeed(0)
    def backAndForth(self, speed, delay=1, times=5):
        self.setSpeed(speed)
        GPIO.output(self.sleep_pin, 1)
        for x in range(times):
            time.sleep(delay)
            GPIO.output(self.dir_pin, x % 2)
        GPIO.output(self.sleep_pin, 0)



mh = Adafruit_MotorHAT()
motor = steering_motor(mh, 15, 0, 22)

def setSpeed(speed):
    motor.setSpeed(speed)
def testSpeed(speed, delay=1):
    motor.testSpeed(speed,delay)
def backAndForth(speed, delay=1, times=5):
    motor.backAndForth(speed, delay, times)
def kill():
    motor.setSpeed(0)
if __name__ == "__main__":
    motor.setSpeed(10)
