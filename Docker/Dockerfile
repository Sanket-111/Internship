FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3

WORKDIR /app

COPY hello_world.py /app/

CMD ["python3", "hello_world.py"]
