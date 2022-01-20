from pathlib import Path
import cv2
import numpy as np
import os
import tensorflow as tf
import unittest


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        self.valid_images = [".jpg"]
        self.directory = os.path.join(Path(__file__).parents[1], "static", "sample")
        self.image_width = 30
        self.image_height = 30
        self.model = tf.keras.models.load_model(
            os.path.join(Path(__file__).parents[1], "model", "1")
        )

    def test_model(self):
        for filename in os.listdir(self.directory):
            with self.subTest(filename=filename):
                file_number = os.path.splitext(filename)[0]
                extension = os.path.splitext(filename)[1]
                if extension.lower() not in self.valid_images:
                    continue

                # GIVEN
                # Load valid images into memory and preprocess them into format TensorFlow model expects
                loaded_image = cv2.imread(os.path.join(self.directory, filename), cv2.IMREAD_COLOR)
                resized_image = cv2.resize(loaded_image, (self.image_width, self.image_height))
                expanded_image = np.expand_dims(resized_image, axis=0)

                # WHEN
                prediction = self.model.predict(expanded_image)

                # THEN
                # Get top prediction index and compare with expected value
                top_prediction_index = prediction[0].argsort()[::-1][0]
                error_message = f"Expected {file_number} but got {top_prediction_index} instead."
                self.assertEqual(int(file_number), int(top_prediction_index), error_message)


if __name__ == "__main__":
    unittest.main()
