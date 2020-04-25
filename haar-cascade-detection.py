import cv2
import numpy as np

def nothing():
    pass

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cv2.namedWindow("frame")
cv2.createTrackbar("Scale","frame",11, 20, nothing)
cv2.createTrackbar("Neighbors","frame",0, 20, nothing)

while True:
    _,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #scale,minimum neighbors
    scale = cv2.getTrackbarPos("Scale","frame")
    neighbors = cv2.getTrackbarPos("Neighbors","frame")

    faces = face_cascade.detectMultiScale(gray,scale/10.0,neighbors)
    print(faces)
    for face in faces:
        (x,y,w,h) = face
        frame = cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,255),2)
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
