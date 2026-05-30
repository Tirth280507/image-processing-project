import cv2
import numpy as np

img = cv2.imread("images/My_photo.jpg", 1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

print("Shape:", img.shape)
print("Dtype:", img.dtype)
h,w = img.shape[:2]

top_left = img[:h//2,:w//2]
top_right = img[:h//2,w//2:]
bottom_left = img[h//2:, :w//2]
bottom_right = img[h//2:, w//2:]

cv2.imshow("Original", img)
cv2.imshow("Top Left", top_left)
cv2.imshow("Top right", top_right)
cv2.imshow("Bottom Left", bottom_left)
cv2.imshow("Bottom Right", bottom_right)


cv2.waitKey(0)
cv2.destroyAllWindows()
