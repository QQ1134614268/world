# 下载代码
cd /
mkdir app
cd /app
git clone  https://gitee.com/biaozhun/world.git

cd /app/world
pip3.7 install -r requirements.txt

# 同步数据库表结构 TODO 创建数据库
cd /app/world/src
python3.7 manage.py db upgrade

# 启动服务
nohup python3.7 /app/world/src/app.py &

# 添加开机自启
cp /app/world/world_auto_start.service /etc/systemd/system/world_auto_start.service
systemctl enable world_auto_start.service
