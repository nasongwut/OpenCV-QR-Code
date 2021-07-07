import cv2 
import numpy as np
import time
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

org = (00, 185)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
color = (0, 255, 255)
thickness = 1

while True:
    sucess, img = cap.read()

    for barcode in decode(img):
        # print(barcode.data)
        qrData = barcode.data.decode('utf-8')
        print(qrData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)

        pts2 = barcode.rect
        # cv2.putText(img,qrData,)

        cv2.putText(img, qrData, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, fontScale, 
            color, thickness, cv2.LINE_AA, False)

    cv2.imshow('QR Detector', img)
    cv2.waitKey(1)