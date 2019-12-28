cd /app/world
git pull
nohup pip3 install -r requirements.txt  &
python3 /app/world/src/main/python/manage.py db migrate
python3 /app/world/src/main/python/manage.py db upgrade
pkill -f "python3 /app/world/src/main/python/app.py"
nohup python3 /app/world/src/main/python/app.py &
