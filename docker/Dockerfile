FROM ubuntu:16.10
RUN apt-get update && apt-get install -y python-pip wget
RUN pip install mapnik
RUN mkdir /build
VOLUME /build
WORKDIR /build
CMD ./build.sh
