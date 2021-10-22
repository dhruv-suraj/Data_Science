import pytesseract as pytesseract
import re
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text=pytesseract.image_to_string(Image.open(r'invoice6.png'))
# print(text)
num1 = re.findall(r'\d+\.\d+', text)
print(num1)
    # num.sort()
list1 = sorted(num1, key=float)
a=list1[len(list1)-1]
print(a)
# num2 = re.findall(r'\d+\,\d+\.\d+', text)
# if total==num1 or total==num2:
# or num=re.findall(r'\d+\.\d+\,\d+', text)