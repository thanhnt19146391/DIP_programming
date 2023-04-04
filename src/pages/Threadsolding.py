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
        
        if grandparent.src_img == None:
            print('Src_img = None')
        else:
            print('Src_img is not None')
        self.src_img_lb = tk.Label(
            self,
            image = self.photos[1] if grandparent.src_img == None else grandparent.src_img,
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
    
        
    def update_image(self, ctrl, grandparent):
        """
        Local update image: This function will call controller
        which update global source image

        """
        ret = ctrl.update_image(grandparent = grandparent)
        if ret:
            self.src_img_lb.config(image = grandparent.src_img)
        else:
            messagebox.showinfo(title = 'Message', message = "Clipboard is Empty.")
  
        

        
        
if __name__ == '__main__':
    pass
    