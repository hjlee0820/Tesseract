import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'H:\Programming\Programs\Tesseract-OCR\tesseract.exe'

a = Image.open('영수증.jpg')
result = pytesseract.image_to_string(a, lang='kor')
print(result)

result.split()
