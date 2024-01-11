import base64
import random
from pathlib import Path
from tempfile import mkdtemp

import cv2
import model
import numpy as np
from flask import Flask, flash, redirect, render_template, request
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies), and secure cookies
app.config.update(
    SESSION_FILE_DIR=mkdtemp(),
    SESSION_PERMANENT=False,
    SESSION_TYPE="filesystem",
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="Lax",
)
Session(app)

# Define global configs
SAMPLE_PATH = Path(__file__).parent.resolve() / "static" / "sample"


@app.before_request
def before_request():
    # If http is requested then redirect to https
    if request.headers.get("X-Forwarded-Proto") == "http":
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)


@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"

    # Configure HTTP security headers
    response.headers[
        "Strict-Transport-Security"
    ] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    # User reached via GET request
    if request.method == "GET":
        return render_template("index.html", classes=model.CLASSES)

    # User reached via POST request
    # Check if random button was hit
    if request.form["action"] == "random":
        # Get random sample image and read image bytes
        random_filename = random.choice(list(SAMPLE_PATH.iterdir()))
        with open((SAMPLE_PATH / random_filename).as_posix(), "rb") as file:
            file_bytes = file.read()
        # Get image file extension
        extension = random_filename.suffix

    # Upload button was hit
    else:
        # Read bytes from uploaded file
        uploaded_file = request.files["file"]

        # Check if user hit upload button without uploading a file
        if uploaded_file.filename == "":
            # User did not upload a file
            flash("Please choose a file before hitting the upload button", "info")
            return render_template("index.html", classes=model.CLASSES)

        # User uploaded a file, read bytes and get file extension
        file_bytes = uploaded_file.stream.read()
        extension = Path(uploaded_file.filename).suffix

    # Convert image into base64 string
    base64_image = base64.b64encode(file_bytes).decode("ascii")

    # Decode image into NumPy array and get prediction from model
    image = (
        cv2.imdecode(np.frombuffer(file_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
        if file_bytes
        else None
    )
    prediction = model.get_prediction(image)

    # Get results from response and return `result.html`
    if isinstance(prediction, tuple):
        # Valid response
        class_name, confidence = prediction

        response = {
            "prediction": f"Predicted Class: {class_name}",
            "confidence": f"Confidence Score: {str(confidence)}",
            "image_base64": base64_image,
            "image_extension": extension,
        }

        flash("Success", "success")
    else:
        # Invalid response
        response = {"prediction": f"Error: {prediction}", "image_extension": extension}
        if image is not None:
            response["image_base64"] = base64_image

        flash("Error", "danger")

    return render_template("result.html", result=response)
