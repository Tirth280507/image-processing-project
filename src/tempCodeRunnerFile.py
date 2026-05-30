

h,w = img[:2]

top_left = img[:h//2,:w//2]

cv2.imshow("Original", img)
cv2.imshow("Top Left", top_left)


cv2.waitKey(0)
cv2.destroyAllWindows()
