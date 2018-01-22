# -*- coding: utf-8 -*-

import freenect
import cv2
import numpy as np

class KinectTA():
    def __init__(self, parent=None):
        pass
        
    #function to get RGB image from kinect
    def get_video(self):
        array,_ = freenect.sync_get_video()
        #array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
        return array
     
    #function to get depth image from kinect
    def get_depth(self):
        array,_ = freenect.sync_get_depth()
        array = array.astype(np.uint8)
        array = cv2.applyColorMap(array, cv2.COLORMAP_JET)
        return array
    #function to get infrared camera 
    def get_infra(self):
        array,_ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
        array = array.astype(np.uint8)
        array = cv2.cvtColor(array,cv2.COLOR_GRAY2BGR)
        return array
    
    # looping to get image RGB
    def image_loop(self):
        rgb=self.get_video()
        return rgb
        
    def image_stop(self):
        freenect.sync_stop()
