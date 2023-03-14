FROM python:3.10-slim-buster

WORKDIR /app

COPY main.py ./

CMD [ "python3", "./main.py" ]