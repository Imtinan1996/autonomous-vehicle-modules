import numpy as np
import cv2
import pyautogui
import matplotlib.pyplot as plt

#area_to_remove=np.array([[100,474],[100,375],[300,200],[520,200],[800,375],[800,475]]) # for driving segment 
area_to_remove=np.array([[250,650],[450,500],[850,500],[1050,650]]) # for youtube video


def draw_lanes(image,lanes):
    try:
        for line in lanes:
            coordinates=line
            if coordinates != []:
                cv2.line(image,(coordinates[0],coordinates[1]),(coordinates[2],coordinates[3]),[0,255,0],10)
    except:
        pass
    return image

def mask_area(image):
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,[area_to_remove],255)
    masked_img=cv2.bitwise_and(image,mask)
    return masked_img

def blur_image(image):
    return cv2.GaussianBlur(image,(5,5),0)
    
def edge_convert(image):
    processed_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    processed_img=cv2.Canny(processed_img,threshold1=300,threshold2=400)
    return processed_img

def detect_lines(image):
    image=blur_image(image)
    detected_lines=cv2.HoughLinesP(image,1,np.pi/180,180,np.array([]),100,100)
    gradients=[]
    try:
        for line in detected_lines:
            coordinates=line[0]
            cv2.line(image,(coordinates[0],coordinates[1]),(coordinates[2],coordinates[3]),[255,255,255],3)
            gradients.append(((coordinates[3]-coordinates[1])/(coordinates[2]-coordinates[0])))
    except:
        pass
    return image,detected_lines,gradients

    
def findLanes(videoName):
    video=cv2.VideoCapture(videoName)

    line1=[]
    line2=[]
    while True:
        bool,frame=video.read()
        if bool is False:
            cv2.destroyAllWindows()
            video.release()
            break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            video.release()
            break
        cv2.imshow('driving-video',frame)
        edges=edge_convert(frame)
        cv2.imshow('canny-edges',edges)
        roi=mask_area(frame)
        cv2.imshow('removed unwanted area',roi)
        roi_edges=mask_area(edges)
        cv2.imshow('roi edges',roi_edges)
        lines,lanes,gradients=detect_lines(roi_edges)
        cv2.imshow('lines edges',lines)
        for i in range(len(gradients)):
            if gradients[i]>0.5: #LINE 2
                #print("right line found with coordinates",lanes[i][0],"and gradients",gradients[i])
                line2=lanes[i][0]
            elif gradients[i]<-0.5: #line 1
                #print("left line found with coordinates",lanes[i][0],"and gradients",gradients[i])
                line1=lanes[i][0]
        frame_with_lanes=draw_lanes(frame,[line1,line2])
        cv2.imshow('the lanes',frame_with_lanes)
        #print("gradients",gradients)

findLanes('sample-videos/test-from-youtube.mp4')
