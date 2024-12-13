# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 16:24:23 2024

@author: Yusuf Furkan Umutlu
"""
import cv2

cap= cv2.VideoCapture(0)

yüzBul=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,frame =cap.read()
    
    if ret:
        fbul=yüzBul.detectMultiScale(frame,minNeighbors=3)
        
        for (x,y,w,h) in fbul:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),10)
        cv2.imshow("yüz tanıma",frame)
        
    if cv2.waitKey(1)& 0xFF==ord("q"): break
cap.release()
cv2.destroyAllWindows()