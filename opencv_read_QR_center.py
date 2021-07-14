import cv2 
import numpy as np
import time
from pyzbar.pyzbar import decode

res_x = 1024
res_y = 768
res_center = (int(res_x/2),int(res_y/2))

cap = cv2.VideoCapture(0)
cap.set(3,res_x)
cap.set(4,res_y)

#acuracy pixcel
acuracy = 20



while True:
    sucess, img = cap.read()

    for barcode in decode(img):
        # print(barcode.data)
        qrData = barcode.data.decode('utf-8')

        # print(qrData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,0,255),2)
        

        countPoint = 0
        for x in pts:
            listptsNew= x
            point = x[0]
            newpoint = (point[0],point[1])
            cv2.putText(img, str(countPoint), newpoint, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
                (0, 0, 255), 1, cv2.LINE_AA, False)
            countPoint+=1          

        pts2 = barcode.rect
        # cv2.line(img,(pts2),(0,0,255),1)
        print('----------------------')
        # print(pts2)

        QRcenter = (
            int(pts2[0]+pts2[2]/2),
            int(pts2[1]+pts2[3]/2)
            ) 
        print('QR Center : '+str(QRcenter)+'')
        print('Camera Center :' + str(res_center)+'')
        print('Acuracy : '+ str(acuracy)+'')
        # print(res_center)
        # print(type(res_center))
# 
        if QRcenter[0] <= res_center[0]+acuracy and QRcenter[1] <= res_center[1]+acuracy:
            if QRcenter[0] >= res_center[0]-acuracy and QRcenter[1] >= res_center[1]-acuracy:
                cv2.circle(img,QRcenter,2,(0,255,0),10)
                print('Center is : True')
            # else:

        else:
            cv2.circle(img,QRcenter,2,(0,0,255),5)
            print('Center is : False') 
        print('----------------------')


        cv2.putText(img, qrData, (int(pts2[0]),pts2[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
            (0, 0, 255), 1, cv2.LINE_AA, False)
        cv2.putText(img, 'Location', (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
            (0, 0, 255), 1, cv2.LINE_AA, False)

        # print(res_center)

    cv2.line(img,(int(res_x/2),0),(int(res_x/2),res_y),(0,0,255),1)
    cv2.line(img,(0,int(res_y/2)),(res_x,int(res_y/2)),(0,0,255),1)
    cv2.circle(img,res_center,acuracy,(0,0,255),2)

    cv2.imshow('QR Detector', img)
    # time.sleep()
    cv2.waitKey(1)