FROM python:3
RUN apt-get update && apt-get upgrade -y
RUN apt-get install sqlite3
RUN mkdir /app
EXPOSE 8000
WORKDIR /app
COPY /app/ /app/
RUN pip3 install -r /app/requirements.txt
RUN chmod u+x entrypoint.sh
ENTRYPOINT sh entrypoint.sh