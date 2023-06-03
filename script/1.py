import cv2 as cv
import numpy as np

VIDEO_PATH = 'D:/Digital_Image_Processing/DIP_programming/video/video0.mp4'
WINNAME1 = 'Video'
WINNAME2 = 'Gray'
SCALE_PERCENT = 30

def resize_image(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return resized

# Naming a window
cv.namedWindow(winname = WINNAME1, flags = cv.WINDOW_GUI_NORMAL)
# Using resizeWindow()
cv.resizeWindow(winname = WINNAME1, width = round(1920 * SCALE_PERCENT / 100) * 2, height = round(1080 * SCALE_PERCENT / 100))
    
# Naming a window
cv.namedWindow(winname = WINNAME2, flags = cv.WINDOW_NORMAL)
# Using resizeWindow()
cv.resizeWindow(winname = WINNAME2, width = round(1920 * SCALE_PERCENT / 100), height = round(1080 * SCALE_PERCENT / 100))

cap = cv.VideoCapture(VIDEO_PATH)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret: 
        '''
            The default frame as BGR.
            Convert BGR to RGB:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) 
        '''
        print('Image shape: ', frame.shape)
        source_frame = frame
        dst_frame = source_frame.copy()
        gray_frame = cv.cvtColor(source_frame, cv.COLOR_BGR2GRAY)
       
        # Blur using 3 * 3 kernel.
        gray_blurred_frame = cv.blur(gray_frame, (3, 3))
        
        # detect circles in the image
        circles = cv.HoughCircles(
            image = gray_blurred_frame, 
            method = cv.HOUGH_GRADIENT, 
            dp = 1, 
            minDist = 100,
            param1 = 50,
            param2 = 30,
            minRadius = 100,
            maxRadius = 150)
        
        
        print('-----------------------------------------------')
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for index, (x, y, r) in enumerate(circles):
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv.circle(dst_frame, (x, y), r, (0, 255, 0), 4)
                cv.rectangle(dst_frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

                # Monitor informations
                print(f'{index} ({x}, {y}) r = {r}')


        
        slide = np.concatenate((source_frame, dst_frame), axis = 1)
        cv.imshow(winname = WINNAME1, mat = slide)
        cv.imshow(winname = WINNAME2, mat = gray_blurred_frame)
        key = cv.waitKey(delay = None)
        if key == 27:
            cv.destroyAllWindows()
            break

