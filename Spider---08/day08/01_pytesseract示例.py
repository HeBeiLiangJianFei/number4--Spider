import pytesseract
from PIL import Image

image = Image.open("test1.jpg")
string = pytesseract.image_to_string(image)
print(string)






