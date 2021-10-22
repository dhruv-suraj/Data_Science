import cv2
import pytesseract as pytesseract
from PIL import Image

def ocr(img):
    text=pytesseract.image_to_string(img)
    return text
img=cv2.imread('imvoice1.png')
def grey(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

img=grey(img)
print(ocr(img))

