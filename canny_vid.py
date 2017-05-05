import numpy as np
import cv2
import io
import picamera
import picamera.array
camera = picamera.PiCamera()

#cap = cv2.VideoCapture('track.mp4')
stream = picamera.array.PiRGBArray(camera)


for foo in camera.capture_continuous(stream, format='bgr'):
    frame = stream.array
    
#    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    blur = cv2.bilateralFilter(grey,12,70,70)
#    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#    edges = cv2.Canny(th3,1000,1000, 5)
    cv2.imshow('Original',frame)

#    lines = cv2.HoughLines(edges,1,np.pi/180,100)
#    color = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
#    for rho,theta in lines[0]:
#        a = np.cos(theta)
#        b = np.sin(theta)
#        x0 = a*rho
#        y0 = b*rho
#        x1 = int(x0 + 1000*(-b))
#        y1 = int(y0 + 1000*(a))
#        x2 = int(x0 - 1000*(-b))
#        y2 = int(y0 - 1000*(a))
#
#        cv2.line(color,(x1,y1),(x2,y2),(0,0,255),2)
#    cv2.imshow('Trajectory',color)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    stream.truncate()
    stream.seek(0)

cap.release()
cv2.destroyAllWindows()
