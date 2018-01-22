# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore,  QtWidgets,  QtGui

from Ui_mainwindow import Ui_MainWindow
from kinect_ta import KinectTA

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
        
        self.knct = KinectTA()
        
        self.scene = QtWidgets.QGraphicsScene()
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btnStart_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.tmr.start(10)
    
    @pyqtSlot()
    def on_btnStop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.tmr.stop()
        self.knct.image_stop()
        
    def kinect_image(self):
        imghasil = self.knct.image_loop()
        #qimg = QtGui.QImage(imghasil.data,imghasil.shape[1], imghasil.shape[0], QtGui.QImage.Format_RGB888)
        qimg = QtGui.QImage(imghasil.data,imghasil.shape[1], imghasil.shape[0], QtGui.QImage.Format_RGB888)
        self.scene.addPixmap(QtGui.QPixmap(qimg))
        self.grphKnct.setScene(self.scene)
