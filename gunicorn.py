# debug = True
loglevel = 'debug'
bind = "0.0.0.0:9090"
pidfile = "/var/log/gunicorn.pid"
accesslog = "/var/log/gunicorn_access.log"
errorlog = "/var/log/debug.log"
daemon = True

# 启动的进程数
workers = 2
x_forwarded_for_header = 'X-FORWARDED-FOR'
