import os
from pathlib import Path

import cv2
import numpy as np
import pytest
import tensorflow as tf
from conftest import *

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Disable tensorflow debugging logs


@pytest.fixture(scope="module")
def model():
    return tf.keras.models.load_model(
        Path(__file__).parents[1].resolve()
        / "model"
        / "1"
    )


@pytest.mark.parametrize("file_name", list(SAMPLE_PATH.iterdir()))
def test_model(model, file_name):
    # GIVEN
    valid_images = [".jpg"]
    image_width = 30
    image_height = 30

    file_number = file_name.stem
    extension = file_name.suffix
    if extension.lower() not in valid_images:
        return

    # Load valid images into memory and preprocess them into format TensorFlow model expects
    loaded_image = cv2.imread((SAMPLE_PATH / file_name).as_posix(), cv2.IMREAD_COLOR)
    resized_image = cv2.resize(loaded_image, (image_width, image_height))
    expanded_image = np.expand_dims(resized_image, axis=0)

    # WHEN
    prediction = model.predict(expanded_image)

    # THEN
    # Get top prediction index and compare with expected value
    top_prediction_index = prediction[0].argsort()[::-1][0]
    assert int(top_prediction_index) == int(file_number)


if __name__ == "__main__":
    pytest.main([__file__])
