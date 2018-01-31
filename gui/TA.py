#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 10:11:59 2018

@author: fotoniks
"""
import freenect
import cv2
import numpy as np
import threading
import time


#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
#function to get depth image from kinect
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    array = cv2.cvtColor(array,cv2.COLOR_GRAY2BGR)
    cv2.imshow('RGB image',array)
    return array
#function to get infrared camera 
def get_infra():
    array,_ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    array = array.astype(np.uint8)
    array = cv2.cvtColor(array,cv2.COLOR_GRAY2BGR)
    cv2.imshow('infra',array)
    return array


if __name__ == "__main__":
    
    
    freenect.init()
    t_2 = 0
    while 1:
        
        #get a frame from RGB camera
        t_1 = time.time()
        print("waktu yang dibutuhkan :", t_1-t_2)
        t_2 = time.time()
        t1= threading.Thread(target=get_infra, args=())
        t2= threading.Thread(target=get_depth, args=())
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
#        c=np.concatenate((t1,t2), axis=1)
#        cv2.imshow(' ', c)
        
        

#        #get a frame from depth sensor
#        depth = get                _depth()
#        infra = get_infra()
        #display RGB image
        #rgb=get_video()
    #        a=cv2.applyColorMap(depth, cv2.COLORMAP_JET)
    #        d,b=threshold=cv2.threshold(depth,0, 255, cv2.THRESH_OTSU)
    #        e= cv2.cvtColor(b, cv2.COLOR_GRAY2BGR)

        
      
        #display depth image
        #cv2.imshow('Depth image',depth)
         
#         quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    freenect.sync_stop() 
    
