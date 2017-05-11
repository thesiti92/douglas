from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM
from Adafruit_MotorHAT import Adafruit_MotorHAT

class steering_motor:
    def __init__(self, controller, pin):
        self.MC = controller
        if (pin < 0) or (pin > 15):
            raise NameError('PWM pin must be between 0 and 15 inclusive')
        self.PWMpin = pin

    def setSpeed(self, speed):
        if (speed < 0):
            speed = 0
        if (speed > 255):
            speed = 255
        self.MC._pwm.setPWM(self.PWMpin, 0, speed*16)
mh = Adafruit_MotorHAT()
motor = steering_motor(mh, 15)
def setSpeed(speed):
    motor.setSpeed(speed)
if __name__ == "__main__":
    motor.setSpeed(10)
