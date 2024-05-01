# Run unit tests
echo "======= Building Docker container ======="
docker build -t traffic .
docker run --rm -d --name traffic \
  -e TF_CPP_MIN_LOG_LEVEL="3" \
  -v "$(pwd)/tests:/tests" \
  -v "$(pwd)/model:/model" \
  -v "$(pwd)/static:/static" \
  traffic \
  > /dev/null  # redirect output excluding errors

echo "======= Running unit tests ======="
docker exec traffic python -m pytest tests/

echo "======= Cleaning up Docker ======="
docker stop traffic
