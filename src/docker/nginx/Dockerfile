
FROM nginx:1.24.0-alpine 

RUN rm /etc/nginx/conf.d/default.conf 

COPY default.conf /etc/nginx/conf.d/default.conf

# docker run -d --name dj-app-lb-nginx -p 80:80 --network demo-lb-network lb-nginx:v1 
