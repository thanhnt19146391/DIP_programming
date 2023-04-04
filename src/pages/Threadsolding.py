# ############################################################################
#
# Author:       Nguyen Trung Thanh
# Author email: thanhnt19146391@gmail.com
# References: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# 
# ###########################################################################/

import os
import sys
import tkinter as tk
from tkinter import messagebox
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller import controller
from configuration import FONT
import cv2
import numpy as np
from matplotlib import pyplot as plt

class Threadsolding(tk.Frame):

    def __init__(self, parent, grandparent):
        print('We are in __init__ of Threadsolding')
        # Init for tk.Frame
        tk.Frame.__init__(self, parent)
        ctrl = controller()
        self.photos = ctrl.load_PhotoImages(
            ('home-button.png', 50),
            ('image-processing.png', 100),
            ('reload.png', 50)
        )
        
        # Threshold value
        self.thresh_val = tk.IntVar()

        # Column configure
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        # Thresholding label
        threshsholding_lb = tk.Label(
            self, 
            text = 'Image Threasholding', 
            font = FONT,
            
        )
        threshsholding_lb.grid(column = 0, row = 0, columnspan = 3, sticky = 'EW')
        
        # Home button
        home_btn = tk.Button(
            self, 
            text = 'Home', 
            font = FONT,
            bd = 0,
            image = self.photos[0],
            command = lambda: [grandparent.show_frame(0)])
        home_btn.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 10, sticky = tk.NE)

         # Label (text): Source image
        src_img_txt = tk.Label(
            self, 
            text = 'Source image', 
            font = FONT
        )
        src_img_txt.grid(column = 0, row = 1, sticky = 'W', padx = 10)

        # Label (image): Source image
        self.src_img_lb = tk.Label(
            self,
            image = self.photos[1] if grandparent.src_photo_img == None else grandparent.src_photo_img,
            bd = 0            
        )
        self.src_img_lb.grid(column = 0, row = 2, columnspan = 2, sticky = 'W', padx = 10)

        # Button: update image from clipboard
        update_img_btn = tk.Button(
            self,
            text = 'Update image', 
            font = FONT,
            bd = 0,
            image = self.photos[2],
            command = lambda: [
                self.update_image(ctrl = ctrl, grandparent = grandparent)
            ]
        )
        update_img_btn.grid(column = 0, row = 1, sticky = 'W', padx = 120)

        # Button: Simple thresholding
        sim_thresh_btn = tk.Button(
            self,
            text = 'Simple thresholding', 
            font = FONT,
            bd = 2,
            command = lambda: [
                self.Simple_Thresholding(file_path = grandparent.src_img_path, thresh_val = self.thresh_val.get())
            ]
        )
        sim_thresh_btn.grid(column = 1, row = 1, sticky = 'W', padx = 120)

        # Scale: Threshold scale
        thresh_scale = tk.Scale(
            master = self,
            variable = self.thresh_val,
            from_ = 0,
            to = 255,
            orient = tk.HORIZONTAL
        )
        thresh_scale.grid(column = 1, row = 2, sticky = 'W', padx = 120)
        
    def update_image(self, ctrl, grandparent):
        """
        Local update image: This function will call controller
        which update global source image

        """
        ret = ctrl.update_image(grandparent = grandparent)
        if ret:
            self.src_img_lb.config(image = grandparent.src_photo_img)
        else:
            messagebox.showinfo(title = 'Message', message = "Clipboard is Empty.")

    def Simple_Thresholding(self, file_path = None, thresh_val = 127):
        """ file_path of source image """
        print(self.thresh_val.get())
        img = cv2.imread(filename = file_path, flags = cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check out file path"
        ret, thresh1 = cv2.threshold(src = img, thresh = thresh_val, maxval = 255, type = cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(src = img, thresh = thresh_val, maxval = 255, type = cv2.THRESH_BINARY_INV)
        ret, thresh3 = cv2.threshold(src = img, thresh = thresh_val, maxval = 255, type = cv2.THRESH_TRUNC)
        ret, thresh4 = cv2.threshold(src = img, thresh = thresh_val, maxval = 255, type = cv2.THRESH_TOZERO)
        ret, thresh5 = cv2.threshold(src = img, thresh = thresh_val, maxval = 255, type = cv2.THRESH_TOZERO_INV)
        titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
        images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
        for i in range(6):
            res = plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.ion()
        plt.show()

  
        

        
        
if __name__ == '__main__':
    pass
    