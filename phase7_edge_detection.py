import cv2
import numpy as np

img = cv2.imread("images/My_photo.jpg", 1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

edges = cv2.magnitude(sobel_x, sobel_y)

edges = np.uint8(np.clip(edges, 0, 255))


cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()