import cv2

img = cv2.imread("lena.png")
cv2.imshow('img',img)
cv2.waitKey(0)