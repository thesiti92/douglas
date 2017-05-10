from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

class steering_motor:
    def __init__(self, controller, pwm):
        self.MC = controller
        pwm = in1 = in2 = 0
        if (pin < 0) or (pin > 15):
            raise NameError('PWM pin must be between 0 and 15 inclusive')
        self.PWMpin = pwm

    def setSpeed(self, speed):
        if (speed < 0):
            speed = 0
        if (speed > 255):
            speed = 255
        self.MC._pwm.setPWM(self.PWMpin, 0, speed*16)
