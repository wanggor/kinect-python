#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:31:06 2018

@author: fotoniks
"""
import numpy as np
import cv2

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
