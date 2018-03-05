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
        
        if signal[4]%2 is not 0:
            img1 = KinectTA.get_infra()
        else :
            img1 = KinectTA.get_video()
            
        matriks = np.zeros((480,50,3),'uint8')
        matriks[:,:,2]=100
        matriks[:,22:27,2]=255     
        img1[:,295:345] = 0.2*img1[:,295:345]+ 0.8 * matriks[:,:]
        return img1
    
    def layar_2(signal):
        if signal[5]%2 is not 0:
            img2,depth = KinectTA.get_depthGray()
        elif signal[6]%2 is not 0:
            img2,depth = KinectTA.get_depthJET()
        elif signal[7]%2 is not 0:
            img2,depth = KinectTA.depth_thres()
        else:
            img2,depth = KinectTA.get_depthGray()
        return img2,depth
    
    def merge (gambar,img1, img2):
        gambar[10:490,10:650] = img1[:,:]
        gambar[10:490,660:1300] = img2[:,:]
        return gambar
    
    def data_jalan(time,lubang,radio_btn,data = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],gps=["not connect",0,"N",0,"E"]):
        sinyal = 0
        if radio_btn[0] == 1:
            
            
            
            for i in lubang :
               if i[0] >= 319 and i[0] <= 321 :
                   n=data[len(data)-1][0]+1
                                 
                   data.append([n,time,i[2],i[3],i[4],'none',gps[1],gps[2],gps[3],gps[4]])
                   
                   sinyal = 1
        return data, sinyal
        
    def obj_track(layar1,depth):
        
        #membuat matrik kosong
        matriks = np.ones((480,640),'uint8')
        array = depth.astype(np.uint8)

        th, lem = cv2.threshold(array,0, 1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        #opening untuk menghilangkan noise
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
        kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        lem = cv2.morphologyEx(lem,cv2.MORPH_OPEN,kernel)
        lem = cv2.morphologyEx(lem,cv2.MORPH_CLOSE,kernel2)
       
        #mendapatkan kontur
        image,contour,_ = cv2.findContours(lem,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
              
        posisi =[]

        for c in contour:

            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(layar1,(x,y),(x+w,y+h),(0,255,0),2)
            x=x+int(w/2)
            y=y+int(h/2)
            cv2.circle(layar1,(x,y), 5, (0,0,255), -1)
            
            img = cv2.drawContours(matriks, contour, 0, 1, -1)
            img = cv2.morphologyEx(lem,cv2.MORPH_ERODE,kernel2)
            depth = depth*img
                                   
            maksimal = np.max(depth)
            volume = np.sum(depth)
            area = cv2.contourArea(c)
                      
            #menambahkan posisi serta area tiap objeck
            posisi.append([x,y,area,volume,maksimal])
        
        return layar1,posisi
    

    

    
           
            
        
        
