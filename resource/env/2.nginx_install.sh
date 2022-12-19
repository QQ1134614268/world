echo "
user root;
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

    server {
        listen       80;
        listen  [::]:80;
        server_name  localhost;

        #access_log  /var/log/nginx/host.access.log  main;
        location /api/ {
            proxy_pass  http://localhost:9090/api/;
        }

        location / {
            root   /root/lvying/web/;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    }
}
">/etc/nginx/nginx.conf

docker stop nginx && docker rm nginx

docker run --name nginx -p 80:80  \
  -v /etc/nginx/nginx.conf:/etc/nginx/nginx.conf  \
  -v /var/log/nginx:/var/log/nginx \
  -v /root/lvying/web/:/root/lvying/web/ \
  --privileged=true \
  --restart=always \
  -d nginx

curl http://127.0.0.1