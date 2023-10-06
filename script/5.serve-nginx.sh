# web 独立nginx?
# 多个web 独立部署
echo "
# user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '\$remote_addr - \$remote_user [\$time_local] \"\$request\" '
                      '\$status \$body_bytes_sent \"\$http_referer\" '
                      '\"\$http_user_agent\" \"\$http_x_forwarded_for\"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80;
        server_name  renren.ggok.top;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
          proxy_pass http://\$host:30180;
        }

        location /api/ {
          proxy_pass http://\$host:30190/api/;
        }
    }

    server {
        listen       80;
        server_name  worker.ggok.top;
        root         /usr/share/nginx/html;

        location / {
          proxy_pass http://\$host:30180;
        }

        location /api/ {
          proxy_pass http://\$host.top:30190/;
        }
    }
}
">/etc/nginx/nginx.conf

docker run --name nginx -p 80:80  \
  -v /etc/nginx/nginx.conf:/etc/nginx/nginx.conf  \
  -v /var/log/nginx:/var/log/nginx \
  -d nginx
