FROM python:3.8.13-slim-bullseye

USER 0

WORKDIR /workspace

ADD  . .

RUN apt-get update && apt-get install -y vim curl

RUN pip install -r requirements.txt

CMD [ "python", "producer.py" ]