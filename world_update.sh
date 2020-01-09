cd /app/world
git pull
nohup pip3.7 install -r requirements.txt  &

cd /app/world/src
python3.7 manage.py db migrate
python3.7 manage.py db upgrade

# 启动服务
cd /app/world
pkill -f "python3.7 /app/world/src/app.py"
nohup python3.7 /app/world/src/app.py &
