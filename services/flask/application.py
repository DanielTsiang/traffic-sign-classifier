from pathlib import Path
from flask import Flask, flash, redirect, render_template, request
from flask_session import Session
from tempfile import mkdtemp
import base64
import cv2
import numpy as np
import random
import os

import model

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Define global configs
SAMPLE_PATH = os.path.join(Path(__file__).parent.resolve(), "static", "sample")


@app.before_request
def before_request():
    # If http is requested then redirect to https
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
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
        random_filename = random.choice(os.listdir(SAMPLE_PATH))
        with open(os.path.join(SAMPLE_PATH, random_filename), "rb") as file:
            file_bytes = file.read()
        # Get image file extension
        extension = os.path.splitext(random_filename)[1]

    # Upload button was hit
    else:
        # Read bytes from uploaded file
        uploaded_file = request.files["file"]

        # Check if user hit upload button without uploading a file
        if uploaded_file.filename == "":
            # User did not upload a file
            flash("Please upload a file before hitting the upload button", "info")
            return render_template("index.html", classes=model.CLASSES)

        # User uploaded a file, read bytes and get file extension
        file_bytes = uploaded_file.stream.read()
        extension = os.path.splitext(uploaded_file.filename)[1]

    # Convert image into base64 string
    base64_image = base64.b64encode(file_bytes).decode("ascii")

    # Decode image into NumPy array and get prediction from model
    image = cv2.imdecode(np.frombuffer(file_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
    prediction = model.get_prediction(image)

    # Get results from response and return `result.html`
    if isinstance(prediction, tuple):
        # Valid response
        class_name, confidence = prediction

        response = {
            "prediction": "Predicted Class: " + class_name,
            "confidence": "Confidence Score: " + str(confidence),
            "image_base64": base64_image,
            "image_extension": extension
        }

        flash("Success", "success")
    else:
        # Invalid response
        response = {
            "prediction": "Error: " + prediction,
            "image_extension": extension
        }
        if image is not None:
            response["image_base64"] = base64_image

        flash("Error", "danger")

    return render_template("result.html", result=response)
