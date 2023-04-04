import os
from PIL import Image, ImageTk, ImageGrab
from configuration import SCALER
import cv2

class controller():
    def __init__(self) -> None:
        pass
    
    def load_PhotoImages(self, *arg):
            folderPath = os.path.join(os.path.dirname(__file__), 'pages\icon')
          
            photoImages = []
            for fileName, max_dim in arg:
                filePath = os.path.join(folderPath, fileName)
                # print(filePath)
                photoImage = self.create_PhotoImage(filePath = filePath, max_dim = max_dim)
                photoImages.append(photoImage)
            return photoImages
            
    def create_PhotoImage(self, filePath, max_dim):
        img = Image.open(filePath)
        w, h = img.size
        max_edge = max(w, h)
        scale = max_dim / max_edge
        photoSize = (round(w * scale), round(h * scale))
        resized_img = img.resize(photoSize)
        return ImageTk.PhotoImage(image = resized_img)

    def update_image(self, grandparent):
        try:
            temp_path = os.path.join(os.path.dirname(__file__), 'TempImage\img1.jpg')
            
            im = ImageGrab.grabclipboard() # Get image from clipboard
            im.save(temp_path) # save image to temp folder
            temp_img = self.create_PhotoImage(filePath = temp_path, max_dim = 500)
            grandparent.src_img = temp_img
            return 1
        except:
            return 0
                       
if __name__ == '__main__':
    pass
