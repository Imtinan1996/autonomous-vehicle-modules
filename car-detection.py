import numpy as np
import cv2
import time

def carDetection(videoName):
    video=cv2.VideoCapture(videoName)
    car_cascade=cv2.CascadeClassifier('car-cascade.xml')
    while True:
        prev_time=time.time()
        bool,frame=video.read()
        if bool is False:
            cv2.destroyAllWindows()
            video.release()
            break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            video.release()
            break
        grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        pedestrians=car_cascade.detectMultiScale(grayFrame,1.3,1)
        for (x,y,w,h) in pedestrians:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.imshow('driving-video',frame)
        print("frame took",time.time()-prev_time)

carDetection('sample-videos/driving-segment-1.mp4')