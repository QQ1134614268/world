cd /
mkdir app
cd /app
git clone  https://gitee.com/biaozhun/world.git
cd world
pip3 install -r requirements.txt
nohup python3 /app/world/src/main/python/app.py &

# 设置开机自启 https://www.jb51.net/article/176257.htm
cp word_update.sh  /etc/profile.d/word_update.sh
