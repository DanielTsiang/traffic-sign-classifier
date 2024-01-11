# Run integration tests
echo "======= Starting Docker containers ======="
docker build \
  -f ./services/flask/Dockerfile.flask \
  -t flask \
  ./services/flask/

docker-compose up -d

echo "======= Running integration tests ======="
docker-compose run --rm \
  -e TF_CPP_MIN_LOG_LEVEL="3" \
  -v "$(pwd)/tests:/tests" \
  -v "$(pwd)/services:/services" \
  flask python -m pytest tests/

echo "======= Cleaning up Docker ======="
docker-compose down
