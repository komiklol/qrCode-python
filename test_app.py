from flask import Flask, render_template, request
import class_qrcode

app = Flask(__name__)

# Here you can find different versions of my approach to generate QR Codes with the QR-Library.
# The Max Size fo the QR Code:
# Only Numbers:
# - 7.089 Chars.
# Alphanumerical:
# - 4.296 Chars.
# Binary (8-Bit Bytes):
# - 2.953 Bytes.

# Default route, returns a simple hello world message
@app.route("/")
def hello():
    return "<p>Hello World!<p>"


# Route to calculate the sum of two integers
@app.route('/sum/<int:a>/<int:b>')
def summ(a, b):
    return f"<p>The sum of {a} and {b} is {a + b}<p>"


# Route to generate a QR code and return it as a base64-encoded image (API v1)
@app.route('/api/v1/qr/generate/<string:data>')
def qr_generate(data):
    import qrcode, io, base64

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code and generate the image
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Encode the QR code image into base64
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")

    # Return the image as a base64 string
    return f'<img src="data:image/png;base64,{img_base64}" />'


# Route to generate a QR code using the cQRCode class and return its HTML representation (API v2)
@app.route('/api/v2/qr/generate/<string:data>')
def qr_generate_v2(data):
    cQrC = class_qrcode.cQRCode(data)
    return cQrC.generateHTML()


# Route to display a form for QR code generation using a template (API v3)
@app.route('/api/v3/qr/template/', methods=['GET', 'POST'])
def index(data=None):
    qr_code_img = None

    # If method is POST, generate the QR code based on the form data
    if request.method == 'POST':
        data = request.form.get('text_data')
        if data:
            qr = class_qrcode.cQRCode(data)
            qr_code_img = qr.generate()

    # Render the template with the generated QR code image
    return render_template("index.html", qr_code_image=qr_code_img)


# Route to generate a QR code using the cQRCode class and return its HTML representation (API v4)
@app.route('/api/v4/qr/generate/<string:data>')
def qr_generate_v4(data):
    return class_qrcode.cQRCode(data).generateHTML()
