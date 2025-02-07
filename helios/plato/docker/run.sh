CONTAINER_NAME=plato
NGINX_PORT=8080
PORT=8002
docker run --privileged=true -d -it --rm -v /scratch/project/map:/tmp/map -v /work:/work -v /nfs:/nfs -p $PORT:8002 -p $NGINX_PORT:8080 --name $CONTAINER_NAME plato bash

docker exec -d $CONTAINER_NAME /tmp/map/helios/plato/start_nginx.sh
docker exec -d -u bsu $CONTAINER_NAME /tmp/map/helios/plato/start_plato.sh
