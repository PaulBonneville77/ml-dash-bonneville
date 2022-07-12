FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip install flask

COPY . .

CMD python3 app.py