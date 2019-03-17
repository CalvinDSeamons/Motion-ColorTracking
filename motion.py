import cv2
import numpy as np
import time 
###################################################
#Written by Calvin Seamons 
#No Partner 
#Lab 2 part 2 (motion)
#Feb 11 2019                                    
##################################################


def captureVid():
    video  = cv2.VideoCapture(0)
    width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    ret,image1=video.read()
    frame1 = np.float32(image1)
    frame2 = np.float32(image1)
    blank_image = None;
    

    while(True):
        ret,image1 = video.read()
        cv2.namedWindow('image1')
        #here i get the accum Weight of frames 1 and 2
        cv2.accumulateWeighted(image1,frame1, 0.1)
        cv2.accumulateWeighted(image1,frame2,0.1)
        #frames converst to absolute scale for image1
        result1 = cv2.convertScaleAbs(frame1)
        result2 = cv2.convertScaleAbs(frame2)

        diff_frame = cv2.absdiff(image1,result1)
       
        diff_frame = cv2.cvtColor(diff_frame,cv2.COLOR_BGR2GRAY)

        ret, threshold1 = cv2.threshold(diff_frame,10,255,cv2.THRESH_BINARY)

        diff_frame = cv2.GaussianBlur(threshold1,(9,9),0)

        ret, threshold2 = cv2.threshold(diff_frame,200,255,cv2.THRESH_BINARY)

        if blank_image is None:
            blank_image = diff_frame
            continue

        #diff_frame = cv2.absdiff(blank_image,gray)
        #threshold = cv2.threshold(diff_frame,150,255,cv2.THRESH_BINARY)[1]
        
    
        
        contours,hierachy=cv2.findContours(threshold2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
        for ct in contours:
            if cv2.contourArea(ct) < 2000:
                continue
            (x,y,w,h) = cv2.boundingRect(ct)
            cv2.rectangle(image1,(x,y),(x+w,y+h), (150,255,0), 3)

        cv2.imshow('image1',image1)
        #cv2.imshow('poop',result2)
        #cv2.imshow('blank_image',blank_image)
        cv2.imshow('diff_frame', diff_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


captureVid()
