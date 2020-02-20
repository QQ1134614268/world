git --git-dir /app/world/.git pull
nohup pip3.7 install -r requirements.txt  &

python3.7 /app/world/src/manage.py db upgrade

# 启动服务
pkill -f "python3.7 /app/world/src/app.py"
nohup python3.7 /app/world/src/app.py &
