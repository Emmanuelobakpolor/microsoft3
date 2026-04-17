# Gunicorn configuration for Azure App Service
import multiprocessing

# Bind to Azure's expected port
bind = "0.0.0.0:8000"

# Worker configuration
max_requests = 1000
max_requests_jitter = 50
timeout = 230

# Calculate optimal workers based on CPU count
num_cpus = multiprocessing.cpu_count()
workers = (num_cpus * 2) + 1

# Thread configuration - use threads for better concurrency
worker_class = "gthread"
threads = 1 if num_cpus == 1 else 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Process naming
proc_name = "gunicorn"

# Server socket
backlog = 2048