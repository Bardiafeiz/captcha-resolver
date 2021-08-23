from PIL import Image
import io
from pytesseract import pytesseract
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def resolver():
    if request.method == 'POST':
        img = Image.open(io.BytesIO(request.data))
        
        text = ocr_result = pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
           
        return text[:5]
        
    else:
        return "GET REQUESTED"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

