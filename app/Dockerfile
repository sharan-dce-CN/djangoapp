FROM python:3
RUN apt-get update && apt-get upgrade -y
RUN apt-get install sqlite3
RUN mkdir /app
EXPOSE 8000
EXPOSE 8080
WORKDIR /app
COPY /app/ /app/
RUN pip3 install -r /app/requirements.txt
RUN pip3 install -r /app/python-flask-server-generated/python-flask-server/requirements.txt
RUN chmod u+x entrypoint.sh
RUN chmod u+x swagger_entrypoint.sh
ENTRYPOINT sh entrypoint.sh