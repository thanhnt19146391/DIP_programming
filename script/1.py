import cv2 as cv
import numpy as np

VIDEO_PATH = 'D:/Digital_Image_Processing/DIP_programming/video/video0.mp4'
WINNAME = 'Video'

def resize_image(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return resized


cap = cv.VideoCapture(VIDEO_PATH)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret: 
        '''
            The default frame as BGR.
            Convert BGR to RGB:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) 
        '''
        source_frame = resize_image(img = frame, scale_percent = 30)
        gray_frame = cv.cvtColor(source_frame, cv.COLOR_BGR2GRAY) 
        slide = np.concatenate((source_frame, source_frame), axis = 1)
        cv.imshow(winname = WINNAME, mat = slide)
        cv.imshow(winname = 'gray', mat = gray_frame)
        key = cv.waitKey(delay = 10)
        if key == 27:
            cv.destroyAllWindows()
            break

