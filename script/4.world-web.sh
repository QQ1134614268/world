echo "# 先编译
FROM node:14.15.0-slim AS myBuildImg
# 添加源码
# RUN echo '开始添加源码'
COPY . /root/web
WORKDIR /root/web
RUN npm install
RUN npm run build-ggok

# 部署
FROM nginx:1.23.3
COPY --from=myBuildImg /root/web/dist /usr/share/nginx/html/
CMD nginx -g 'daemon off;'" > web.dockerfile

docker build -t web:1.0 -f web.dockerfile .

# 配置文件
docker run -itd --name world-web  -p 8010:80 --privileged=true --restart=always web:1.0
