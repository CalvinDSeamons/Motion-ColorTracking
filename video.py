import numpy as np
import cv2
import argparse
import time
from threading import Thread 
#imports used for the lab2 are numpy and opencv
#Authors: Calvin Seamons, and someone... maybe :(   .
#Robot Vision Assignment 2
#Febuary 7 2019


###########################################################################

global image1,image2, video, blank_image, redMax, greenMax, blueMax, redMin, blueMin, greenMin




def __main__():
    print("Welcome to Part 1 of Lab2 Computer Vision\nWritten by Calvin Seamons")
    #data = input("Select a value for the video/image display: \n\t1) Normal BGR Video \n\t2) HSV Video \n\t3) Gray Scale Video \n\t4) Color Tracker\n")
    data ="4"
    captureVid(data)




####################################################################################################
def captureVid(data):
    global video, blank_image, image1, image2, greenMax, redMax,blueMax,redMin,greenMin,blueMin
    video = cv2.VideoCapture(0)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    img = np.zeros((300,512,3), np.uint8)
    blank_image = np.zeros((height,width,3), np.uint8)
    cv2.namedWindow('image1')
    cv2.namedWindow('color_tracker')
    cv2.createTrackbar('H Max','color_tracker',0,255,nothing)
    cv2.createTrackbar('S Max','color_tracker',0,255,nothing)
    cv2.createTrackbar('V Max','color_tracker',0,255,nothing)
    cv2.createTrackbar('H Min','color_tracker',0,255,nothing)
    cv2.createTrackbar('S Min','color_tracker',0,255,nothing)
    cv2.createTrackbar('V Min','color_tracker',0,255,nothing)

    cv2.setTrackbarPos('H Max','color_tracker',255)
    cv2.setTrackbarPos('S Max','color_tracker',255)
    cv2.setTrackbarPos('V Max','color_tracker',255)

    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image',0,1,nothing)
    kernel = np.ones((5,5), np.uint8) 
    
    while(True):
        ret,image1 = video.read()
        cv2.setMouseCallback('image1',getMouseData)
        #below is the standard BGR image

        #mask = cv2.inRange(hsv,low_bound,up_bound)

        #colorChange()
        if data == str(1):
            cv2.imshow('image1', image1)

        if data == str(2):
            hsv = cv2.cvtColor(image1,cv2.COLOR_BGR2HSV)
            cv2.imshow('image1',hsv)

        if data == str(3):
            gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            cv2.imshow('image1',gray)

        if data == str(4):
            hsv = cv2.cvtColor(image1,cv2.COLOR_BGR2HSV)
            erosion = cv2.erode(hsv,kernel,iterations=1)
            dilation = cv2.dilate(erosion,kernel,iterations=1)
            redMax = cv2.getTrackbarPos('H Max','color_tracker')
            greenMax = cv2.getTrackbarPos('S Max','color_tracker')
            blueMax = cv2.getTrackbarPos('V Max','color_tracker')
            redMin = cv2.getTrackbarPos('H Min','color_tracker')
            greenMin = cv2.getTrackbarPos('S Min','color_tracker')
            blueMin = cv2.getTrackbarPos('V Min','color_tracker')

            s = cv2.getTrackbarPos(switch,'color_tracker')
            
            #if s == 0:
            #    img[:] = 0
            #else:
            #    img[:] = [b,g,r]

            minArray = np.array([redMin,greenMin,blueMin])
            maxArray = np.array([redMax,greenMax,blueMax])
            frame_threshold = cv2.inRange(hsv, (minArray),(maxArray))
            cv2.imshow('image1',dilation)
            cv2.imshow('color_tracker',frame_threshold)




        #break condition...
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()

def getMouseData(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print( "Row:"+str(y) + ", Col: " + str(x)+ ",  HSV Values: [" + str(image1[y][x][2]) +", "
               + str(image1[y][x][1]) +", "+ str(image1[y][x][0]) + "]")
        #setThreshold(image1[y][x][2],image1[y][x][1],image1[y][x][0])
                

def setThreshold(red,green,blue):
    global redMax,blueMax,greenMax,redMin,greenMin,blueMin, int, str
    redMax = red+50
    blueMax =blue+50
    greenMax = green+50
    redMin = red-50
    greenMin = green-50
    blueMin = blue-50
    cv2.namedWindow('color_tracker')

    cv2.createTrackbar('H Max','color_tracker',0,255,nothing)
    cv2.createTrackbar('S Max','color_tracker',0,255,nothing)
    cv2.createTrackbar('V Max','color_tracker',0,255,nothing)
    cv2.createTrackbar('H Min','color_tracker',0,255,nothing)
    cv2.createTrackbar('S Min','color_tracker',0,255,nothing)
    cv2.createTrackbar('V Min','color_tracker',0,255,nothing)


    cv2.setTrackbarPos('H Max','color_tracker',redMax)
    cv2.setTrackbarPos('S Max','color_tracker',greenMax)
    cv2.setTrackbarPos('V Max','color_tracker',int(blueMax))
    cv2.setTrackbarPos('H Min','color_tracker',int(redMin))
    cv2.setTrackbarPos('S Min','color_tracker',int(greenMin))
    cv2.setTrackbarPos('V Min','color_tracker',int(blueMin))
    


def nothing(x):
    pass














__main__()

