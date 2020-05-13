import cv2
import numpy

cap = cv2.VideoCapture(0)
i = 0
while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)
    
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(str(i)+".png",frame)
        print("Saved " + str(i) + ".png")
        i = i + 1
    elif key == 27:
        break

cam.release()
cv2.destroyAllWindows()
