import PIL
from datetime import datetime
import cv2
import numpy as np
import sched, time
from win32gui import GetWindowText, GetForegroundWindow
from collections import namedtuple
import pyautogui
import pyscreeze
import win32gui

BOX = namedtuple('Box', ['x', 'y', 'w', 'h'])
POINT = namedtuple('Point', ['x', 'y'])

WINDOW_NAME = 'Cửu Âm Chân Kinh  CACK-Vô Danh Kiếm'
WINNAME1 = 'Source'
SAVE_PATH = 'image'
DELAY = 1 # 1 second
SCALE_PERCENT = 30
MAP_BOX = BOX(x = 1410, y = 65, w = 160, h = 160)
PICK_ALL_BOX = BOX(x = 1090, y = 560, w = 95, h = 35)
PRACTICE_BOX = BOX(x = 650, y = 625, w = 300, h = 55)
CENTER_MAP = POINT(x = 1493, y = 143)

def center_of_box(box):
    x = box.x + box.w // 2
    y = box.y + box.h // 2
    return (x, y)

def detect_green(bgr_image):
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    # define range of green color in HSV
    lower_green = np.array([20, 100, 50])
    upper_green = np.array([90, 255, 255])

    # create a mask for green color
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)

    return mask_green

def detect_PICK_ALL_BOX(bgr_img):
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)
    white_pixels = np.sum(thresh == 255)
    
    if 0:
        print(f'White pixels: {white_pixels}') 
        cv2.imshow('', thresh)
        cv2.waitKey(0)

    if white_pixels > 220:
        return 1
    else:
        return 0
    

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

def draw_circle(bgr_img, pt):
    x, y = pt
    bgr_img = cv2.circle(bgr_img, (x, y), radius = 2, color = (0, 0, 255), thickness=-1)
    return bgr_img

def load_template():
    template = []
    classes = ['up', 'down', 'left', 'right', 'j', 'k']
    for class_name in classes:
        file_name = f'template_image/{class_name}.jpg'
        image = cv2.imread(filename = file_name)
        assert image is not None, 'Error file path'
        template.append((image, class_name))
    return template



def do_something(scheduler): 
    print('Running ...')

    window_name = GetWindowText(GetForegroundWindow())
    
    if window_name == WINDOW_NAME:
        
        if 1:
            im = PIL.ImageGrab.grab()
            dt = datetime.now()
            save_path = f"{SAVE_PATH}/pic_{dt.year}_{dt.month}_{dt.day}_{dt.hour}_{dt.minute}_{dt.second}.jpg"
            print(save_path)
            im.save(save_path)

        rgb_img = np.array(im)
        bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
        gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)

        bgr_img, map_box = draw_rectangle(bgr_img = bgr_img, box = MAP_BOX)
        bgr_img, pick_all_box = draw_rectangle(bgr_img = bgr_img, box = PICK_ALL_BOX)
        bgr_img = draw_circle(bgr_img = bgr_img, pt = CENTER_MAP)
        

        '''
            List of user choice:
                0 : auto pick herbs
                1 : auto practice
        '''

        user_choice = 1
        if user_choice == 0:
            pick_all_box_check = detect_PICK_ALL_BOX(pick_all_box)
            if pick_all_box_check:
                x, y = CENTER_PICK_ALL_BOX
                pyautogui.click(x, y)
            else:
                x, y = CENTER_MAP
                pyautogui.click(x, y)
        
        elif user_choice == 1:
            pass

        if 0:
            cv2.imshow(WINNAME1, bgr_img)
            cv2.waitKey(0)
    
    if 1:
        bgr_img = cv2.imread(f'{SAVE_PATH}/pic_2023_6_4_14_20_16.jpg')
        bgr_img, practice_box = draw_rectangle(bgr_img = bgr_img, box = PRACTICE_BOX)
        templ_img, class_name = TEMPLATE[2]
        gray = cv2.cvtColor(practice_box.copy(), cv2.COLOR_BGR2GRAY)
        locations = pyscreeze.locateAll(templ_img, practice_box)
    
        for location in locations:
            print(type(location))
        cv2.imshow(WINNAME1, practice_box)
        cv2.waitKey(0)

    # schedule the next call first
    scheduler.enter(DELAY, 1, do_something, (scheduler,))

if __name__ == '__main__':

    CENTER_PICK_ALL_BOX = center_of_box(PICK_ALL_BOX)
    TEMPLATE = load_template()
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(DELAY, 1, do_something, (my_scheduler,))
    my_scheduler.run()