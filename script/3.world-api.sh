#if [ ! -f "$file" ]; then
#     echo "$file不存在"
#else
#   echo "$file已存在"
#fi

# git clone https://gitee.com/biaozhun/world.git

# 动态--安装目录, 打包环境, data目录; 修改localhost 127.0.0.1等

# 代码同级目录 链接??
cp world/world.dockerfile world.dockerfile

docker build -t world-api:1.0 -f world.dockerfile .

# 优化 环境变量 output目录清理; 挂载目录,log config upload todo
mkdir -m 666 -p /app/world/data/upload
mkdir -m 666 -p /app/world/data/log

docker run -it --name world \
  -v /app/world/data/upload:/root/lvying/world-api/world/data/upload \
  -v /app/world/data/log:/root/lvying/world-api/world/data/log \
  -p 9090:9090 \
  --privileged=true \
  --restart=always \
  -d world-api:1.0 /bin/bash -c "cd /root/lvying/world-api/src && python app.py"

# docker logs world
# docker stop world && docker rm world
