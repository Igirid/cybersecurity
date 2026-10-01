docker -v
docker pull redis
docker pull redis
docker inspect redis --format='{{.NetworkSettings.Ports}}'
docker stop redis
docker run -d --name redis -p 6379:6379 redis:latest
docker ps -a | findstr redis
docker rm redis && docker run -d --name redis -p 6379:6379 redis:latest
docker rm redis
docker run -d --name redis -p 6379:6379 redis:latest
docker ps | findstr redis
docker run -d --name redis-server -p
docker ps
docker info
docker compose version
docker version
docker login
docker info
docker pull [imageName]
docker run [imageName]
docker run -d [imageName] #background
docker start [containerName] #startContainer
docker ps #listRunningContainers
docker ps -a #list running and stopped containers
docker stop [containerName] #stop container
docker kill [containerName] #kill container
docker image inspect [imageName] #get image info
docker run --memory="256m" [imageName] #set max memory
docker run --cpus=".5" [imageName] #set max cpu
docker run --publish 80:80 --name webserver nginx #pull and run an
nginx server
docker ps -a #list running and stopped containers
docker start nginx #startContainer
docker start webserver #startContainer
docker stop webserver #stop container
docker rm webserver #remove container from memory
docker rm webserver #remove container from memory
Get-Content (Get-PSReadlineOption).HistorySavePath | Select-String
"docker"
Get-Content (Get-PSReadlineOption).HistorySavePath | Select-String
"docker" #search history for docker commands
docker run -it nginx -- /bin/bash #attach shell
docker run -it nginx -- microsoft/powershell:nanoserver #attach
powershell
docker run -it nginx -- microsoft/powershell:nanoserver pwsh.exe
#attach powershell
docker container exec -it webserver -- bash #attach to a running
container
docker ps
docker ps -a
docker rm $(docker ps -a -q) #removes all stopped container from memory
docker ps -a
docker images
docker images #list images
docker rmi [imageName] #delete an image
docker system prune -a #removes all images not in use by any containers
 docker run -d -p 8080:80 --name webserver nginx
docker ps
docker images #list images
docker container exec -it webserver -- bash #attach to a running 
container
Get-Content (Get-PSReadlineOption).HistorySavePath | Select-String 
"docker" #search history for docker commands
$ docker container exec -it webserver bash #attach to a running
container
docker container exec -it webserver bash #attach to a running container
docker container exec -it webserver bash #attach to a running container
docker stop webserver #stop container
docker rm webserver #stop container
docker rmi nginx
docker build -t [name:tag] #builds an image using a Dockerfile located
in the same folder
docker build -t [name:tag] -f [fileName] #builds an image using a
Dockerfile locaed in a different folder
docker tag [imageName] [name:tag] #tag an existing image
docker build -t [name:tag] . #builds an image using a Dockerfile
located in the same folder
docker build -t [name:tag] . #builds an image using a Dockerfile
located in the same folder
docker run -d -p 8080:80 webserver-image:v1 webserver
Get-Content (Get-PSReadlineOption).HistorySavePath | Select-String
"docker" #search history for docker commands
docker run -d -p 8080:80 webserver-image:v1 --name webserver
docker run -p 8080:80 webserver-image:v1 --name webserver
docker build -t number-of-islands:v1 .
docker rmi number-of-islands:v1
docker images
docker build -t number_of_islands:v1 .
docker run --name noi number_of_islands:v1
docker ps
docker images
docker rmi number_of_islands:v1
Get-Content (Get-PSReadlineOption).HistorySavePath | Select-String
"docker" #search history for docker commands

docker ps -a --filter name=noi --format '{{.Names}}: {{.Status}}'
