#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from object import Object
from segmentation import Segmentation


# TODO: Terminar
#include "Object.h"

# initial min and max HSV filter values.
# these will be changed using trackbars
HUE_TRACKBAR_MAX_VALUE = 179
SATURATION_TRACKBAR_MAX_VALUE = 255
VALUE_TRACKBAR_MAX_VALUE = 255

# Segmenta as canetas
# H_MIN = 0
# H_MAX = 211
# S_MIN = 156
# S_MAX = 255
# V_MIN = 88
# V_MAX = 186

COLOR = 0
H_MIN = 0
H_MAX = 179
S_MIN = 0
S_MAX = 255
V_MIN = 0
V_MAX = 255

# default capture width and height
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
# max number of objects to be detected in frame
MAX_NUM_OBJECTS=25
# minimum and maximum object area
MIN_OBJECT_AREA = 20*20
MAX_OBJECT_AREA = FRAME_HEIGHT*FRAME_WIDTH/1.5
# names that will appear at the top of each window
windowName = "Original Image"
windowName1 = "HSV Image"
windowName2 = "Filtered Thresholded Image"
windowName3 = "After Morphological Operations"
windowName4 = "Equalized"
trackbarWindowName = "Trackbars"
trackbarWindowName2 = "Trackbars2"

# TODO: Terminar
# //The following for canny edge detec
# Mat dst, detected_edges
# Mat src, src_gray
# int edgeThresh = 1
# int lowThreshold
# int const max_lowThreshold = 100
# int ratio = 3
# int kernel_size = 3
# const char* window_name = "Edge Map"

def calib(numRobots):
    listObjs = []
    for i in range(0, numRobots):
        listObjs.append(Segmentation())

    return listObjs

numRobots = int(input("Digite numero de cores a serem calibradas:"))
listSegmObjs = calib(numRobots)

def on_trackbar_colors(value):
    # print(value)
    # print(listSegmObjs[value].H_MIN)
    # print(listSegmObjs[value].H_MAX)
    # print(listSegmObjs[value].S_MIN)
    # print(listSegmObjs[value].S_MAX)
    # print(listSegmObjs[value].V_MIN)
    # print(listSegmObjs[value].V_MAX)

    cv2.setTrackbarPos("H_MIN", trackbarWindowName2, listSegmObjs[value].H_MIN)
    cv2.setTrackbarPos("H_MAX", trackbarWindowName2, listSegmObjs[value].H_MAX)
    cv2.setTrackbarPos("S_MIN", trackbarWindowName2, listSegmObjs[value].S_MIN)
    cv2.setTrackbarPos("S_MAX", trackbarWindowName2, listSegmObjs[value].S_MAX)
    cv2.setTrackbarPos("V_MIN", trackbarWindowName2, listSegmObjs[value].V_MIN)
    cv2.setTrackbarPos("V_MAX", trackbarWindowName2, listSegmObjs[value].V_MAX)


def on_trackbar(value):
    #This function gets called whenever a
    # # trackbar position is changed
    pass

def createTrackbars():
    # create window for trackbars

    cv2.namedWindow(trackbarWindowName, 0)
    cv2.createTrackbar( "H_MIN", trackbarWindowName, H_MIN, HUE_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "H_MAX", trackbarWindowName, H_MAX, HUE_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "S_MIN", trackbarWindowName, S_MIN, SATURATION_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "S_MAX", trackbarWindowName, S_MAX, SATURATION_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "V_MIN", trackbarWindowName, V_MIN, VALUE_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "V_MAX", trackbarWindowName, V_MAX, VALUE_TRACKBAR_MAX_VALUE, on_trackbar )

def createTrackbars2(numColors):
    # create window for trackbars
    cv2.namedWindow(trackbarWindowName2, 0)
    cv2.createTrackbar( "Color", trackbarWindowName2, COLOR, numColors-1 , on_trackbar_colors )
    cv2.createTrackbar( "H_MIN", trackbarWindowName2, H_MIN, HUE_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "H_MAX", trackbarWindowName2, H_MAX, HUE_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "S_MIN", trackbarWindowName2, S_MIN, SATURATION_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "S_MAX", trackbarWindowName2, S_MAX, SATURATION_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "V_MIN", trackbarWindowName2, V_MIN, VALUE_TRACKBAR_MAX_VALUE, on_trackbar )
    cv2.createTrackbar( "V_MAX", trackbarWindowName2, V_MAX, VALUE_TRACKBAR_MAX_VALUE, on_trackbar )

def drawObject(theObjects, frame):
    for i in range(0, len(theObjects)):
        cv2.circle(frame,(theObjects[i].getXPos(),theObjects[i].getYPos()),10,(0,0,255))
        cv2.putText(frame,str(theObjects[i].getXPos())+ " , " + str(theObjects[i].getYPos()),(theObjects[i].getXPos(),theObjects[i].getYPos()+20),1,1,(0,255,0))
        cv2.putText(frame,str(theObjects[i].getType()),(theObjects[i].getXPos(),theObjects[i].getYPos()-30),1,2,theObjects[i].getColor())

    return frame

def morphOps(thresh):
    # create structuring element that will be used to "dilate" and "erode" image.
    # the element chosen here is a 3px by 3px rectangle

    erodeElement = np.ones((3,3),np.uint8)
    # dilate with larger element so make sure object is nicely visible
    dilateElement = np.ones((8,8),np.uint8)

    thresh = cv2.erode(thresh,erodeElement)
    thresh = cv2.erode(thresh,erodeElement)

    thresh = cv2.dilate(thresh,dilateElement)
    thresh = cv2.dilate(thresh,dilateElement)

    return thresh

def trackFilteredObject(threshold, cameraFeed):
    objects = []
    temp = threshold.copy()
    # these two vectors needed for output of findContours
    # find contours of filtered image using openCV findContours function
    _, contours, hierarchy = cv2.findContours(temp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Debug
    # print(contours)
    # print(hierarchy) 

    # use moments method to find our filtered object
    refArea = 0
    objectFound = False
    
    # print(hierarchy)
    # print(len(hierarchy.shape))
    numObjects = len(hierarchy.shape) if hierarchy is not None else 0

    # print(numObjects)
    if(numObjects > 0):        
        # if number of objects greater than MAX_NUM_OBJECTS we have a noisy filter
        if(numObjects<MAX_NUM_OBJECTS):
            index = 0
            while(index>=0):
                moment = cv2.moments(contours[index])
                area = moment['m00']

                # print(moment)
                # print(area)
                
                # if the area is less than 20 px by 20px then it is probably just noise
                # if the area is the same as the 3/2 of the image size, probably just a bad filter
                # we only want the object with the largest area so we safe a reference area each
                # iteration and compare it to the area in the next iteration.
                if(area>MIN_OBJECT_AREA and area<MAX_OBJECT_AREA and area>refArea):                     
                    object = Object()
                    object.setXPos(moment['m10']/area)
                    object.setYPos(moment['m01']/area)

                    objects.append(object)
                    objectFound = True

                else:
                    objectFound = False

                # print(x,y)

                # print(hierarchy)
                # print(hierarchy.shape)
                # print(type(hierarchy))
                # input()

                index = hierarchy[0][index][0]

            if(objectFound == True):
                cv2.putText(cameraFeed,"Object Detected",(0,50),2,1,(0,255,0),2)
                #  Draw Object Location on Screen
                # cameraFeed = drawObject(x,y,cameraFeed)
                cameraFeed = drawObject(objects, cameraFeed)
        else:
           cv2.putText(cameraFeed,"TOO MUCH NOISE! ADJUST FILTER",(0,50),1,2,(0,0,255),2)

    return cameraFeed

def equalizeIntensity(inputImage):
    if(len(inputImage.shape) >= 3):
        ycrcb = cv2.cvtColor(inputImage,cv2.COLOR_BGR2YCrCb)
        channels = cv2.split(ycrcb)
        cv2.equalizeHist(channels[0], channels[0])
        cv2.merge(channels,ycrcb)
        result = cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR)

        return result

    return inputImage

def main():
    # Some boolean variables for different functionality within this program
    trackObjects = True
    useMorphOps = True

    # Create slider bars for HSV filtering
    createTrackbars()
    createTrackbars2(numRobots)


    # Video capture object to acquire webcam feed capture object at location zero (default location for webcam)
    capture = cv2.VideoCapture(0)

    # Set height and width of capture frame
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

    # Start an infinite loop where webcam feed is copied to cameraFeed matrix all of our operations will be performed within this loop
    while(1):
        # Store image to matrix
        ret, cameraFeed = capture.read()

        # for i in range(0, numRobots):
        # Get current positions of four trackbars
        # cv2.setTrackbarPos()

        # H_MIN = cv2.getTrackbarPos("H_MIN", trackbarWindowName)
        # H_MAX = cv2.getTrackbarPos("H_MAX", trackbarWindowName)
        # S_MIN = cv2.getTrackbarPos("S_MIN", trackbarWindowName)
        # S_MAX = cv2.getTrackbarPos("S_MAX", trackbarWindowName)
        # V_MIN = cv2.getTrackbarPos("V_MIN", trackbarWindowName)
        # V_MAX = cv2.getTrackbarPos("V_MAX", trackbarWindowName)

        color = cv2.getTrackbarPos("Color", trackbarWindowName2)
        listSegmObjs[color].H_MIN = cv2.getTrackbarPos("H_MIN", trackbarWindowName2)
        listSegmObjs[color].H_MAX = cv2.getTrackbarPos("H_MAX", trackbarWindowName2)
        listSegmObjs[color].S_MIN = cv2.getTrackbarPos("S_MIN", trackbarWindowName2)
        listSegmObjs[color].S_MAX = cv2.getTrackbarPos("S_MAX", trackbarWindowName2)
        listSegmObjs[color].V_MIN = cv2.getTrackbarPos("V_MIN", trackbarWindowName2)
        listSegmObjs[color].V_MAX = cv2.getTrackbarPos("V_MAX", trackbarWindowName2)

        # Apply Histogram Equalization
        # equalizeHist(cameraFeed,cameraEq)
        cameraEq = equalizeIntensity(cameraFeed)

        # convert frame from BGR to HSV colorspace
        HSV = cv2.cvtColor(cameraFeed,cv2.COLOR_BGR2HSV)

        # filter HSV image between values and store filtered image to threshold matrix
        threshold = []
        for i in range(0,numRobots):
            threshold.append(cv2.inRange(HSV,np.array([listSegmObjs[i].H_MIN,listSegmObjs[i].S_MIN,listSegmObjs[i].V_MIN]),np.array([listSegmObjs[i].H_MAX,listSegmObjs[i].S_MAX,listSegmObjs[i].V_MAX])))

            cv2.imshow("Unfiltered thresholded Image %d" % (i+1),threshold[i])

            # perform morphological operations on thresholded image to eliminate noise
            # and emphasize the filtered object(s)
            if(useMorphOps):
                threshold[i] = morphOps(threshold[i])

            cv2.imshow("Filtered Thresholded Image %d" % (i+1), threshold[i])

            # Pass in thresholded frame to our object tracking function this function will return the x and y coordinates
            # of the filtered object
            if(trackObjects):
                cameraFeed = trackFilteredObject(threshold[i], cameraFeed)


        # Show frames
        cv2.imshow(windowName,cameraFeed)
        cv2.imshow(windowName1,HSV)
        cv2.imshow(windowName4,cameraEq)

        #  Delay 30ms so that screen can refresh.
        # Image will not appear without this waitKey() command
        # Press 'ESC' to exit
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
           break

        # k = cv2.waitKey(5) & 0xFF
        # if k == 99:
        #     cv2.destroyWindow(trackbarWindowName)


    capture.release()
    cv2.destroyAllWindows()

# Main
main()
