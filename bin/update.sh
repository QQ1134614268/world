cd /root/workspace/world/web
git pull
docker build -t world_web .
docker stop world_web && docker rm world_web
docker run -d --name world_web -p 18100:80 -v /app/world_web/data/log:/var/log/nginx --restart=always world_web

cd /root/workspace/world
git pull
docker build -t world_serve .
docker stop world_serve && docker rm world_serve
docker run -d --name world_serve -p 19100:19100 -v /app/world_serve/data/upload_file:/app/data/upload_file -v /app/world_serve/data/log:/app/data/log --restart=always world_serve


cd /root/workspace/VueProjects/Jiangxin
git pull
docker build -t jiangxin_web .
docker stop jiangxin_web && docker rm jiangxin_web
docker run -d --name jiangxin_web -p 18200:80 -v /app/jiangxin_web/data/log:/var/log/nginx --restart=always jiangxin_web

cd /root/workspace/TemplateBoot/JiangXin
git pull
docker build -t jiangxin_serve .
docker stop jiangxin_serve && docker rm jiangxin_serve
docker run -d --name jiangxin_serve -p 19200:19200 -v /app/jiangxin_serve/data/upload:/app/data/upload -v /app/jiangxin_serve/data/log:/app/data/log --restart=always jiangxin_serve
