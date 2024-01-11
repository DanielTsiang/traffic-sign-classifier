import base64
import random
from contextlib import contextmanager
from http import HTTPStatus
from io import BytesIO

import cv2
import numpy as np
import pytest
from conftest import *
from flask import template_rendered

from services.flask import model
from services.flask.application import app


@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_index():
    # GIVEN
    with app.test_client() as test_client:
        with captured_templates(app) as templates:
            # WHEN
            response = test_client.get("/")
            template, context = templates[0]

    # THEN
    assert response.status_code == HTTPStatus.OK
    assert template.name == "index.html"
    assert context["classes"] == model.CLASSES


def test_valid_upload():
    # GIVEN
    # Get random sample image and read image bytes
    random_filename = random.choice(list(SAMPLE_PATH.iterdir()))
    with open((SAMPLE_PATH / random_filename).as_posix(), "rb") as file:
        file_bytes = file.read()

    # Get image file name and extension
    file_name = random_filename.stem
    extension = random_filename.suffix

    # Convert image into base64 string
    base64_image = base64.b64encode(file_bytes).decode("ascii")

    # Create payload for POST request to app
    payload = {"file": (BytesIO(file_bytes), random_filename), "action": "upload"}

    with app.test_client() as test_client:
        with captured_templates(app) as templates:
            # WHEN
            response = test_client.post("/", data=payload)
            template, context = templates[0]
            result = context["result"]

    # THEN
    assert response.status_code == HTTPStatus.OK
    assert template.name == "result.html"
    assert result["prediction"] == f"Predicted Class: {model.CLASSES[int(file_name)]}"
    assert result["confidence"] == "Confidence Score: 1.0"
    assert result["image_base64"] == base64_image
    assert result["image_extension"] == extension


def test_unknown_upload():
    # GIVEN
    # Create blank black image
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    # Encode image into data stream and get image bytes
    image_encoded = cv2.imencode(".jpg", image)[1]
    image_bytes = image_encoded.tobytes()

    # Set image file name and extension
    file_name = "blank.jpg"
    extension = ".jpg"

    # Convert image into base64 string
    base64_image = base64.b64encode(image_bytes).decode("ascii")

    # Create payload for POST request to app
    payload = {"file": (BytesIO(image_bytes), file_name), "action": "upload"}

    with app.test_client() as test_client:
        with captured_templates(app) as templates:
            # WHEN
            response = test_client.post("/", data=payload)
            template, context = templates[0]
            result = context["result"]

    # THEN
    assert response.status_code == HTTPStatus.OK
    assert template.name == "result.html"
    assert result["prediction"] == "Error: Unknown image"
    assert result["image_base64"] == base64_image
    assert result["image_extension"] == extension


def test_invalid_upload():
    # GIVEN
    # Create invalid image
    image = "invalid"
    image_bytes = str.encode(image)

    # Set image file name and extension
    file_name = "invalid.jpg"
    extension = ".jpg"

    # Create payload for POST request to app
    payload = {"file": (BytesIO(image_bytes), file_name), "action": "upload"}

    with app.test_client() as test_client:
        with captured_templates(app) as templates:
            # WHEN
            response = test_client.post("/", data=payload)
            template, context = templates[0]
            result = context["result"]

    # THEN
    assert response.status_code == HTTPStatus.OK
    assert template.name == "result.html"
    assert result["prediction"] == "Error: Invalid image uploaded"
    assert result["image_extension"] == extension


def test_random():
    # GIVEN
    # Create payload for POST request to app
    payload = {"action": "random"}

    with app.test_client() as test_client:
        with captured_templates(app) as templates:
            # WHEN
            response = test_client.post("/", data=payload)
            template, context = templates[0]
            result = context["result"]

    # THEN
    assert response.status_code == HTTPStatus.OK
    assert template.name == "result.html"
    assert "Predicted Class:" in result["prediction"]
    assert result["confidence"] == "Confidence Score: 1.0"
    assert "image_base64" in result
    assert "image_extension" in result


if __name__ == "__main__":
    import subprocess

    try:
        subprocess.run(["docker-compose", "up", "-d"])
        pytest.main()
    finally:
        subprocess.run(["docker-compose", "down"])
