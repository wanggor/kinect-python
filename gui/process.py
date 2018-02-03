#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:51:09 2018

@author: fotoniks
"""
from kinect_ta import KinectTA
import cv2

class display:
    def __init__(self):
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi',self.fourcc, 20.0, (640,480))
        
        pass
    def layar_1(signal):
        
        if signal[3]%2 is not 0:
            img1 = KinectTA.get_video()
        else :
            img1 = KinectTA.get_infra()
        return img1
    
    def layar_2(signal):
        if signal[5]%2 is not 0:
            img2 = KinectTA.get_depthGray()
        elif signal[6]%2 is not 0:
            img2 = KinectTA.get_depthJET()
        else:
            img2 = KinectTA.depth_thres()
        return img2
    
    def merge (gambar,img1, img2):
        gambar[10:490,10:650] = img1[:,:]
        gambar[10:490,660:1300] = img2[:,:]
        return gambar
    

    
           
            
        
        