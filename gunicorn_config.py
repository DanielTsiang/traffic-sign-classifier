import warnings
from os import getenv as env

warnings.filterwarnings("ignore")

# App level
# The port to bind.
port = int(env("PORT", 8000))

# The socket to bind.
bind = env("GUNICORN_BIND", f"0.0.0.0:{port}")
