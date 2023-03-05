FROM python:3.10-slim-buster

WORKDIR /home

COPY main.py ./

CMD [ "python3", "./main.py" ]