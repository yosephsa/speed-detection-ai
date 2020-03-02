import numpy as np
import cv2 as cv

def opticalFlowDenseA(prvs, next):
    prvs = cv.cvtColor(prvs,cv.COLOR_BGR2GRAY)
    hsv = np.zeros_like(next)
    hsv[...,1] = 255
    ret, frame2 = cap.read()
    next = cv.cvtColor(next,cv.COLOR_BGR2GRAY)

    #obtain dense optical flow
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 2, 5, 1.2, 0)

    # convert from cartesian to polar
    mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])

    #hue corresponds to direction
    hsv[...,0] = ang*180/np.pi/2

    #value corresponds to magnitude
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)

    #convert hsv to bgr
    bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)

    return bgr

def opticalFlowDenseB(image_current, image_next):
    """
    input: image_current, image_next (RGB images)
    calculates optical flow magnitude and angle and places it into HSV image
    * Set the saturation to the saturation value of image_next
    * Set the hue to the angles returned from computing the flow params
    * set the value to the magnitude returned from computing the flow params
    * Convert from HSV to RGB and return RGB image with same size as original image
    """
    
   
    
    gray_current = cv.cvtColor(image_current, cv.COLOR_RGB2GRAY)
    gray_next = cv.cvtColor(image_next, cv.COLOR_RGB2GRAY)
    
    
    hsv = np.zeros((480, 640, 3))
    # set saturation
    hsv[:,:,1] = cv.cvtColor(image_next, cv.COLOR_RGB2HSV)[:,:,1]
 
    # Flow Parameters
    # flow_mat = cv2.CV_32FC2
    flow_mat = None
    image_scale = 0.5
    nb_images = 1
    win_size = 15
    nb_iterations = 2
    deg_expansion = 5
    STD = 1.3
    extra = 0
    # obtain dense optical flow paramters
    flow = cv.calcOpticalFlowFarneback(gray_current, gray_next,  
                                        flow_mat, 
                                        image_scale, 
                                        nb_images, 
                                        win_size, 
                                        nb_iterations, 
                                        deg_expansion, 
                                        STD, 
                                        0)
                                        
        
    # convert from cartesian to polar
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])  
        
    # hue corresponds to direction
    hsv[:,:,0] = ang * (180/ np.pi / 2)
    
    # value corresponds to magnitude
    hsv[:,:,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    
    # convert HSV to int32's
    hsv = np.asarray(hsv, dtype= np.float32)
    rgb_flow = cv.cvtColor(hsv,cv.COLOR_HSV2RGB)
    return rgb_flow

cap = cv.VideoCapture(cv.samples.findFile("data_raw/test.mp4"))

while(1):
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    rgb_flow = opticalFlowDenseB(frame1, frame2)

    cv.imshow("frame2", rgb_flow)
    cv.imshow("frame1", frame2)
    k = cv.waitKey(30) & 0xff

