FROM python:3.7.13-slim
# 复制源码
COPY . /root/lvying/world-api
# 更新pip.
# RUN /usr/local/bin/python -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
# 安装依赖; 优化依赖(800M), 去掉不用的, 删减功能 MongoDB等;  docker history <镜像名>”，查看每个层的大小; todo
RUN pip install -r /root/lvying/world-api/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 兼容cv2, 参考 https://blog.csdn.net/weixin_42990464/article/details/125203404
RUN pip install opencv-python-headless -i https://mirrors.aliyun.com/pypi/simple/
# 更新数据库
RUN cd /root/lvying/world-api/src/ && /usr/local/bin/python/bin/flask db upgrade
EXPOSE 9090
# CMD python -m cd /root/lvying/world-api/src/app.py # bug no module named app todo
CMD cd /root/lvying/world-api/src/ && python app.py
