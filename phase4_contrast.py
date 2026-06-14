import numpy as np
import cv2


img =  cv2.imread("images/My_photo.jpg")
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

contrat_factor = 1.5

contrast = img.astype(np.float32) * contrat_factor

contrat = np.clip(contrast, 0, 255)

contrast = contrast.astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("High Contrast", contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()
