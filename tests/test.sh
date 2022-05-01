# Run integration tests
echo "======= Starting Docker containers ======="
docker-compose up -d --build

echo "======= Running integration tests ======="
docker-compose run --rm \
  -e TF_CPP_MIN_LOG_LEVEL="3" \
  -v "$(pwd)/tests:/tests" \
  -v "$(pwd)/services:/services" \
  flask python3 -m unittest discover -s /tests -p "test*"

echo "======= Cleaning up Docker ======="
docker-compose down
