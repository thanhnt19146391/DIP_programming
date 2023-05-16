# ############################################################################
#
# Author:       Nguyen Trung Thanh
# Author email: thanhnt19146391@gmail.com
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

class VideoProcessing(tk.Frame):

    def __init__(self, parent, grandparent):
        print('We are in __init__ of VideoProcessing')
        # Init for tk.Frame
        tk.Frame.__init__(self, parent)
        ctrl = controller()
        self.photos = ctrl.load_PhotoImages(
            ('home-button.png', 50),
            ('video.png', 100),
            ('reload.png', 50)
        )
        
        # Threshold value
        self.thresh_val = tk.IntVar()

        # Column configure
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        # Thresholding label
        page_title_lb = tk.Label(
            self, 
            text = 'Video Processing', 
            font = FONT,
            
        )
        page_title_lb.grid(column = 0, row = 0, columnspan = 3, sticky = 'EW')
        
        # Home button
        home_btn = tk.Button(
            self, 
            text = 'Home', 
            font = FONT,
            bd = 0,
            image = self.photos[0],
            command = lambda: [grandparent.show_frame(0)])
        home_btn.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 10, sticky = tk.NE)

        

  
        

        
        
if __name__ == '__main__':
    pass
    