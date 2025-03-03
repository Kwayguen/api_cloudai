
# creer image docker
docker build . -t ynov-api

# start docker container
docker run -p 8000:8000 -e PORT=8000 -v "$(pwd):/home/app" -it ynov-api


