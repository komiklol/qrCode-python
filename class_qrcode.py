import qrcode, io, base64


class cQRCode:
    def __init__(self, data):
        # Initialize the QR code with provided data
        self.data = data

    def generateHTML(self):
        # Create a QRCode object with specified parameters
        qr = qrcode.QRCode(
            version=1,  # Version of the QR code (1 = smallest size)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each QR code box
            border=4,  # Border size around the QR code
        )
        qr.add_data(self.data)  # Add the data to be encoded in the QR code
        qr.make(fit=True)  # Adjust the size of the QR code automatically
        img = qr.make_image(fill_color="black", back_color="white")  # Generate the QR code image

        # Create an in-memory byte buffer to store the QR code image
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")  # Save the image in the buffer as a PNG file
        buffer.seek(0)  # Move back to the beginning of the buffer
        # Encode the image to base64 string for embedding in HTML
        img_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")
        # Return the HTML <img> tag with the base64 image data
        return f'<img src="data:image/png;base64,{img_base64}" />'

    def generate(self):
        # Create a QRCode object with specified parameters
        qr = qrcode.QRCode(
            version=1,  # Version of the QR code (1 = smallest size)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each QR code box
            border=4,  # Border size around the QR code
        )
        qr.add_data(self.data)  # Add the data to be encoded in the QR code
        qr.make(fit=True)  # Adjust the size of the QR code automatically
        img = qr.make_image(fill_color="black", back_color="white")  # Generate the QR code image

        # Create an in-memory byte buffer to store the QR code image
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")  # Save the image in the buffer as a PNG file
        buffer.seek(0)  # Move back to the beginning of the buffer
        # Encode the image to base64 string
        return base64.b64encode(buffer.getvalue()).decode("ascii")
