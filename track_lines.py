from numpy import array, average, pi, where
from math import degrees
from serial import Serial
from cv2 import threshold, cvtColor, resize, COLOR_BGR2GRAY, THRESH_BINARY, THRESH_OTSU, Canny, HoughLines, bilateralFilter
from picamera import PiCamera
from picamera.array import PiRGBArray
from steering import turn, kill
from RPi.GPIO import IN, setmode, setup, BCM, add_event_detect, BOTH, input
from breaking import brake
import threading
ser = Serial('/dev/ttyACM0', 115200)
camera = PiCamera()
stream = PiRGBArray(camera)
brake_pin = 12
half=pi/2
braking = False
mph=0

setmode(BCM)
setup(brake_pin, IN)

mh = Adafruit.MotorHAT()
throttle = mh.getStepper(200, 1)  # 200 steps/rev, port (1 or 2)
throttle.setSpeed(40)  # 40 RPM
steps = 30
#Cruise Control: pulses throttle while speed <2 mph
thr = threading.Thread(target = cruise)

def cruise():
    throttle.step(self, steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

def brake(channel):
    if input(brake_pin):
        print "braking"
        braking = True
    else:
        print "going"
        braking = False
add_event_detect(brake_pin, BOTH, callback=brake, bouncetime=1000)
 # this callback is just to reset the steering. we shouldnt reset the cruise control because we'd need to reset the demos
for foo in camera.capture_continuous(stream, format='bgr', resize=(640,480), use_video_port=True):
    #TODO: check mph and if off by a bit accelerate/decelerate

    #TODO: write clean acceleration and breaking methods to import from another file. maybe have varying degrees of acceleration or breaking.

    #to read in mph: need try except because arduino sometimes gives null values

    try:
        if ser.readline().split()[1] < 2 & braking == False:
            thr.start()
    except:
        pass

    if braking:
        brake()
        kill()
        print "we braked"
        #TODO: disengage accelerator motor
        continue
    ret3,frame = threshold(bilateralFilter(cvtColor(stream.array, COLOR_BGR2GRAY),12,70,70),0,255,THRESH_BINARY+THRESH_OTSU)
    edges = Canny(frame,1000,1000, 5)
    lines = HoughLines(edges,1,pi/180,100)
    if lines is None:
        kill()
        stream.truncate()
        stream.seek(0)
        continue
    thetas=array([theta for rho, theta in lines[0]])
    theta_filtered=thetas[where((thetas>=0) & (thetas <=pi))]

    #use list of thetas to figure out degrees to turn
    if (average(theta_filtered) < half):
        radians_to_turn = half - average(thetas)
        turn(degrees(radians_to_turn), dir=False)
    else:
        radians_to_turn = average(thetas) - half
        turn(degrees(radians_to_turn), dir=True)
    stream.truncate()
    stream.seek(0)
