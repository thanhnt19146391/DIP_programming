# ############################################################################
#
# Author:       Nguyen Trung Thanh
# Author email: thanhnt19146391@gmail.com
#
# ###########################################################################/

import os
import sys
import tkinter as tk
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller import controller
from configuration import FONT

class Threadsolding(tk.Frame):

    def __init__(self, parent, grandparent):
        # Init for tk.Frame
        tk.Frame.__init__(self, parent)
        ctrl = controller()
        self.photos = ctrl.load_PhotoImages(
            ('home-button.png', 50)
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
        threshsholding_lb.grid(column = 1, row = 0, sticky = 'EW')
        
        # Home button
        home_btn = tk.Button(
            self, 
            text = 'Home', 
            font = FONT,
            bd = 0,
            image = self.photos[0],
            command = lambda: [grandparent.show_frame(0)])
        home_btn.grid(column = 2, row = 0, padx = 10, pady = 10, sticky = tk.NE)

  
        

        
        
if __name__ == '__main__':
    pass
    