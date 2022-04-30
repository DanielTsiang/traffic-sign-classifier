# Run integration git stests
echo "Starting Docker containers..."
docker-compose up -d

echo "Running integration tests..."
python3 -m unittest discover -s tests  -p "test*"

echo "Cleaning up Docker..."
docker-compose down
