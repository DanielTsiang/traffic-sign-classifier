# Traffic Sign Classifier

[![Traffic Sign Classifier](https://img.shields.io/website-up-down-green-red/https/danieltsiang.github.io.svg)](https://traffic-sign-classifier-ztlt.onrender.com/)
[![Test App Status](https://github.com/DanielTsiang/traffic-sign-classifier/actions/workflows/test-app.yml/badge.svg?branch=main)](https://github.com/DanielTsiang/traffic-sign-classifier/actions?query=branch%3Amain)
[![GitHub branches](https://badgen.net/github/branches/DanielTsiang/traffic-sign-classifier?&kill_cache=1)](https://github.com/DanielTsiang/traffic-sign-classifier/branches)
[![Known Vulnerabilities](https://snyk.io/test/github/DanielTsiang/traffic-sign-classifier/badge.svg?targetFile=services/flask/requirements.txt)](https://snyk.io/test/github/DanielTsiang/traffic-sign-classifier?targetFile=services/flask/requirements.txt)
[![Profile views](https://gpvc.arturio.dev/traffic-sign-classifier)](https://gpvc.arturio.dev/traffic-sign-classifier)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Buymeacoffee](https://badgen.net/badge/icon/buymeacoffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/dantsiang8)

## Description
A single-page web app serving a machine learning model which classifies traffic signs.

This Flask app is served by Gunicorn with NGINX as the reverse proxy.

The Machine Learning model is a Convoluted Neural Network (CNN) trained by myself using the TensorFlow library.
See [here](https://github.com/DanielTsiang/CS50ai/tree/main/project5/traffic) for more details on how I trained this CNN.

## Getting Started
1. Visit the web application [here](https://traffic-sign-classifier-ztlt.onrender.com/).
2. Note that the app may take up to 30 seconds to load as it wakes up from automatic sleep if it hasn't been used in a while.

### Video Demo
https://user-images.githubusercontent.com/74436899/151076061-8875ae51-8c43-4dea-b9bd-9bed501bf234.mp4

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

## Technologies Used
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?logo=TensorFlow&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?logo=opencv&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?logo=gunicorn&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?logo=nginx&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?logo=javascript&logoColor=%23F7DF1E)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?logo=githubactions&logoColor=white)
![Dependabot](https://img.shields.io/badge/dependabot-025E8C?logo=dependabot&logoColor=white)

* Docker with Docker Compose
* TensorFlow with TensorFlow Serving
* Python with Flask framework & OpenCV library
* Gunicorn
* NGINX
* HTML5
* CSS with Bootstrap framework
* JavaScript with DataTables library
* GitHub Actions workflows for CI to automate running tests via Docker Compose
* Dependabot to keep dependencies up to date and mitigate security vulnerabilities

## Running locally
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
