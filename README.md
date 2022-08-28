# Traffic Sign Classifier

[![Traffic Sign Classifier](https://img.shields.io/website-up-down-green-red/https/danieltsiang.github.io.svg)](https://traffic-sign-classifier-dt.onrender.com/)
[![Test app status](https://github.com/DanielTsiang/traffic-sign-classifier/actions/workflows/test-python-app.yml/badge.svg?branch=deploy)](https://github.com/DanielTsiang/traffic-sign-classifier/actions/workflows/test-python-app.yml)
[![GitHub branches](https://badgen.net/github/branches/DanielTsiang/traffic-sign-classifier?&kill_cache=1)](https://github.com/DanielTsiang/traffic-sign-classifier/branches)
[![Security](https://snyk.io/test/github/DanielTsiang/traffic-sign-classifier/deploy/badge.svg)](https://snyk.io/test/github/DanielTsiang/traffic-sign-classifier/deploy)
[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Ftraffic-sign-classifier-dt.onrender.com%2F&label=Hits&countColor=%2337d67a&style=flat)](https://visitorbadge.io/status?path=https%3A%2F%2Ftraffic-sign-classifier-dt.onrender.com%2F)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Buymeacoffee](https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-orange.svg?style=flat&logo=buymeacoffee)](https://www.buymeacoffee.com/dantsiang8)

## Description
A single-page web app serving a machine learning model which classifies traffic signs.

This Flask app is served by Gunicorn.

The Machine Learning model is a Convoluted Neural Network (CNN) trained by myself using the TensorFlow library.
See [here](https://github.com/DanielTsiang/CS50ai/tree/main/project5/traffic) for more details on how I trained this CNN.

## Getting Started
1. Visit the web application [here](https://traffic-sign-classifier-dt.onrender.com/).

### Video Demo
https://user-images.githubusercontent.com/74436899/151076061-8875ae51-8c43-4dea-b9bd-9bed501bf234.mp4

## Specification
* Design and build a single-page web app to serve a Machine Learning model I trained.
* Serve the Python Flask app with Gunicorn.
* Flask web app is run in a Docker Container.
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
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?logo=javascript&logoColor=%23F7DF1E)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?logo=githubactions&logoColor=white)
![Dependabot](https://img.shields.io/badge/dependabot-025E8C?logo=dependabot&logoColor=white)
![Render](https://img.shields.io/badge/render-46E3B7.svg?logo=render&logoColor=white)

* Docker
* TensorFlow
* Python with Flask framework & OpenCV library
* Gunicorn
* HTML5
* CSS with Bootstrap framework
* JavaScript with DataTables library
* GitHub Actions workflows for CI to automate running tests via a Docker container
* Dependabot to keep dependencies up to date and mitigate security vulnerabilities
* Render for deployment

## Running locally
### Docker
1. Ensure you have Docker installed.
2. To build and start the app, in the root folder where `Dockerfile` is contained, run the following command in the terminal:
`docker build -t traffic . && docker run --rm --publish 8000:8000 --name traffic traffic`
3. Visit `localhost:8000` in your web browser.
4. To shut down the app, in the terminal hit `CTRL+C`.

#### Testing
To run the unit tests, in the root folder, run the following in the terminal:
```
sh tests/test.sh
```

### Python
1. In the root folder where `requirements.txt` is contained, run `pip install -r requirements.txt` in the terminal to install the requirements for this project.
2. To start the app, in the root folder, run the following command in the terminal:
`gunicorn --log-config logging.conf -c gunicorn_config.py wsgi:app`
3. Visit `localhost:8000` in your web browser.
4. To shut down the app, in the terminal hit `CTRL+C`.

#### Testing
In the root folder, run the following in the terminal to install the test requirements and then run the unit tests:
```
pip3 install -r requirements_test.txt
python3 -m unittest discover -s /tests -p "test*"
```
