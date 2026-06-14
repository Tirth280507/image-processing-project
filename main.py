import cv2
from image_processor import *

img = cv2.imread("images/My_photo.jpg", 1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)


tl, tr, bl, br = split_image(img)
gray = grayscale(img)
bright = adjust_brightness(img, 50)
contrast = adjust_contrast(img, 1.5)
inverted = invert(img)
blurred = blur(img)
sharpened = sharpen(img)
edges = edge_detection(img)


cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Bright", bright)
cv2.imshow("Contrast", contrast)
cv2.imshow("Inverted", inverted)
cv2.imshow("Blurred", blurred)
cv2.imshow("Sharpened", sharpened)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()