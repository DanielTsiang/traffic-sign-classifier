FROM tensorflow/serving

ENV MODEL_BASE_PATH /models
ENV MODEL_NAME traffic-sign-classifier
ENV PORT 8501

COPY ./model/ /models/traffic-sign-classifier/
COPY ./model.config /models/model.config
