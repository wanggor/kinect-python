# -*- coding: utf-8 -*-

import freenect
import cv2
import numpy as np

class KinectTA():
    def __init__():
        pass
        
    #function to get RGB image from kinect
    def get_video():
        array,_ = freenect.sync_get_video()
        array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
        return array
    
    #function to get depth image from kinect (JET)
    def get_depthJET():
        depth,_ = freenect.sync_get_depth()
        array = depth.astype(np.uint8)
        array = cv2.applyColorMap(array, cv2.COLORMAP_JET)
        array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        return array,depth
    
    #function to get infrared camera 
    
    def get_depthGray():
        depth,_ = freenect.sync_get_depth()
        array = depth.astype(np.uint8)
        array = cv2.cvtColor(array, cv2.COLOR_GRAY2RGB)
        return array,depth
    
        
    def depth_thres():
        depth,_ = freenect.sync_get_depth()
        array = depth.astype(np.uint8)
        th,array=cv2.threshold(array,0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
#        kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#        array = cv2.morphologyEx(array,cv2.MORPH_OPEN,kernel)
#        array = cv2.morphologyEx(array,cv2.MORPH_CLOSE,kernel2)

        array = cv2.cvtColor(array, cv2.COLOR_GRAY2RGB)
        return array,depth
        
    # looping to get image RGB
    def get_infra():
        array,_ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
        array = array.astype(np.uint8)
        array = cv2.cvtColor(array,cv2.COLOR_GRAY2RGB)
        return array

     
    def image_stop():
        freenect.sync_stop()
