FROM python:3.11

WORKDIR /Users/dami/local

COPY . ./docker

EXPOSE 8081

RUN useradd d
USER d

CMD ["python", "docker/xdd.py"]

