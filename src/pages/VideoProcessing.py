# ############################################################################
#
# Author:       Nguyen Trung Thanh
# Author email: thanhnt19146391@gmail.com
# 
# ###########################################################################/

import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller import controller
from configuration import FONT
import cv2
import numpy as np
from matplotlib import pyplot as plt

class video():
    def __init__(self, master, col, row, scale):
        self.scale = scale

        self.frame_label = tk.Label(
            master = master
        )

        self.frame_label.grid(column = col, row = row)

        self.update_frame(master.frames[0])

    def createPhotoImage(self, mat, scale = None):
        if scale == None:
            scale = 1
        img = Image.fromarray(mat)
        w, h = img.size
        w = int(w * scale)
        h = int(h * scale)
        img = img.resize((w, h))
        dst = ImageTk.PhotoImage(image = img)
        return dst
    
    def update_frame(self, frame):
        self.photoImage = self.createPhotoImage(frame, self.scale)
        self.frame_label.config(image = self.photoImage)

class VideoProcessing(tk.Frame):

    def __init__(self, parent, grandparent):

        print('We are in __init__ of VideoProcessing')
        tk.Frame.__init__(self, parent)
        ctrl = controller()

        self.photos = ctrl.load_PhotoImages(
            ('home-button.png', 50),
            ('video.png', 100),
            ('reload.png', 50)
        )
        
        '''
            Column configure
        '''
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)
        
        '''
            Title :         col = 0, row = 0
            Home button:    col = 0, row = 0
            Video path:     col = 0, row = 1
            Frame index:    col = 1, row = 1
            Previous index: col = 2, row = 1
            Next index:     col = 3, row = 1
            Source video:   col = 0, row = 2
        '''

        # Title label
        page_title_lb = tk.Label(
            self, 
            text = 'Video Processing', 
            font = FONT
            
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

        '''
            Frame index: show the index of current frame
        '''
        self.frame_index = 0
        self.frame_index_lb = tk.Label(
            self, 
            text = f'Frame index : {self.frame_index}', 
            font = FONT
        )
        self.frame_index_lb.grid(column = 1, row = 1, sticky = tk.E)

        '''
            Previou index button
        '''
        pre_index_button = tk.Button(
            self, 
            text = 'Previous', 
            font = FONT,
            bd = 1,
            command = lambda: [self.update_frame_index(-1)])
        pre_index_button.grid(column = 2, row = 1)
        
        '''
            Previou index button
        '''
        next_index_button = tk.Button(
            self, 
            text = 'Next', 
            font = FONT,
            bd = 1,
            command = lambda: [self.update_frame_index(1)])
        next_index_button.grid(column = 3, row = 1)

        '''
            Video path
        '''
        video_path_lb = tk.Label(
            self, 
            text = 'Video path : ', 
            font = FONT
        )
        video_path_lb.grid(column = 0, row = 1, sticky = 'W')
        
        self.video_path = tk.StringVar(self, value = str('D:/Digital_Image_Processing/DIP_programming/video/video0.mp4'))
        
        video_path_entry = tk.Entry(self, textvariable = self.video_path, width = 100, font = FONT)
        video_path_entry.grid(column = 0, row = 1, sticky = 'W', padx = 150)

        '''
            Import source video
        '''
        self.import_source_video()

        '''
            Show source video
        '''
        self.source_video = video(master = self, col = 0, row = 2, scale = 0.25)
        
        
    
    def import_source_video(self):
        '''
            Import video frome video path
            Save number of frames as self.frames
        '''
        try: 
            cap = cv2.VideoCapture(self.video_path.get())
            self.frames = []
            while(cap.isOpened()):
                if len(self.frames) > 200:
                    break
                ret, frame = cap.read()
                if ret: 
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    self.frames.append(frame) 
                else:
                    break
            print(f'Successefully import video\nNumber of frame: {len(self.frames)}')      
        except: 
            print('Error: import video')
        
    def update_frame_index(self, value):
        self.frame_index += value
        if self.frame_index < 0 or self.frame_index == len(self.frames):
            self.frame_index = 0
        self.frame_index_lb.config(text = f'Frame index : {self.frame_index}')
        self.source_video.update_frame(frame = self.frames[self.frame_index])
            

        
        
if __name__ == '__main__':
    pass
    