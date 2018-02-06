#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:31:06 2018

@author: fotoniks
"""
import cv2
import time
from kinect_ta import KinectTA
from windows import main_windows,radio_btn
from process import display



windows = main_windows(1310,710,240,240,240)
gambar = windows.background()

gambar, pss_Start = windows.button(gambar,100,550,150,'Start')
gambar, pss_Pause= windows.button(gambar,100,600,150,'Pause')


gambar, pss_Record= windows.button(gambar,100,650,150,'Record')

gambar, pss_RGB = windows.button(gambar,350,575,160,'Citra RGB')
gambar, pss_Infra= windows.button(gambar,350,625,160,'Citra Inframerah')


gambar, pss_Gray = windows.button(gambar,630,550,280,'Citra Kedalam (Gray Scale)')
gambar, pss_JET= windows.button(gambar,630,600,280,'Citra Kedalaman (JET)')
gambar, pss_Thres = windows.button(gambar,630,650,280,'Citra Kedalaman (Thresholding)')

posisi =[[pss_Start,pss_Pause],pss_Record,[pss_RGB,pss_Infra],[pss_Gray,pss_JET,pss_Thres]]

cv2.namedWindow('image')

rdio_btn = radio_btn(posisi,gambar)
cv2.setMouseCallback('image',rdio_btn.Btn_Click)




data = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

t1 = 0



fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
n=0;

while(1):
    t2 = time.time()
    print(t2-t1)
    t1 = time.time()

    img1 = display.layar_1(rdio_btn.signal)
    img2 = display.layar_2(rdio_btn.signal)
    
    img1,img2, lubang =display.obj_track(img1,img2)

    gambar = display.merge(rdio_btn.gambar,img1,img2)
    cv2.imshow('image',gambar)
    
    main_windows.tble_view(gambar,data)
    
    if rdio_btn.signal[0] == 1:
        
        for i in lubang :
           if i[0] == 320:
               data[n][2]=i[2]
               n=n+1
           
    
    #save video when start and rerecord button is pressed
    if rdio_btn.signal[0] == 1 and rdio_btn.signal[2] == 1:
        frame = cv2.flip(img2,0)
        out.write(frame)

    if cv2.waitKey(20) & 0xFF == 27:
        KinectTA.image_stop()
        break
out.release()
cv2.destroyAllWindows()
                
            