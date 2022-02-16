docker pull nginx
# conf 相对路径
cp ../conf/nginx.conf /etc/nginx/nginx.conf
docker run -d --name nginx -d -p 80:80  -v /etc/nginx/nginx.conf:/etc/nginx/nginx.conf  -v /var/log/nginx:/var/log/nginx nginx
