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
    
    #function to get depth image from kinect
    def get_depthJET():
        array,_ = freenect.sync_get_depth()
        array = array.astype(np.uint8)
        array = cv2.applyColorMap(array, cv2.COLORMAP_JET)
        array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        return array
    #function to get infrared camera 
    
    def get_depthGray():
        array,_ = freenect.sync_get_depth()
        array = array.astype(np.uint8)
        array = cv2.cvtColor(array, cv2.COLOR_GRAY2RGB)
        return array
        
    def depth_thres():
        array,_ = freenect.sync_get_depth()
        array = array.astype(np.uint8)
        th,array=cv2.threshold(array,0, 255, cv2.THRESH_OTSU)
        array = cv2.cvtColor(array, cv2.COLOR_GRAY2RGB)
        return array
        
    # looping to get image RGB
    def get_infra():
        array,_ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
        array = array.astype(np.uint8)
        array = cv2.cvtColor(array,cv2.COLOR_GRAY2RGB)
        return array

     
    def image_stop():
        freenect.sync_stop()
