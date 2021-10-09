echo "==========================================="
echo "removing containers"
echo "==========================================="
docker rm -vf $(docker ps -a -q)
echo "==========================================="
echo "removing images"
echo "==========================================="
docker rmi -f $(docker images -a -q)
echo "==========================================="
echo "all containers (must be empty)"
echo "==========================================="
docker ps -a
echo "==========================================="
echo "all images (must be empty)"
echo "==========================================="
docker image ls