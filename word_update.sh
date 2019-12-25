cd /app/world
git pull
pip3 install -r requirements.txt
pkill -f "python3 /app/world/src/main/python/app.py"
nohup python3 /app/world/src/main/python/app.py &
