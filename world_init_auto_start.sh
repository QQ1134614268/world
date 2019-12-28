# 下载代码
cd /
mkdir app
cd /app
git clone  https://gitee.com/biaozhun/world.git

# 同步数据库表结构
python3 /app/world/src/main/python/manage.py db init
python3 /app/world/src/main/python/manage.py db migrate
python3 /app/world/src/main/python/manage.py db upgrade

# 启动服务
cd world
pip3 install -r requirements.txt
nohup python3 /app/world/src/main/python/app.py &

# 添加开机自启
cp /app/world/world_auto_start.service /etc/systemd/system/world_auto_start.service
systemctl enable world_auto_start.service
