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

docker exec traffic python3 -m pip install -r requirements_test.txt

echo "======= Running unit tests ======="
docker exec traffic python3 -m unittest discover -s /tests -p "test*"

echo "======= Cleaning up Docker ======="
docker stop traffic
