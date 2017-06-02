import numpy as np
import cv2

img = cv2.imread('road.jpg', 0)

blur = cv2.bilateralFilter(img,12,70,70)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

edges = cv2.Canny(th3,1000,1000, 5)
cv2.imshow('Original',img)

lines = cv2.HoughLines(edges,1,np.pi/180,100)
color = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(color,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('Trajectory',color)

cv2.waitKey(0)

cv2.destroyAllWindows()
