# Traffic Sign Classifier

## Description
A single-page web app serving a machine learning model which classifies traffic signs.

This Flask app is served by Gunicorn with NGINX as the reverse proxy.

The Machine Learning model is a Convoluted Neural Network (CNN) trained by myself using the TensorFlow library.
See [here](https://github.com/DanielTsiang/CS50ai/tree/main/project5/traffic) for more details on how I trained this CNN.

## Getting Started
1. Visit the web application [here](https://traffic-sign-classifier-dt.herokuapp.com/).
2. Note that the app may take up to 30 seconds to load as it wakes up from automatic sleep if it hasn't been used in a while.

### Video Demo
https://user-images.githubusercontent.com/74436899/151076061-8875ae51-8c43-4dea-b9bd-9bed501bf234.mp4

### Running locally
1. Ensure you have Docker installed.
2. To start the app, in the root folder where `docker-compose.yml` is contained, run `docker-compose up` in the terminal.
3. Visit `localhost:1337` in your web browser. Bypass the invalid SSL certificate warning.
E.g. in Chrome, click on the screen with the page open and type `thisisunsafe` to bypass the warning.
4. If you are unable to bypass the warning, checkout the `non-ssl` branch instead to run the Docker
containers without SSL enforced. In this branch, visit `localhost` instead.
5. To shut down the app, run `docker-compose down` in the terminal or hit `CTRL+C`.

### Testing
To run the integration tests, in the root folder, run the following in the terminal:
```
sh tests/test.sh
```

## Specification
* Design and build a single-page web app to serve a Machine Learning model I trained.
* Serve the Python Flask app with Gunicorn and use NGINX as the reverse proxy. Customise NGINX config to force SSL.
* Serve the TensorFlow model using TensorFlow Serving for optimal performance and managing model versioning.
* Flask, NGINX and TensorFlow Serving Docker containers are orchestrated using Docker Compose.
* Users can upload their own images or select a random image for the model to classify.
* Uploaded images are not stored by the web app. Files are checked to determine if they are valid images.
* Dismissible messages are displayed to the user to notify machine learning inference success or error.
* Front-end is styled using the Bootstrap CSS framework, crafting a mobile-friendly layout.
* Using JavaScript, users can search and sort the information displayed in the table.

### Technologies Used
* Docker with Docker Compose
* Python with Flask framework & OpenCV library
* TensorFlow with TensorFlow Serving
* NGINX
* HTML
* CSS with Bootstrap framework
* JavaScript with DataTables library
