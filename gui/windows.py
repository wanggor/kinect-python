import numpy as np
import cv2

class main_windows():
    ''' Class for build a button and background with width(px), height(px), 
        and single color (red,green, blue)'''
        
    def __init__(self,width,height,red,green,blue):
        self.width = width
        self.height = height
        self.color = [ blue, green,red ]

    
    def background(self):
        
        ''' build canvas/background for display the image or GUI for user'''
        
        windows = np.ones((self.height,self.width,3))
        windows = windows.astype(np.uint8)
        for i in range (3):
            windows[:,:,i] = windows[:,:,i]* self.color[i]
        return windows
    
    def button(self ,a, x, y,l, kata, switch=0):
        ''' build button for display the image or GUI for user
            return in posisition of button in canvas or background'''
        img = cv2.rectangle(a,(x,y),(x + l,y+30),(255,255,255),-1)
        img = cv2.rectangle(img,(x+5,y+5),(x + l-5,y + 25),(150,150,150),1)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img,kata,(x+15,y+20), font, 0.5,(50,50,50),1,cv2.LINE_AA)
        
        if switch%2 == 0:
            img = cv2.circle(img,(x+5,y+15), 5, (0,0,255), -1)
        else :
            img = cv2.circle(img,(x+5,y+15), 5, (0,255,0), -1)
        
        position = []
        
        for i in range (l):
            for j in range (30):
                position.append([j+y,i+x])
        
        return img, position
    
    def tble_view(background, data=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]):
    
        font = cv2.FONT_HERSHEY_DUPLEX
        size = len(data)
        x = 0
        y = 0 
        
        space = [25,80,80,80,30]
        
        
        cv2.rectangle(background,(920,520),(1290,700),(255,255,255),-1)
        cv2.rectangle(background,(920,520),(950,700),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1030,700),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1110,700),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1190,700),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1290,700),(0,0,0),1)
        
        cv2.rectangle(background,(920,520),(1290,550),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1290,580),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1290,610),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1290,640),(0,0,0),1)
        cv2.rectangle(background,(920,520),(1290,670),(0,0,0),1)
        
        cv2.putText(background,'NO',(925,540), font, 0.5,(50,50,50),1,cv2.LINE_AA)
        cv2.putText(background,'LUAS',(955,540), font, 0.5,(50,50,50),1,cv2.LINE_AA)
        cv2.putText(background,'VOLUME',(1035,540), font, 0.5,(50,50,50),1,cv2.LINE_AA)
        cv2.putText(background,'TINGGI(MAK)',(1112,540), font, 0.4,(50,50,50),1,cv2.LINE_AA)
        cv2.putText(background,'KONDISI',(1195,540), font, 0.5,(50,50,50),1,cv2.LINE_AA)
        
        for i in data[size-5:size] :
            x = 0
            n=0
            for j in i:
                      
                cv2.putText(background,str(j),(930+x,695-y), font, 0.3,(50,50,50),1,cv2.LINE_AA)
                x = x + space[n]
                n=n+1
            y = y + 30

class radio_btn():
    ''' make button into radio button, and return signal that indicate which
        the button is press on'''
    def __init__ (self, posisi, gambar):
        self. posisi = posisi
        self.Gray = 0
        self.Jet = 0
        self.Thr=0
        
        self.gambar =gambar
        
        self.RGB=0
        self.Infra=0
        
        self.Start=0
        self.Pause=0
        self.Record=0
        self. signal = [0,0,0,0,0,0,0,0]
    
    def Btn_Click(self,event,x,y,flags,param):

        
    
        if event == cv2.EVENT_LBUTTONDOWN:
             if [y,x] in self.posisi[3][0]:
                 self.Gray = self.Gray + 1
                                    
                 if self.Gray%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(635,565), 5, (0,255,0), -1)
                     self.gambar= cv2.circle(self.gambar,(635,615), 5, (0,0,255), -1)
                     self.gambar= cv2.circle(self.gambar,(635,665), 5, (0,0,255), -1)
                     self.Jet = 0
                     self.Thr = 0
             if [y,x] in self.posisi[3][1]:
                 self.Jet = self.Jet + 1
                     
                 if self.Jet%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(635,615), 5, (0,255,0), -1)
                     self.gambar= cv2.circle(self.gambar,(635,565), 5, (0,0,255), -1)
                     self.gambar= cv2.circle(self.gambar,(635,665), 5, (0,0,255), -1)
                     self.Gray = 0
                     self.Thr = 0
             if [y,x] in self.posisi[3][2]:
                 self.Thr = self.Thr + 1
                     
                 if self.Thr%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(635,665), 5, (0,255,0), -1)
                     self.gambar= cv2.circle(self.gambar,(635,615), 5, (0,0,255), -1)
                     self.gambar= cv2.circle(self.gambar,(635,565), 5, (0,0,255), -1)
                     self.Gray = 0
                     self.Jet = 0
                     
             if [y,x] in self.posisi[2][0]:
                 self.RGB = self.RGB + 1
                     
                 if self.RGB%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(355,590), 5, (0,255,0), -1)
                     self.gambar= cv2.circle(self.gambar,(355,640), 5, (0,0,255), -1)
                     self.Infra = 0
                     
             if [y,x] in self.posisi[2][1]:
                 self.Infra = self.Infra + 1
                     
                 if self.Infra%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(355,640), 5, (0,255,0), -1)
                     self.gambar= cv2.circle(self.gambar,(355,590), 5, (0,0,255), -1)
                     self.RGB = 0
             if [y,x] in self.posisi[0][0]:
                 self.Start = self.Start + 1
                     
                 if self.Start%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(105,565), 5, (0,255,0), -1)
                     self.gambar= cv2.circle(self.gambar,(105,615), 5, (0,0,255), -1)
                     self.Pause = 0
                     
             if [y,x] in self.posisi[0][1]:
                 self.Pause = self.Pause + 1
                     
                 if self.Pause%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(105,615), 5, (0,255,0), -1)
                     self.gambar= cv2.circle(self.gambar,(105,565), 5, (0,0,255), -1)
                     self.Start = 0
             if [y,x] in self.posisi[1]:
                 self.Record = self.Record + 1
                 print(self.Record)
                 if self.Record%2 is not 0 :
                     self.gambar= cv2.circle(self.gambar,(105,665), 5, (0,255,0), -1)
                 else:
                     self.gambar= cv2.circle(self.gambar,(105,665), 5, (0,0,255), -1)
             self.signal=[self.Start, self.Pause, self.Record, self.RGB, self.Infra, self.Gray, self.Jet, self.Thr]
    
        
    
    
    
     