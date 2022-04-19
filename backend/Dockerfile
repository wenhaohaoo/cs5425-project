FROM python:3.8.13-slim-buster

WORKDIR /workdir

ADD . .

RUN apt-get update && apt-get install -y vim curl wget

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
