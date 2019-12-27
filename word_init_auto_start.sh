# 下载代码
cd /
mkdir app
cd /app
git clone  https://gitee.com/biaozhun/world.git

# 启动服务
cd world
pip3 install -r requirements.txt
nohup python3 /app/world/src/main/python/app.py &

# 添加开机自启
cp /app/world/word_auto_start.service /etc/systemd/system/word_auto_start.service
systemctl enable word_auto_start.service
