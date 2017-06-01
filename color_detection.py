import sys
import math

sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
from matplotlib import pyplot as plt

white = (255, 255, 255)
red = (0,0,255)

half=np.pi/2
frame_width=500.0

cap = cv2.VideoCapture('road4.avi')


# define the list of boundaries
boundaries = [
    ([10, 50, 10], [50, 100, 50]),
]

#green
# lower=np.array([10, 50, 10])
# upper=np.array([50, 100, 50])

#gray
lower=np.array([105, 105, 105])
upper=np.array([185, 185, 185])

#white
lower=np.array([240, 240, 240])
upper=np.array([255, 255, 255])

image=cv2.imread("photo.png")

def resize(image, width):
    r = width / image.shape[1]
    dim = (int(width), int(image.shape[0] * r))
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.namedWindow("main", cv2.WINDOW_NORMAL)

    # loop over the boundaries

    #for (lower, upper) in boundaries:

    # create NumPy arrays from the boundaries
    #lower =np.array(lower, dtype="uint8")
    #upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask

    resized = resize(frame, 1000.0)

    #crop
    #resized = resized[0:1000, 220:1000]  # Crop from x, y, w, h -> 100, 200, 300, 400


    mask = cv2.inRange(resized, lower, upper)


    output = cv2.bitwise_and(resized, resized, mask=mask)

    color_image=np.hstack([resized, output])
    # show the images
    cv2.imshow("images", np.hstack([resized, output]))

    gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    threshhold_img = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    tight_bin = cv2.Canny(threshhold_img, 225, 250)

    lines = cv2.HoughLines(tight_bin, 1, np.pi / 180, 100)
    # print lines
    theta_list = []
    rho_list = []
    lowest_y = 1000

    print len(lines[0])
    for rho, theta in lines[0]:
    #for x in range(40):
        #rho,theta=lines[0][x]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        theta_list.append(theta)
        rho_list.append(rho)

        #cv2.rectangle(resized, (int(x0), int(y0)), (int(x0) + 2, int(y0) + 2), (0, 255, 0), 2)
        cv2.line(tight_bin, (x1, y1), (x2, y2), white, 2)

    cv2.imshow('Trajectory', tight_bin)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()