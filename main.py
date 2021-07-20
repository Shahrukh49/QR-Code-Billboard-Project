import cv2
import numpy as np
import re
import glob, os
import sys

cap = cv2.VideoCapture(0)
#vid1 = cv2.imread('video1.jpg', 1)
detector = cv2.QRCodeDetector()

cv2.namedWindow("QRSCANNER", 0)
cv2.setWindowProperty("QRSCANNER", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
print(cv2.__version__)
while True:
    for file in glob.glob("*.jpg"):
        print(file)
        picture = cv2.imread(file)

        cv2.imshow("QRSCANNER",picture)

        #pic.append(picture)
        
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        
        if bbox is not None:
            for i in range(len(bbox)):
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                            0, 0), thickness=2)
                
            cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)

            #cv2.imshow("QRSCANNER", img)

            if data:
                print("Data found: " + data)
                ## omxplayer here
                #cv2.imshow("QRSCANNER", vid1)
                #k = cv2.waitKey(4000)
                data = data.replace(" ","")
                os.system("omxplayer "+data+".mp4")
                counter = 0

        #counter = counter - 1
        #print(counter)

        k = cv2.waitKey(2000)
        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()
