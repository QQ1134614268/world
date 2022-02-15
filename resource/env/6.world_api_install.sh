git_dir = $PWD/world

python3 -m venv /path/to/new/virtual/environment
cd  $PWD/world
git pull
# 日志目录

python3 -m venv /path/to/new/virtual/environment
docker run  -v $PWD/world:$PWD/world  -w $PWD/world python:3.5 python -m venv $PWD/world/venv
docker run  -v $PWD/world:$PWD/world  -w $PWD/world python:3.5 pip install -r requirements.txt
docker run  -v $PWD/world:$PWD/world  -w $PWD/world python:3.5 pip install -r requirements.txt
