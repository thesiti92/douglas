import numpy as np
import math
import cv2
import io
import picamera
import picamera.array
camera = picamera.PiCamera()
stream = picamera.array.PiRGBArray(camera)

theta_list=[]
rho_list=[]
half=np.pi/2
quarter=0.25*np.pi
three_quarter=0.75*np.pi

for foo in camera.capture_continuous(stream, format='bgr'):
    ret3,frame = cv2.threshold(cv2.bilateralFilter(cv2.cvtColor(cv2.resize(stream.array, [500,500]), cv2.COLOR_BGR2GRAY),12,70,70),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    edges = cv2.Canny(frame,1000,1000, 5)
    lines = cv2.HoughLines(edges,1,np.pi/180,100)
    print lines[0]
    
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        theta_list.append(theta)
        rho_list.append(rho)
        
        cv2.line(color,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow('Trajectory',color)

    theta_np=np.array(theta_list)
    rho_np = np.array(rho_list)

    theta_filtered=theta_np[np.where((theta_np>=quarter) & (theta_np <=three_quarter))]
    rho_filtered=rho_np[np.where((rho_np>=quarter) & (rho_np <=three_quarter))]

#use list of thetas to figure out degrees to turn
    print "average theta", np.average(theta_np)
    print "average filtered theta", np.average(theta_filtered)

    if (np.average(theta_filtered) < half):
        radians_to_turn = half - np.average(theta_list)
        print "turn left", math.degrees(radians_to_turn)
    else:
        radians_to_turn = np.average(theta_list) - half
        print "turn right", math.degrees(radians_to_turn)

    stream.truncate()
    stream.seek(0)
