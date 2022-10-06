import numpy as np
import cv2 as cv
img = np.zeros((512,512,3), np.uint8)
img2 = np.zeros((512,512,3), np.uint8)
cv.line(img,(200,200),(300,50),(75,45,74),8)
cv.line(img,(400,200),(300,50),(75,45,74),8)
cv.line(img,(0,400),(512,400),(0,255,0),8)
cv.rectangle(img,(200,200),(400,400),(14,145,255),8)
cv.rectangle(img,(300,300),(250,250),(255,255,255),5)
font = cv.FONT_HERSHEY_SIMPLEX
cv.imshow("original", img)
cv.waitKey()