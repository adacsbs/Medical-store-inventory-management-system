import pytesseract
from PIL import Image
def scan_image(image_path):
    # Open the image file
    image = Image.open(image_path)  
    # Perform OCR using Tesseract
    output=pytesseract.image_to_string(image_path)  
    #print(output)
    return output
    
