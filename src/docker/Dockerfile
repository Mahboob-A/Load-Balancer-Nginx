
FROM python:3.12-slim-bullseye

ARG APP_HOME=/use/src/app

COPY requirements/base.txt /tmp/requirements/base.txt 

RUN pip install --no-cache-dir  -r /tmp/requirements/base.txt 

RUN rm /tmp/requirements/base.txt

WORKDIR ${APP_HOME}

COPY . . 

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]

# docker build -t lb-api-img:v1 .. 

# docker run -d --name dj-app-03 -p 5002:5000 --network demo-lb-network lb-api-img:v1
