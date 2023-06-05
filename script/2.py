import glob
import cv2
from collections import namedtuple

BOX = namedtuple('Box', ['x', 'y', 'w', 'h'])

PRACTICE_BOX = BOX(x = 650, y = 625, w = 300, h = 55)
SRC_PATH = 'image'
SAVE_PATH = 'image/practice_box'

def crop_box(img, box):
    img_height, img_width = img.shape[:2]
    pt1 = (box.x, box.y)
    pt2 = (min(box.x + box.w, img_width), min(box.y + box.h, img_height))
    crop_img = img.copy()
    crop_img = crop_img[pt1[1] : pt2[1], pt1[0] : pt2[0], :]
    
    return crop_img

for path in glob.glob(f'{SRC_PATH}/*.jpg'):
    file_name = path.split('\\')[-1]
    print(file_name)
    img = cv2.imread(path)
    crop = crop_box(img, PRACTICE_BOX)
    cv2.imwrite(f'{SAVE_PATH}/{file_name}', crop)