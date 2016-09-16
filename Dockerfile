FROM ubuntu:xenial

RUN apt-get update

RUN apt-get -y -q install python3

RUN mkdir -p /application

COPY test.py /application/

COPY test1 /application/test1

WORKDIR /application/

ENTRYPOINT ["python3", "test1/application.py"]

#CMD python3 test1/application.py

