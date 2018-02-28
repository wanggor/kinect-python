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
import threading
import serial

def wahyu():
    global a
    a = 0
    while 1:
        a=a+1
#        print(str(a))
        time.sleep(1)
        
        
    
def data_gps():
    global gps  
    data_gps=["not connect",0,"N",0,"E"] 
    error = "USB is not pluged in or port cannot to be read" 
    try:
        
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = "/dev/ttyACM0"
        ser.timeout = 1
        ser.open()
        
        #ser_io = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        
        if ser.isOpen():
            
        #	print('Open: %s' % str(ser.port))
        
        	#while 1:
        		#ser_io.write("AT\n")
        		#ser_io.flush()
        		#ser_recev = ser_io.readline()
        		#if len(ser_recev) > 0:
        			#print(ser_recev)
        			#break
        		#time.sleep(0.1)
            
            
            
            #to make sure arduino connect to GSM modul
            while 1:
                error = "Arduino not connected"
                
                ser.write(bytearray(b'AT\n\r'))
                respons =  ser.readlines()
                        
                if len(respons)>1 :
                    respons = str(respons[1],'utf-8')
                    if respons == "OK\r\n":
                        break
                        
            
            respons = []
            
            
            #to make sure GPS activate 
            while 1:
                error = "GPS not activate"
                
                ser.write(bytearray(b'AT+CGPSPWR=1\n\r'))
                respons =  ser.readlines()
                print (respons)
                
                if len(respons)>1 :
                    respons = str(respons[1],'utf-8')
                    if respons == "OK\r\n":
                        
                        break
                
            a=0
            
            
            while 1:
                error = "Something wrong with your GPS"
                
#                t=time.time()
                ser.write(bytearray(b'AT+CGPSINF=32\n\r'))
                        
                recev = ser.readlines()
                recev = str(recev[1],'utf-8')
                
                if len(recev) > 0:
                    
                    recev = recev.split(',')
                    if recev[2] == "A":
                        
                        data_gps[0] = "Connect"
                        data_gps[1] = recev[3][0:2]+" deg "+ recev[3][2:len(recev)]
                        data_gps[2] = recev [4]
                        data_gps[3] = recev[5][0:3]+" deg "+ recev[5][3:len(recev)]
                        data_gps[4] = recev [6]
                    else:
                        data_gps[0] = "Not Connect"
                    
                    print(data_gps)
                
                gps=data_gps
                a=a+1
#                print(time.time()-t)
                if cv2.waitKey(20) & 0xFF == 27:
                                        
                    break
        		
            while 1:
                
                error = "GPS cannot to be closed"
                
                ser.write(bytearray(b'AT+CGPSPWR=0\n\r'))
                respons =  ser.readlines()
                print (respons)
                
                if len(respons)>1 :
                    respons = str(respons[1],'utf-8')
                    if respons == "OK\r\n":
                        
                        break    
            ser.close()
    
    
    except:
        ser.close()
        print(error)
        exit
    print(error)
#    return data_gps



def windows(a=0):
    global gps
    gps=["not connect",0,"N",0,"E"] 

    gambar, posisi = main_windows.windows() 
    cv2.namedWindow('image')
    rdio_btn = radio_btn(posisi,gambar)
    cv2.setMouseCallback('image',rdio_btn.Btn_Click)
    
    
    
    
    data = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    

    
    
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    
#    a=0
    while(1):

#        print(str(a))
#        a=a+1

        img1 = display.layar_1(rdio_btn.signal)
        img2,depth = display.layar_2(rdio_btn.signal)
        
        img1, lubang = display.obj_track(img1,depth)
    
        gambar = display.merge(rdio_btn.gambar,img1,img2)
        
    
            
        data =display.data_jalan(lubang,rdio_btn.signal,data)
        main_windows.tble_view(gambar,data)
        latar = main_windows.Gps(gambar,gps)
        
        cv2.imshow('image',gambar)
#        print(a)
        gambar = latar
    
        #save video when start and rerecord button is pressed
        if rdio_btn.signal[0] == 1 and rdio_btn.signal[2] == 1:
            frame = cv2.flip(img2,0)
            out.write(frame)
    
        if cv2.waitKey(20) & 0xFF == 27:
            KinectTA.image_stop()
            break
        
    out.release()
    cv2.destroyAllWindows()
    
    return data

#gps=["not connect",0,"N",0,"E"]
#
#t1= threading.Thread(target=windows)
#t2= threading.Thread(target=data_gps)
#
#t1.start()
#t2.start()
windows()