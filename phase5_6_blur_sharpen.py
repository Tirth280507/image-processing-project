import cv2
import numpy as np


img = cv2.imread("images/My_photo.jpg", 1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)


# for blur 
blurred = cv2.blur(img, (5, 5))

#for Sharpen 
kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

sharpened = cv2.filter2D(img, -1, kernel)


cv2.imshow("Original", img)
cv2.imshow("Blurred", blurred)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()