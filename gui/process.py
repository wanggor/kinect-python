#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#
"""
Created on Wed Jan 31 22:51:09 2018

@author: fotoniks
"""
from kinect_ta import KinectTA
import cv2
import numpy as np

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
        matriks = np.zeros((480,50,3),'uint8')
        matriks[:,:,2]=100
        matriks[:,22:27,2]=255     
        img1[:,295:345] = 0.2*img1[:,295:345]+ 0.8 * matriks[:,:]
        

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
    
    def obj_track(RGB, bw):
        depth = KinectTA.get_depthGray16bit()
        matriks = np.ones((480,640),'uint16')
        lem = cv2.cvtColor(bw,cv2.COLOR_BGR2GRAY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(15,1))

        lem = cv2.morphologyEx(lem,cv2.MORPH_OPEN,kernel)
       
        image,contour,_ = cv2.findContours(lem.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        
        posisi =[]
        # And draw it on the original image
        for c in contour:
            # enter your filtering here
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(RGB,(x,y),(x+w,y+h),(0,255,0),2)
            x=x+int(w/2)
            y=y+int(h/2)
            cv2.circle(RGB,(x,y), 5, (0,0,255), -1)
            
            img = cv2.drawContours(matriks, contour, 0, 1, -1)
            depth = depth*img
            
            
            
            maksimal = np.max(depth)
            minimal = np.min(depth)
            volume = np.sum(depth)
            area = cv2.contourArea(c)
            
#            cv2.putText(RGB,str(area),x,y), font, 0.5,(50,50,50),1,cv2.LINE_AA)
            
            #menambahkan posisi serta area tiap objeck
            posisi.append([x,y,area,volume,maksimal,minimal])
        
        return RGB,bw,posisi
    
#    def ukuran (posisi)
    

    
           
            
        
        
