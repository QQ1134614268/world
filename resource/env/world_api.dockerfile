FROM ajouz/python3.7
WORKDIR $PWD/world
#还是git?
ADD $PWD/world .
# 虚拟的有必要?
RUN python -m venv $PWD/world/venv
# 软连接
RUN $PWD/world/venv/script/pip install -r requments.txt
RUN $PWD/world/venv/script/flask  db upgrade
CMD nohup python3.7 /app/world/src/app.py &
#运行dockerfile,构建镜像
# docker build -t 镜像名:tag -f dockerfile .
# docker run --name mongo --restart=always -p 27017:27017  -v /var/mongo/data:/data -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root1234567890 -d mongo:4.2.5

#查看镜像的 dockerflie
#docker inspect 镜像名