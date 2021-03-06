FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip install joblib

RUN pip install -U pytest

RUN pip install flask

RUN pip install -U scikit-learn

COPY . .

CMD python3 app.py