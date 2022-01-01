import cv2
cap = cv2.VideoCapture(2)
ret, frame = cap.read()
print(frame)
cv2.imshow('laugh',frame)