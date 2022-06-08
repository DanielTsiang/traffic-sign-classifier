# Traffic Sign Classifier

## Description
A single-page web app serving a Machine Learning model which classifies traffic signs.

This Flask app is served by Gunicorn.

The Machine Learning model is a Convoluted Neural Network (CNN) trained by myself using the TensorFlow library.
See [here](https://github.com/DanielTsiang/CS50ai/tree/main/project5/traffic) for more details on how I trained this CNN.

## Getting Started
1. Visit the web application [here](https://traffic-sign-classifier-dt.herokuapp.com/).
2. Note that the app may take up to 30 seconds to load as it wakes up from automatic sleep if it hasn't been used in a while.

### Video Demostration
https://user-images.githubusercontent.com/74436899/151076061-8875ae51-8c43-4dea-b9bd-9bed501bf234.mp4

### Running locally in Docker
1. Ensure you have Docker installed.
2. To build and start the app, in the root folder where `Dockerfile` is contained, run the following command in the terminal:
`docker build -t traffic . && docker run --rm --publish 8000:8000 --name traffic traffic`
3. Visit `localhost:8000` in your web browser.
4. To shut down the app, in the terminal hit `CTRL+C`.

### Running locally with Python
1. In the root folder where `requirements.txt` is contained, run `pip install -r requirements.txt` in the terminal to install the requirements for this project.
2. To start the app, in the root folder, run the following command in the terminal:
`gunicorn -c gunicorn_config.py wsgi:app`
3. Visit `localhost:8000` in your web browser.
4. To shut down the app, in the terminal hit `CTRL+C`.

### Testing
To run the unit tests, in the root folder, run the following in the terminal:
```
sh tests/test.sh
```

## Specification
* Design and build a single-page web app to serve a Machine Learning model I trained.
* Serve the Python Flask app with Gunicorn.
* Flask web app is run in a Docker Container.
* Users can upload their own images or select a random image for the model to classify.
* Uploaded images are not stored by the web app. Files are checked to determine if they are valid images.
* Dismissible messages are displayed to the user to notify machine learning inference success or error.
* Front-end is styled using the Bootstrap CSS framework, crafting a mobile-friendly layout.
* Using JavaScript, users can search and sort the information displayed in the table.

### Technologies Used
* Docker
* Python with Flask framework & OpenCV library
* TensorFlow
* HTML
* CSS with Bootstrap framework
* JavaScript with DataTables library
