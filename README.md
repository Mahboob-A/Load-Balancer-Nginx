# Load-Balancer-Nginx

## Load Balancer with Nginx Practical Implementation with Docker as well as AWS and Other Experiments 

- I will continue to add various Load Balancer related practical experiments. 

- In this section, I have implemented a simple LB POC with Docker. 


<br>

### Instructions 

- Please clone the repository 

- cd to `src`

#### Using Docker Compose 

- Check Makefile to create the Network first and also the images if you want to spawn the containers manually instead of using docker-compose. 

- once the network is created, you can run `make docker-up` and the project will be up and running. 

- you can see more on: `src/docker/nginx/default.conf` for more details. 

###############################################################


#### Manual Mode 

- you can also perform the manual mode. 

- after creating the network, also create the necessary images. see Makefile for instructions. 

- then you can run the `make` commands one by one to see the demonstration. 


- Then visit: `127.0.0.1/app/test` to see the output. 

- NOTE that you need to install `Makefile` if you do not have it in your system. If you're a Windows user, then you can copy the commands in the `Makefile`and run it directly. 


### Round Robin 
![lb-ngx-dock-round-robin](https://github.com/user-attachments/assets/f1de38b5-3bc3-4917-b9e7-ed9a9869bf05)

<br><br>

### Weighted Round Robin 
- Three servers. Traffic distributed as: 3, 2, 1
- See more on: https://github.com/Mahboob-A/Load-Balancer-Nginx-Docker/blob/main/src/docker/nginx/Dockerfile

![lb-ngx-dock-weighted-round-robin](https://github.com/user-attachments/assets/0bdedec3-6f83-4ce6-9010-ec864f96f44c)
