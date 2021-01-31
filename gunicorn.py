# debug = True
loglevel = 'debug'
bind = "0.0.0.0:9090"
pidfile = "data/log/gunicorn.pid"
accesslog = "data/log/gunicorn_access.log"
errorlog = "data/log/debug.log"
daemon = True

# 启动的进程数
workers = 2
x_forwarded_for_header = 'X-FORWARDED-FOR'
