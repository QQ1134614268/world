cd  /app/world
git pull
cd
# git --git-dir /app/world/.git pull
nohup pip3.7 install -r /app/world/requirements.txt  &
pkill -f "python3.7 /app/world/src/app.py"
nohup python3.7 /app/world/src/app.py &


cd /app/world_web
git pull
npm install
cd
pkill -f "node /app/world_web"
nohup npm run production &
