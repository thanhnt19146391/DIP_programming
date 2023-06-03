from PIL import ImageGrab
from datetime import datetime
import cv2
import numpy as np
import sched, time
from win32gui import GetWindowText, GetForegroundWindow
from collections import namedtuple

BOX = namedtuple('Box', ['x', 'y', 'w', 'h'])


WINDOW_NAME = 'Cửu Âm Chân Kinh  CACK-Vô Danh Kiếm'
WINNAME1 = 'Source'
SAVE_PATH = 'image'
DELAY = 1 # 1 second
SCALE_PERCENT = 30
MAP_BOX = BOX(x = 1410, y = 65, w = 160, h = 160)
ALL_BOX = BOX(x = 1090, y = 560, w = 95, h = 35)

def center_of_box(box):
    x = box.x + box.w // 2
    y = box.y + box.h // 2
    return (x, y)

def detect_green(bgr_image):
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    return hsv_image

def detect_all_box(bgr_img):
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)
    white_pixels = np.sum(thresh == 255)
    print(f'White pixels: {white_pixels}') 
    if white_pixels > 220:
        return 1
    else:
        return 0
    # cv2.imshow('a', thresh)
    # cv2.waitKey(0)

def draw_rectangle(bgr_img, box):
    img_height, img_width = bgr_img.shape[:2]
    pt1 = (box.x, box.y)
    pt2 = (min(box.x + box.w, img_width), min(box.y + box.h, img_height))
    crop_img = bgr_img.copy()
    crop_img = crop_img[pt1[1] : pt2[1], pt1[0] : pt2[0], :]
    cv2.rectangle(
        img = bgr_img, 
        pt1 = pt1, 
        pt2 = pt2,
        color = (0, 0, 255),
        thickness = 2
    )
    return bgr_img, crop_img

def do_something(scheduler): 
    print('Running ')

    window_name = GetWindowText(GetForegroundWindow())
    
    if window_name == WINDOW_NAME:
        im = ImageGrab.grab()
        dt = datetime.now()
        save_path = f"{SAVE_PATH}/pic_{dt.year}_{dt.month}_{dt.day}_{dt.hour}_{dt.minute}_{dt.second}.jpg"
        print(save_path)
        im.save(save_path)

        rgb_img = np.array(ImageGrab.grab())
        bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
        gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)

        bgr_img, map_box = draw_rectangle(bgr_img = bgr_img, box = MAP_BOX)
        bgr_img, all_box = draw_rectangle(bgr_img = bgr_img, box = ALL_BOX)
        
        all_box_check = detect_all_box(all_box)
        print(bgr_img.shape)
        # cv2.imshow(WINNAME1, all_box)
        # cv2.waitKey(0)
        
    # schedule the next call first
    scheduler.enter(DELAY, 1, do_something, (scheduler,))

if __name__ == '__main__':

    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(DELAY, 1, do_something, (my_scheduler,))
    my_scheduler.run()