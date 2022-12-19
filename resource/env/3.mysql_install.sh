#!/usr/bin/env bash
# rm -rf /etc/mysql
mkdir -m 644 -p /etc/mysql/conf
mkdir -m 644 -p /var/log/mysql
mkdir -m 644 -p /var/lib/mysql

echo '
[client]
port=3306
default-character-set=UTF8MB4
[mysql]
default-character-set=UTF8MB4
[mysqld]
character_set_server=UTF8MB4
max_connections=100

datadir=/var/lib/mysql

lower_case_table_names=0

performance_schema = OFF
innodb_buffer_pool_size = 8M
innodb_log_buffer_size = 1M
key_buffer_size = 0
' > /etc/mysql/conf/my.cnf

docker pull mysql:8.0.19

docker run  --name mysql \
-p 3306:3306 \
-v /etc/mysql/conf/my.cnf:/etc/mysql/my.cnf \
-v /var/lib/mysql-files:/var/lib/mysql-files \
-v /var/lib/mysql:/var/lib/mysql \
-v /var/log/mysql:/var/log/mysql \
-e MYSQL_ROOT_PASSWORD=1234567890 \
--privileged=true \
--restart=always \
-d mysql:8.0.19

sleep 20
docker exec -it mysql mysql -uroot -p1234567890 -e "
use mysql;
create user 'wg'@'%' identified with mysql_native_password by '123456';
grant all privileges on *.* to 'wg'@'%' with grant option;
flush privileges;"

docker stop mysql && docker rm mysql

# docker exec -it mysql mysql -uroot -p1234567890 -e "source /var/lib/mysql/sqlfile.sql"

# firewall-cmd --zone=public --add-port=3306/tcp --permanent
# firewall-cmd --reload
# systemctl restart docker
# systemctl restart firewalld
