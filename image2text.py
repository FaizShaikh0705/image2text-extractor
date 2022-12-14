from pytesseract import pytesseract
import os

class OCR:
    def __init__(self):
        self.path = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    def extract(self,filename):
        try:
            pytesseract.tesseract_cmd = self.path

            text = pytesseract.image_to_string(filename)
            return text
        except Exception as e:
            print(e)
            return "Error"

ocr = OCR()
text = ocr.extract("images/image2.jpeg")
print (text)