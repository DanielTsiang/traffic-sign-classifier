FROM tensorflow/serving

ENV MODEL_BASE_PATH /models
ENV MODEL_NAME traffic-sign-classifier
ENV PORT 8501

COPY ./model/ /models/traffic-sign-classifier
COPY ./model.config /models/

# Fix because base tf_serving_entrypoint.sh does not take $PORT env variable while $PORT is set by Heroku
# CMD is required to run on Heroku
COPY ./tf_serving_entrypoint.sh /usr/bin/tf_serving_entrypoint.sh
CMD ["/usr/bin/tf_serving_entrypoint.sh"]
