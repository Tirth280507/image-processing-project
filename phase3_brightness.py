import numpy as np
import cv2

img =  cv2.imread("images/My_photo.jpg")
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

bright = img.astype(np.int16) + 50

bright = np.clip(bright, 0, 255)

bright = bright.astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("Bright", bright)

cv2.waitKey(0)
cv2.destroyAllWindows()

