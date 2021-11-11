import pytesseract as pytesseract
import re
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text=pytesseract.image_to_string(Image.open(r'invoice6.png'))
# print(text)
text=text.replace(',','')
num = re.findall(r'\d+\.\d+', text)
print(num)
    # num.sort()
maxamount = max(num,key=lambda x:float(x))
# list1 = sorted(num1, key=float)
if len(num) == 0:
    print('invoice cant be read')
else:
    print('The invoice amount is ' +maxamount)
# a=list1[len(list1)-1]
# print(a)


