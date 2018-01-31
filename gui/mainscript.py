#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import time as tm
import cv2

import pygtk
pygtk.require('2.0')
    
import gtk
import gtk.glade
import numpy as np 

from kinect_ta import KinectTA

class WahyuKinect:
	def __init__(self):
		
		# get GUI file
		guibuilder=gtk.Builder()
		guibuilder.add_from_file("windowgui.glade")
		guibuilder.connect_signals(self)
		
		# window object
		window=guibuilder.get_object("mainWindow")
		window.connect("destroy",self.on_destroy)
		
		# image view object
		self.imgview1 = guibuilder.get_object("imgv1")
		self.imgview2 = guibuilder.get_object("imgv2")
		self.imgview1.set_size_request(320, height=240)
		self.imgview2.set_size_request(320, height=240)
		
		# button start object
		btnStart=guibuilder.get_object("btnStart")
		btnStart.connect("clicked",self.on_start)
		
		# button stop object
		btnStop=guibuilder.get_object("btnStop")
		btnStop.connect("clicked",self.on_stop)
		
		# radio button object
		self.rbtRGB=guibuilder.get_object("rbtRGB")
		self.rbtIR=guibuilder.get_object("rbtIR")
		
		# radio button object
		self.rbtGray=guibuilder.get_object("rbtGray")
		self.rbtJET=guibuilder.get_object("rbtJET")
		self.rbtThresh=guibuilder.get_object("rbtThresh")
		
		# define all initial flag
		self.run_flag = 0
		self.t1 = 0
		
		# add timeout callback
		gtk.timeout_add(40, self.loop_cb) # 40 finest resolution
		
		# define kinect object
		self.kc = KinectTA()
		
		# final app show
		window.show()
		
	def on_destroy(self, widget):
		self.kc.kinect_stop()
		gtk.main_quit()
		
	def on_start(self, widget):
		self.run_flag = 1
		
	def on_stop(self, widget):
		self.run_flag = 0
		self.kc.kinect_stop()
		
	def loop_cb(self):
		if self.run_flag == 1:
			if self.rbtRGB.get_active():
				img1 = self.kc.get_video()
			else:
				img1 = self.kc.get_infra()
				
			self.imgview1.set_from_pixbuf(gtk.gdk.pixbuf_new_from_array(
										img1,
										gtk.gdk.COLORSPACE_RGB,
										8))
			
			if self.rbtGray.get_active():
				img2 = self.kc.get_depthGray()
			elif self.rbtJET.get_active():
				img2 = self.kc.get_depthGray()
			elif self.rbtThresh.get_active():							
				img2 = self.kc.get_depthThres()
				
			self.imgview2.set_from_pixbuf(gtk.gdk.pixbuf_new_from_array(
										img2,
										gtk.gdk.COLORSPACE_RGB,
										8))
										
			self.t2 = tm.time()
			print(self.t2 - self.t1)
			self.t1 = tm.time()
		
		return True
	
if __name__ == "__main__":
    app = WahyuKinect()
    gtk.main()

