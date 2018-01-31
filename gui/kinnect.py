# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore,  QtWidgets,  QtGui

from Ui_kinnect import Ui_MainWindow
from kinect_ta import KinectTA
t=0

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        self.tmr = QtCore.QTimer()
        self.tmr.timeout.connect(self.kinect_image)
        #class kinect 
        self.knct = KinectTA()
        
        self.scene1 = QtWidgets.QGraphicsScene()
        self.scene2 = QtWidgets.QGraphicsScene()
        
        self.isGray = 0 #defoul JET
        self.isRGB = 1
        self.t2=0
        print('a')
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btnStrart_released(self):
        """
        Slot documentation goes here.
        """
        self.tmr.start(0)
       
    
    @pyqtSlot()
    def on_btnPause_released(self):
        """
        Slot documentation goes here.
        """
        self.tmr.stop()
        self.knct.image_stop()
    
    @pyqtSlot()
    def on_btnSave_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass
    

    
    @pyqtSlot()
    def on_radioButtongray_clicked(self):
        """
        Slot documentation goes here.
        """
       
        # TODO: not implemented yet
        self.isGray = 1
    

    
    @pyqtSlot()
    def on_radioButtonjet_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.isGray = 2
    

    
    @pyqtSlot()
    def on_radioButtonTresh_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.isGray = 3   

    
    @pyqtSlot()
    def on_radioButtonRGB_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.isRGB = 1
    
    
    @pyqtSlot()
    def on_radioButtonInfra_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.isRGB = 2

    def kinect_image(self):
        t1=time.time()
        #print(t1-self.t2)
      
        
        #layar 1
        if self.isRGB == 1:
            RGB = self.knct.get_video()
            qimg1 = QtGui.QImage(RGB.data,RGB.shape[1], RGB.shape[0], QtGui.QImage.Format_RGB888)
            self.scene1.addPixmap(QtGui.QPixmap(qimg1))
            self.grpvImg1.setScene(self.scene1)
        if self.isRGB == 2:
            RGB = self.knct.get_infra()
            qimg1 = QtGui.QImage(RGB.data,RGB.shape[1], RGB.shape[0], QtGui.QImage.Format_RGB888)
            self.scene1.addPixmap(QtGui.QPixmap(qimg1))
            self.grpvImg1.setScene(self.scene1)
        
        #qimg = QtGui.QImage(imghasil.data,imghasil.shape[1], imghasil.shape[0], QtGui.QImage.Format_RGB888)
       
        #layar 2
        if self.isGray == 1:
            Gray = self.knct.get_depthGray()
            qimg2 = QtGui.QImage(Gray.data,Gray.shape[1], Gray.shape[0], QtGui.QImage.Format_RGB888)
            self.scene2.addPixmap(QtGui.QPixmap(qimg2))
            self.grpvImg2.setScene(self.scene2)
        if self.isGray == 2:
            JET = self.knct.get_depthJET()
            qimg2 = QtGui.QImage(JET.data,JET.shape[1], JET.shape[0], QtGui.QImage.Format_RGB888)
            self.scene2.addPixmap(QtGui.QPixmap(qimg2))
            self.grpvImg2.setScene(self.scene2)
        if self.isGray == 3:
            Thrs = self.knct.depth_thres()
            qimg2 = QtGui.QImage(Thrs.data,Thrs.shape[1], Thrs.shape[0], QtGui.QImage.Format_RGB888)
            self.scene2.addPixmap(QtGui.QPixmap(qimg2))
            self.grpvImg2.setScene(self.scene2)
        self.t2=time.time()
        
        
       

    
