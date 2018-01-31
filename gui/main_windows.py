#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:31:06 2018

@author: fotoniks
"""
import numpy as np
import cv2
import time
from kinect_ta import KinectTA


class main_windows():
    
    def __init__(self,width,height,red,green,blue):
        self.width = width
        self.height = height
        self.color = [ blue, green,red ] 
    
    def background(self):
        windows = np.ones((self.height,self.width,3))
        windows = windows.astype(np.uint8)
        for i in range (3):
            windows[:,:,i] = windows[:,:,i]* self.color[i]
        return windows
    
    def button(self ,a, x, y,l, kata, switch=0):
        
        img = cv2.rectangle(a,(x,y),(x + l,y+30),(255,255,255),-1)
        img = cv2.rectangle(img,(x+5,y+5),(x + l-5,y + 25),(150,150,150),1)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,kata,(x+15,y+20), font, 0.5,(0,0,0),1,cv2.LINE_AA)
        
        if switch%2 == 0:
            img = cv2.circle(img,(x+5,y+15), 5, (0,0,255), -1)
        else :
            img = cv2.circle(img,(x+5,y+15), 5, (0,255,0), -1)
        
        position = []
        
        for i in range (l):
            for j in range (30):
                position.append([j+y,i+x])
        
        return img, position


    
    def Btn_Click(event,x,y,flags,param):
        global Gray
        global Jet
        global Thr
        
        global gambar
        
        global RGB
        global Infra
        
        global Start
        global Pause
        global Record
        
        if event == cv2.EVENT_LBUTTONDOWN:
             if [y,x] in pss_Gray:
                 Gray = Gray + 1
                                    
                 if Gray%2 is not 0 :
                     gambar= cv2.circle(gambar,(705,515), 5, (0,255,0), -1)
                     gambar= cv2.circle(gambar,(705,565), 5, (0,0,255), -1)
                     gambar= cv2.circle(gambar,(705,615), 5, (0,0,255), -1)
                     Jet = 0
                     Thr = 0
             if [y,x] in pss_JET:
                 Jet = Jet + 1
                     
                 if Jet%2 is not 0 :
                     gambar= cv2.circle(gambar,(705,565), 5, (0,255,0), -1)
                     gambar= cv2.circle(gambar,(705,515), 5, (0,0,255), -1)
                     gambar= cv2.circle(gambar,(705,615), 5, (0,0,255), -1)
                     Gray = 0
                     Thr = 0
             if [y,x] in pss_Thres:
                 Thr = Thr + 1
                     
                 if Thr%2 is not 0 :
                     gambar= cv2.circle(gambar,(705,615), 5, (0,255,0), -1)
                     gambar= cv2.circle(gambar,(705,565), 5, (0,0,255), -1)
                     gambar= cv2.circle(gambar,(705,515), 5, (0,0,255), -1)
                     Gray = 0
                     Jet = 0
                     
             if [y,x] in pss_RGB:
                 RGB = RGB + 1
                     
                 if RGB%2 is not 0 :
                     gambar= cv2.circle(gambar,(405,540), 5, (0,255,0), -1)
                     gambar= cv2.circle(gambar,(405,590), 5, (0,0,255), -1)
                     Infra = 0
                     
             if [y,x] in pss_Infra:
                 Infra = Infra + 1
                     
                 if Infra%2 is not 0 :
                     gambar= cv2.circle(gambar,(405,590), 5, (0,255,0), -1)
                     gambar= cv2.circle(gambar,(405,540), 5, (0,0,255), -1)
                     RGB = 0
             if [y,x] in pss_Start:
                 Start = Start + 1
                     
                 if Start%2 is not 0 :
                     gambar= cv2.circle(gambar,(105,515), 5, (0,255,0), -1)
                     gambar= cv2.circle(gambar,(105,565), 5, (0,0,255), -1)
                     Pause = 0
                     
             if [y,x] in pss_Pause:
                 Pause = Pause + 1
                     
                 if Pause%2 is not 0 :
                     gambar= cv2.circle(gambar,(105,565), 5, (0,255,0), -1)
                     gambar= cv2.circle(gambar,(105,515), 5, (0,0,255), -1)
                     Start = 0
             if [y,x] in pss_Record:
                 Record = Record + 1
                 print(Record)
                 if Record%2 is not 0 :
                     gambar= cv2.circle(gambar,(105,615), 5, (0,255,0), -1)
                 else:
                     gambar= cv2.circle(gambar,(105,615), 5, (0,0,255), -1)

       
                     
Gray = 0
Jet = 0
Thr = 0

RGB = 0
Infra = 0

Start = 0
Pause = 0
Record = 0 



windows = main_windows(1310,750,240,240,240)
gambar = windows.background()

gambar, pss_Start = windows.button(gambar,100,500,150,'Start')
gambar, pss_Pause= windows.button(gambar,100,550,150,'Pause')
radiobtn_1 = [pss_Start,pss_Pause]

gambar, pss_Record= windows.button(gambar,100,600,150,'Record')

gambar, pss_RGB = windows.button(gambar,400,525,150,'Citra RGB')
gambar, pss_Infra= windows.button(gambar,400,575,150,'Citra Inframerah')
radiobtn_2 = [pss_RGB,pss_Infra]

gambar, pss_Gray = windows.button(gambar,700,500,270,'Citra Kedalam (Gray Scale)')
gambar, pss_JET= windows.button(gambar,700,550,270,'Citra Kedalaman (JET)')
gambar, pss_Thres = windows.button(gambar,700,600,270,'Citra Kedalaman (Thresholding)')
radiobtn_3 = [pss_Gray,pss_JET,pss_Thres]

radioBtn = [radiobtn_1,radiobtn_2,radiobtn_3]


cv2.namedWindow('image')
cv2.setMouseCallback('image',main_windows.Btn_Click)

t1 = 0
while(1):
    t2 = time.time()
    print(t2-t1)
    t1 = time.time()
    if RGB%2 is not 0:
        img1 = KinectTA.get_video()
    else :
        img1 = KinectTA.get_infra()
    if Gray%2 is not 0:
        img2 = KinectTA.get_depthGray()
    elif Jet%2 is not 0:
        img2 = KinectTA.get_depthJET()
    else:
        img2 = KinectTA.depth_thres()
        
    
    gambar[10:490,10:650] = img1[:,:]
    gambar[10:490,660:1300] = img2[:,:]
    cv2.imshow('image',gambar)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
                
            