# 先编译
FROM node:14.15.0-slim AS myBuildImg
# 添加源码
# RUN echo '开始添加源码'
COPY . /root/web
# RUN cd /root/web
WORKDIR /root/web
# RUN npm -g install npm@7.19.1
RUN npm install --force
RUN npm run build

# 部署
FROM nginx:1.23.3
#copy jar from the first stage
COPY --from=myBuildImg /root/web/dist /usr/share/nginx/html/
CMD nginx -g 'daemon off;'
