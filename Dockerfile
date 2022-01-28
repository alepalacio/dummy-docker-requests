FROM python:3.9.5-slim-buster

WORKDIR /opt/app/

COPY requirements.txt /opt/app/

RUN apt-get -q -y update\
    && pip install --upgrade pip\
    && pip install -r requirements.txt

COPY . /opt/app/

CMD [ "python","api.py" ]