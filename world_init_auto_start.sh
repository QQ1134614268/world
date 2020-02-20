# 下载代码
mkdir /app
git clone  https://gitee.com/biaozhun/world.git /app

pip3.7 install -r /app/world/requirements.txt

python3.7 /app/world/src/manage.py db upgrade

# 启动服务
nohup python3.7 /app/world/src/app.py &

# 添加开机自启
cp /app/world/world_auto_start.service /etc/systemd/system/world_auto_start.service
systemctl enable world_auto_start.service
