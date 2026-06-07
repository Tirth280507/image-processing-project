import numpy as np
import cv2

img =  cv2.imread("images/My_photo.jpg")
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

print("original shape : ", img.shape)
print(img.dtype)

gray_manual = (

    0.299 * img[:,:,2] +
    0.587 * img[:,:,1] +
    0.114 * img[:,:,0]
)

gray_manual = gray_manual.astype(np.uint8)

grey_cv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", img)
cv2.imshow("Manual Gray", gray_manual)
cv2.imshow("Opencv Grey", grey_cv)


cv2.waitKey(0)
cv2.destroyWindow()
