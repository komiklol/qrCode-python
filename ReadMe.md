# QR Code Generator - Flask Application

This project is a simple Python web application created using the Flask framework. The application allows users to generate QR codes using various routes and methods.

## What is it for?

This application serves as a QR Code generator that provides flexibility in how QR codes are created and consumed. It supports a range of features:

1. **Dynamic QR Code Generation**: Generate QR codes directly via API routes or HTML forms.
2. **Multiple API Versions**:
   - Version 1: Basic QR code generation and return as a Base64 image.
   - Version 2: QR code generation using a custom class and rendered as HTML.
   - Version 3: Form-based interaction for QR code creation using templates.
   - Version 4: Similar to version 2, but cleaner output using the custom class.
3. **Simple Sum Endpoint**: A basic feature to demonstrate Flask routing and parameter handling.

---

## How to Use It

### 1. Clone the Repository

Clone this project into your working directory:

```shell script
git clone <repository_url>
cd <project_directory>
```

### 2. Set Up the Environment

It is recommended to use a virtual environment for this project. Follow these steps:

```shell script
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages, install Flask and qrcode library:

```shell script
pip install Flask qrcode[pil]
```

### 4. Run the Application

Start the Flask server:

```shell script
flask -app test_app.py run
```

The Flask application will start and be accessible by default on `http://127.0.0.1:5000`.

---

### Routes and Usage

1. **Home Route** (`/`):  
   Displays a "Hello World!" message.

2. **Sum Route** (`/sum/<int:a>/<int:b>`):  
   Example: `/sum/10/5`  
   Returns the sum of `a` and `b`.

3. **QR Code Generation (API v1)** (`/api/v1/qr/generate/<string:data>`):  
   Generates a QR code for the given `<data>` and returns it as an embedded image.  
   Example: `/api/v1/qr/generate/HelloWorld`.

4. **QR Code Generation (API v2)** (`/api/v2/qr/generate/<string:data>`):  
   Generates a QR code using the `cQRCode` class and returns the HTML representation.  
   Example: `/api/v2/qr/generate/HelloWorld`.

5. **Form-Based QR Code (API v3)** (`/api/v3/qr/template/`):  
   A form to submit text and generate a QR code. Accessible via a template-based HTML page.  
   Example: Access this route via browser and submit the form.

6. **QR Code Generation (API v4)** (`/api/v4/qr/generate/<string:data>`):  
   Another implementation of generating QR codes using `cQRCode` and returning the HTML representation.

---

## What to Install?

This project is based on the following dependencies:

- **Flask**: A lightweight web framework for Python. ([Flask Documentation](https://flask.palletsprojects.com/en/stable/))
- **qrcode**: Library for creating QR codes. ([qrcode Documentation](https://github.com/lincolnloop/python-qrcode))
- **Pillow**: Required by `qrcode` for image generation. It is installed via `qrcode[pil]`.

Install all dependencies using the following command:

```shell script
pip install Flask qrcode[pil]
```

---

## References

The project is inspired by the [Flask Quickstart Guide](https://flask.palletsprojects.com/en/stable/quickstart/).

Enjoy using the QR Code Generator Flask App! 🚀