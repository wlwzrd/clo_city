"""gunicorn WSGI server configuration."""

from multiprocessing import cpu_count

def max_workers():
    return cpu_count()

command = '/opt/clo_sites/bin/gunicorn'
pythonpath = '/opt/clo_sites/clo_city'
bind = '127.0.0.1:8001'
#user = nobody
#max_requests = 2000
#worker_class = 'gevent'
workers = max_workers()
