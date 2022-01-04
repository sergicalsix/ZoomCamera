import cv2
import time


cap = cv2.VideoCapture(1)

cascade_path = 'haarcascade_frontalface_alt2.xml'
cascade = cv2.CascadeClassifier(cascade_path)
color = (255, 255, 255) #白


while True:
    ret, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
    if len(facerect) > 0:
        #検出した顔を囲む矩形の作成
        for rect in facerect:
            cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=4)
    cv2.imshow('myface',image)

    cv2.waitKey(1) 
    time.sleep(0.05)
    cv2.destroyAllWindows()

