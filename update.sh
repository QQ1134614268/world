# mkdir /app
# cd /app
# git clone https://gitee.com/biaozhun/world
# cd world
# /usr/local/python3.7.5/bin/pip install python3-venv
# /usr/local/python3.7.5/bin/python -m venv venv_world
# venv_world/bin/pip install --upgrade pip
cd  /app/world
git pull
# git --git-dir /app/world/.git pull
venv_world/bin/pip install -r /app/world/requirements.txt  >> /var/log/world_install.log
cd  /app/world/src
venv_world/bin/flask db upgrade

pkill -f "/app/world/src/app.py"
nohup venv_world/bin/python /app/world/src/app.py >>/var/log/world.log 2>&1 &

cd /app/world/web
npm install >> /var/log/world_web_install.log
# pkill -f "node /app/world/web"
#nohup npm run production >>/var/log/world_web.log 2>&1 &
# nohup npm run local >>/var/log/world_web.log 2>&1 &
npm run build-production
