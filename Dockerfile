FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN apt-get install joblib -y

RUN pip install -U pytest

RUN pip install flask

COPY . .

CMD python3 app.py