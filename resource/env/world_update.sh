cd  /app/world
git pull
cd
# git --git-dir /app/world/.git pull
pip3.7 install -r /app/world/requirements.txt  >> /var/log/world_install.log
cd  /app/world/src
/usr/local/python3.7/bin/flask db upgrade

pkill -f "python3.7 /app/world/src/app.py"
nohup python3.7 /app/world/src/app.py >>/var/log/world.log 2>&1 &

cd  /app/world/web
npm install >> /var/log/world_web_install.log
pkill -f "node /app/world/web"
nohup npm run production >>/var/log/world_web.log 2>&1 &
