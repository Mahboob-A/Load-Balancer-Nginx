
# NOTE: add "make" before the commands. 



# Create the netwotk, and necessary images first. 
# Create the Bridge network 
lb-network:
	docker network create demo-lb-network

# Create the image for the Django app. Go to: src/docker/ and RUN: make app-img-create 
app-img-create: 
	docker build -t lb-api-img:v1 .. 


# Create the image for the Nginx. Go to: src/docker/nginx and RUN: docker build -t lb-nginx . 
nginx-img-create:
	docker run -d --name dj-app-lb-nginx -p 80:80 --network demo-lb-network lb-nginx:v1 


# Using the Docker Compose 
# cd to src: 
docker-up: 
	docker compose -p lb-ngnx-docker up --build -d --remove-orphans

# cd to src: 
docker-down: 
	docker compose -p lb-ngnx-docker down


# By Manual process. 
# Spawn Containers 
# cd to src. Spawn the Django and Nginx containers. 
app-01: 
	docker run -d --name dj-app-01 -p 5001:5000 --network demo-lb-network lb-api-img:v1

app-02:
	docker run -d --name dj-app-02 -p 5001:5000 --network demo-lb-network lb-api-img:v1

app-03:
	docker run -d --name dj-app-03 -p 5002:5000 --network demo-lb-network lb-api-img:v1

# The nginx container. 
lb-nginx-app: 
	docker run -d --name lb-nginx-app -p 80:80 --network demo-lb-network lb-nginx:v1 


# ## Stop Containers 
app-01-down: 
	docker stop dj-app-01 

app-02-down: 
	docker stop dj-app-02

app-03-down: 
	docker stop dj-app-03

lb-nginx-down: 
	docker stop lb-nginx-app