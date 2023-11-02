import json
import os
from typing import Optional, Union

import cv2
import numpy as np
import requests

# Define global configs
SIZE = 30
CONFIDENCE_THRESHOLD = 0.988
CLASSES = [
    "Speed limit (20km/h)",
    "Speed limit (30km/h)",
    "Speed limit (50km/h)",
    "Speed limit (60km/h)",
    "Speed limit (70km/h)",
    "Speed limit (80km/h)",
    "End of speed limit (80km/h)",
    "Speed limit (100km/h)",
    "Speed limit (120km/h)",
    "No passing",
    "No passing vehicles over 3.5 metric tons",
    "Right-of-way at the next intersection",
    "Priority road",
    "Yield",
    "Stop",
    "No vehicles",
    "Vehicles over 3.5 tons prohibited",
    "No entry",
    "General caution",
    "Dangerous curve to the left",
    "Dangerous curve to the right",
    "Double curve",
    "Bumpy road",
    "Slippery road",
    "Road narrows on the right",
    "Road work",
    "Traffic signals",
    "Pedestrians",
    "Children crossing",
    "Bicycles crossing",
    "Beware of ice/snow",
    "Wild animals crossing",
    "End of speed and passing limits",
    "Turn right ahead",
    "Turn left ahead",
    "Ahead only",
    "Go straight or right",
    "Go straight or left",
    "Keep right",
    "Keep left",
    "Roundabout mandatory",
    "End of no passing",
    "End of no passing vehicles over 3.5 metrics tons",
]
TENSORFLOW_SERVING_HOST = os.environ.get("TENSORFLOW_SERVING_HOST", "localhost")
TENSORFLOW_SERVING_PORT = int(os.environ.get("TENSORFLOW_SERVING_PORT", "8501"))
MODEL_NAME = "traffic-sign-classifier"
MODEL_URI = f"http://{TENSORFLOW_SERVING_HOST}:{TENSORFLOW_SERVING_PORT}/v1/models/{MODEL_NAME}:predict"


def get_prediction(image: np.ndarray) -> Optional[Union[tuple[str, float], str]]:
    # If valid image received, preprocess it into format TensorFlow model expects
    if image is None:
        return "Invalid image uploaded"
    resized_image = cv2.resize(image, (SIZE, SIZE))
    expanded_image = np.expand_dims(resized_image, axis=0)

    # Create JSON payload that TensorFlow model expects
    data = json.dumps({"instances": expanded_image.tolist()})

    # Make POST request to model served by TensorFlow Serving
    response = requests.post(MODEL_URI, data=data.encode("utf-8"))
    prediction = np.array(response.json()["predictions"][0])

    # Get top prediction
    top_prediction_index = prediction.argsort()[::-1][0]

    # Get confidence score of top prediction
    confidence = prediction[top_prediction_index]

    if confidence > CONFIDENCE_THRESHOLD:
        # Get label of the top prediction i.e. class name
        top_prediction_label = CLASSES[top_prediction_index]
        return top_prediction_label, np.round(confidence, 2)

    return "Unknown image"
