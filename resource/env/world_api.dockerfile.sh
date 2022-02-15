docker build -t world_api:1.1.0 -f world_api.dockerfile .
# log
docker run --name world_api:1.1.0 --restart=always -p 8010:8010 -v /var/mongo/data:/data -d world_api:1.1.0
