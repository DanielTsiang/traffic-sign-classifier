import warnings
from os import getenv as env
from multiprocessing import cpu_count

warnings.filterwarnings("ignore")

# App level
# The port to bind.
port = int(env("GUNICORN_PORT", "8000"))

# The socket to bind.
bind = env("GUNICORN_BIND", f"0.0.0.0:{port}")

# The number of worker processes that this serves
workers = int(env("GUNICORN_WORKERS", (2 * cpu_count()) + 1))

worker_tmp_dir = env("GUNICORN_WORKER_TMP_DIR", "/tmp")

# If a worker does not notify the master process in this number of seconds,
# it is killed and a new worker is spawned to replace it.
timeout = int(env("GUNICORN_TIMEOUT", 30))
