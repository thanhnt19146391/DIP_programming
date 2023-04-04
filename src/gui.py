# ############################################################################
#
# Author:       Nguyen Trung Thanh
# Author email: thanhnt19146391@gmail.com
#
# ###########################################################################/

import sys
import tkinter as tk
from PIL import Image, ImageTk
from configuration import DEFAULT_WIDTH, DEFAULT_HEIGHT, SCALER
from pages.MenuPage import MenuPage
from pages.Threadsolding import Threadsolding
from controller import controller

# Controller of application
class DIP_Gui(tk.Tk):
    """Toplevel widget of Tk which represents the main window
    of our application."""
    def __init__(self, *arg, **kwargs):
        """ Back-end """
        print('We are in __init__ of DIP_Gui')
        self.src_img = None
        print('src_img = None')
        """ Front-end """
        # __init__ function for class tk.Tk
        tk.Tk.__init__(self, *arg, **kwargs)
        self.title("Digital Image Processing Bot")

        """
        Windown size
        We have some option below.
        Choose one of them and unable remainder
        """
        self.window_witdh = round(DEFAULT_WIDTH * SCALER)
        self.window_height = round(DEFAULT_HEIGHT * SCALER)
        # self.geometry(f"{self.window_witdh}x{self.window_height}+0+0")
        # self.attributes('-fullscreen', True)
        self.state('zoomed')
        
        self.pageLayouts = [
            MenuPage, 
            Threadsolding
        ]
        
        self.frames = {} 
        self.crete_container()
        self.show_frame(n = 0)

    
    def crete_container(self):
        # parent of frames
        self.container = tk.Frame(self) 
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1) 

    def show_frame(self, n):
        """
        n : order of page
        """
        # Ensure that n in range, otherwise return first frame  
        if n >= len(self.pageLayouts):
            n = 0
        # F is the page (class) at n 
        F = self.pageLayouts[n]
        # Init class 
        frame = F(parent = self.container, grandparent = self) 
        """ 
        parent = container (Frame), grandparent = MassageBotGui (Tk) 
        
        """
        self.frames[F] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")
        frame.tkraise()

if __name__ == '__main__':
    app = DIP_Gui()
    app.mainloop()