from contextlib import contextmanager
from flask import template_rendered
from http import HTTPStatus
from io import BytesIO
from pathlib import Path
import base64
import cv2
import numpy as np
import os
import random
import unittest

from application import app
import model

# Define global configs
SAMPLE_PATH = os.path.join(Path(__file__).parents[1].resolve(), "static", "sample")


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


class AppTestCase(unittest.TestCase):
    def test_index(self):
        # GIVEN
        with app.test_client() as test_client:
            with captured_templates(app) as templates:
                # WHEN
                response = test_client.get("/")
                template, context = templates[0]

        # THEN
        self.assertEquals(HTTPStatus.OK, response.status_code)
        self.assertEquals("index.html", template.name)
        self.assertEquals(model.CLASSES, context["classes"])

    def test_valid_upload(self):
        # GIVEN
        # Get random sample image and read image bytes
        random_filename = random.choice(os.listdir(SAMPLE_PATH))
        with open(os.path.join(SAMPLE_PATH, random_filename), "rb") as file:
            file_bytes = file.read()

        # Get image file name and extension
        file_name = os.path.splitext(random_filename)[0]
        extension = os.path.splitext(random_filename)[1]

        # Convert image into base64 string
        base64_image = base64.b64encode(file_bytes).decode("ascii")

        # Create payload for POST request to app
        payload = {
            "file": (BytesIO(file_bytes), random_filename),
            "action": "upload"
        }

        with app.test_client() as test_client:
            with captured_templates(app) as templates:
                # WHEN
                response = test_client.post("/", data=payload)
                template, context = templates[0]
                result = context["result"]

        # THEN
        self.assertEquals(HTTPStatus.OK, response.status_code)
        self.assertEquals("result.html", template.name)
        self.assertEquals("Predicted Class: " + model.CLASSES[int(file_name)], result["prediction"])
        self.assertEquals("Confidence Score: 1.0", result["confidence"])
        self.assertEquals(base64_image, result["image_base64"])
        self.assertEquals(extension, result["image_extension"])

    def test_unknown_upload(self):
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
        payload = {
            "file": (BytesIO(image_bytes), file_name),
            "action": "upload"
        }

        with app.test_client() as test_client:
            with captured_templates(app) as templates:
                # WHEN
                response = test_client.post("/", data=payload)
                template, context = templates[0]
                result = context["result"]

        # THEN
        self.assertEquals(HTTPStatus.OK, response.status_code)
        self.assertEquals("result.html", template.name)
        self.assertEquals("Error: Unknown image", result["prediction"])
        self.assertEquals(base64_image, result["image_base64"])
        self.assertEquals(extension, result["image_extension"])

    def test_invalid_upload(self):
        # GIVEN
        # Create invalid image
        image = "invalid"
        image_bytes = str.encode(image)

        # Set image file name and extension
        file_name = "invalid.jpg"
        extension = ".jpg"

        # Create payload for POST request to app
        payload = {
            "file": (BytesIO(image_bytes), file_name),
            "action": "upload"
        }

        with app.test_client() as test_client:
            with captured_templates(app) as templates:
                # WHEN
                response = test_client.post("/", data=payload)
                template, context = templates[0]
                result = context["result"]

        # THEN
        self.assertEquals(HTTPStatus.OK, response.status_code)
        self.assertEquals("result.html", template.name)
        self.assertEquals("Error: Invalid image uploaded", result["prediction"])
        self.assertEquals(extension, result["image_extension"])

    def test_random(self):
        # GIVEN
        # Create payload for POST request to app
        payload = {
            "action": "random"
        }

        with app.test_client() as test_client:
            with captured_templates(app) as templates:
                # WHEN
                response = test_client.post("/", data=payload)
                template, context = templates[0]
                result = context["result"]

        # THEN
        self.assertEquals(HTTPStatus.OK, response.status_code)
        self.assertEquals("result.html", template.name)
        self.assertIn("Predicted Class:", result["prediction"])
        self.assertEquals("Confidence Score: 1.0", result["confidence"])
        self.assertIn("image_base64", result)
        self.assertIn("image_extension", result)


if __name__ == "__main__":
    unittest.main()
