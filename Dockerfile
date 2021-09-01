FROM python:3.8.2-alpine

WORKDIR /docker-flask-loginPage

ADD . /docker-flask-loginPage

RUN pip install -r requirement.txt

CMD ["python","app.py"]