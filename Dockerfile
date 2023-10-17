FROM docker.io/python:3.12.0-slim-bookworm

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="My ChRIS Plugin" \
      org.opencontainers.image.description="A ChRIS plugin to do something awesome"


WORKDIR /usr/local/src/chris-timer-plugin

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["commandname"]
