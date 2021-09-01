from PIL import Image
import io
from pytesseract import pytesseract
from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def resolver():
    if request.method == 'POST':
        try:
            img = Image.open(io.BytesIO(base64.b64decode(request.form.get('data'))))
            text = ocr_result = pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            return text[:5]
        except:
            return None
        
    else:
        return "GET REQUESTED!"
    

