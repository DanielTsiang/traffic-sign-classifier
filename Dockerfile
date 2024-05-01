FROM python:3.11-slim

# Copy source code and set working directory
COPY . /app
WORKDIR /app

# Enable venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Start gunicorn
CMD ["gunicorn", "--log-config", "logging.conf", "-c", "gunicorn_config.py", "wsgi:app"]