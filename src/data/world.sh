echo 'cd  /app/world
git pull
cd
# git --git-dir /app/world/.git pull
nohup pip3.7 install -r /app/world/requirements.txt  &
cd  /app/world/src
python3.7 manage.py db upgrade

pkill -f "python3.7 /app/world/src/app.py"
nohup python3.7 /app/world/src/app.py &


cd /app/world_web
git pull
npm install
pkill -f "node /app/world_web"
nohup npm run production >/dev/null 2>&1 &
cd
'>world_update.sh

chmod +x world_update.sh