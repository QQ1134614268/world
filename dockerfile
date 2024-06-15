FROM python:3.7.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY src/* .
RUN mkdir -p data/upload_file && mkdir -p data/log
EXPOSE 9090
CMD python app.py
# docker build -t world_serve .
# docker run -d --name world_serve -p 9090:9090 -v /app/world_serve/data:/app/data --restart=always world_serve
