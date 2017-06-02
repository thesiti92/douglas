from steppertest import Stepper

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