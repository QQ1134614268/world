#!/bin/bash
# 数据库认证
db_name='world'
# 其它
backup_path='/var/mysql_backup'
log_path='/var/log/world_back_mysql.log'
curr_date=$(date '+%Y-%m-%d_%H:%M:%S')

echo $curr_date '--开始同步' >> $log_path
# Dump数据库到SQL文件
mysqldump --defaults-extra-file=/etc/my.cnf $db_name > $backup_path/$db_name-$curr_date.sql

# 删除30天之前的就备份文件
find $backup_path/* -mtime +30 -exec rm {} \;
echo $curr_date '--同步结束'  >> $log_path
