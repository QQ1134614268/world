echo 'cd  /app/world
git pull
cd
# git --git-dir /app/world/.git pull
pip3.7 install -r /app/world/requirements.txt  > /var/log/world.log
cd  /app/world/src
python3.7 manage.py db upgrade

pkill -f "python3.7 /app/world/src/app.py"
nohup python3.7 /app/world/src/app.py &


cd  /app/world/web
npm install >> /var/log/world.log
pkill -f "node /app/world/web"
nohup npm run production >/dev/null 2>&1 &
'>world_update.sh

chmod +x world_update.sh