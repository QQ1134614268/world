#!/bin/bash
# 数据库认证
user="root"
password="123456"
host="127.0.0.1"
db_name="world"
# 其它
backup_path="/root/backup/mysql"
date=$(date +"%d-%b-%Y")
# 设置导出文件的缺省权限
umask 177
# Dump数据库到SQL文件
mysqldump --user=$user --password=$password --host=$host $db_name > $backup_path/$db_name-$date.sql

# 删除30天之前的就备份文件
find $backup_path/* -mtime +30 -exec rm {} \;

# chmod 777 /root/world_db_backup.sh
# vim /var/spool/cron/root
# 0 5 * * * /root/world_db_backup.sh

# sed XXX