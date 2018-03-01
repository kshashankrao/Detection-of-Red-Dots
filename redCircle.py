import cv2
import numpy as np

img = cv2.imread("DDD.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(img, lower_red, upper_red)
#cv2.imshow("Mask0",mask0)

lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img, lower_red, upper_red)
#cv2.imshow("Mask1",mask1)

mask = mask0+mask1
#cv2.imshow("Mask1",mask)

_,cnts,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#print(cnts)

# area1 and area2 are the range of contour area, change accordingly
area1 = 100
area2 = 2000000
totalDots = []

# Count the total number of contours
for cnt in cnts:
    if area1 < cv2.contourArea(cnt) < area2:
        totalDots.append(cnt)

text = "Total number of dots are: {}".format(len(totalDots))
cv2.putText(mask, text, (50, 20),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 255, 255), 2) 
cv2.imshow("Mask",mask)
print("Total number of dots are:{}".format(len(totalDots)))
