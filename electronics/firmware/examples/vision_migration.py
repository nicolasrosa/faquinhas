import cv2
import numpy as np

# initial min and max HSV filter values.
# these will be changed using trackbars
H_MIN = 0
H_MAX = 71
S_MIN = 76
S_MAX = 238
V_MIN = 98
V_MAX = 220
# default capture width and height
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
# max number of objects to be detected in frame
MAX_NUM_OBJECTS=50
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

def on_trackbar(value):
    #This function gets called whenever a
    # trackbar position is changed
    pass


def createTrackbars():
    # create window for trackbars

    cv2.namedWindow(trackbarWindowName, 0)
    # create memory to store trackbar name on window
    # create trackbars and insert them into window
    # 3 parameters are: the address of the variable that is changing when the trackbar is moved(eg.H_LOW),
    # the max value the trackbar can move (eg. H_HIGH),
    # and the function that is called whenever the trackbar is moved(eg. on_trackbar)
    #                                   ---->    ---->     ---->
    cv2.createTrackbar( "H_MIN", trackbarWindowName, H_MIN, H_MAX, on_trackbar )
    cv2.createTrackbar( "H_MAX", trackbarWindowName, H_MAX, H_MAX, on_trackbar )
    cv2.createTrackbar( "S_MIN", trackbarWindowName, S_MIN, S_MAX, on_trackbar )
    cv2.createTrackbar( "S_MAX", trackbarWindowName, S_MAX, S_MAX, on_trackbar )
    cv2.createTrackbar( "V_MIN", trackbarWindowName, V_MIN, V_MAX, on_trackbar )
    cv2.createTrackbar( "V_MAX", trackbarWindowName, V_MAX, V_MAX, on_trackbar )

def drawObject(x, y, frame):
    # use some of the openCV drawing functions to draw crosshairs
    # on your tracked image!

    # UPDATE:JUNE 18TH, 2013
    # added 'if' and 'else' statements to prevent
    # memory errors from writing off the screen (ie. (-25,-25) is not within the window!)

    x = int(x)
    y = int(y)

    cv2.circle(frame,(x,y),20,(0,255,0),2)
    if(y-25>0):
        cv2.line(frame,(x,y),(x,y-25),(0,255,0),2)
    else:
        cv2.line(frame,(x,y),(x,0),(0,255,0),2)
    if(y+25<FRAME_HEIGHT):
        cv2.line(frame,(x,y),(x,y+25),(0,255,0),2)
    else:
        cv2.line(frame,(x,y),(x,FRAME_HEIGHT),(0,255,0),2)
    if(x-25>0):
        cv2.line(frame,(x,y),(x-25,y),(0,255,0),2)
    else:
        cv2.line(frame,(x,y),(0,y),(0,255,0),2)
    if(x+25<FRAME_WIDTH):
        cv2.line(frame,(x,y),(x+25,y),(0,255,0),2)
    else:
        cv2.line(frame,(x,y),(FRAME_WIDTH,y),(0,255,0),2)

    cv2.putText(frame,str(x)+","+str(y),(x,y+30),1,1,(0,255,0),2)

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

def trackFilteredObject(x, y, threshold, cameraFeed):
    temp = threshold.copy()
    # these two vectors needed for output of findContours
    # find contours of filtered image using openCV findContours function
    im2, contours, hierarchy = cv2.findContours(temp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Debug
    # print(im2)
    # print(contours)
    # print(hierarchy) 

    # use moments method to find our filtered object
    refArea = 0
    objectFound = False
    
    print(hierarchy)
    print(len(hierarchy.shape))
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
                    # input("Press")
                    x = moment['m10']/area
                    y = moment['m01']/area
                    objectFound = True
                    refArea = area
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
                cameraFeed = drawObject(x,y,cameraFeed)
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

    # x and y values for the location of the object
    x=0; y=0

    # create slider bars for HSV filtering
    createTrackbars()

    # video capture object to acquire webcam feed
    # capture object at location zero (default location for webcam)
    capture = cv2.VideoCapture(0)
    # set height and width of capture frame

    capture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)
    # start an infinite loop where webcam feed is copied to cameraFeed matrix
    # all of our operations will be performed within this loop
    while(1):
        # store image to matrix
        ret, cameraFeed = capture.read()

        # get current positions of four trackbars
        H_MIN = cv2.getTrackbarPos("H_MIN", trackbarWindowName)
        H_MAX = cv2.getTrackbarPos("H_MAX", trackbarWindowName)
        S_MIN = cv2.getTrackbarPos("S_MIN", trackbarWindowName)
        S_MAX = cv2.getTrackbarPos("S_MAX", trackbarWindowName)
        V_MIN = cv2.getTrackbarPos("V_MIN", trackbarWindowName)
        V_MAX = cv2.getTrackbarPos("V_MAX", trackbarWindowName)

        # Apply Histogram Equalization
        # equalizeHist(cameraFeed,cameraEq)
        cameraEq = equalizeIntensity(cameraFeed)

        # convert frame from BGR to HSV colorspace
        HSV = cv2.cvtColor(cameraFeed,cv2.COLOR_BGR2HSV)

        # filter HSV image between values and store filtered image to threshold matrix
        threshold = cv2.inRange(HSV,np.array([H_MIN,S_MIN,V_MIN]),np.array([H_MAX,S_MAX,V_MAX]))

        cv2.imshow("Unfiltered thresholded Image",threshold)
        # perform morphological operations on thresholded image to eliminate noise
        # and emphasize the filtered object(s)
        if(useMorphOps):
            threshold = morphOps(threshold)

        # Pass in thresholded frame to our object tracking function this function will return the x and y coordinates
        # of the filtered object
        if(trackObjects):
            cameraFeed = trackFilteredObject(x,y,threshold, cameraFeed)

        # Show frames
        cv2.imshow(windowName,cameraFeed)
        cv2.imshow(windowName1,HSV)
        cv2.imshow(windowName2,threshold)
        cv2.imshow(windowName4,cameraEq)

        #  Delay 30ms so that screen can refresh.
        # Image will not appear without this waitKey() command
        # Press 'ESC' to exit
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
           break

    capture.release()
    cv2.destroyAllWindows()

# Main
main()