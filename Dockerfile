FROM docker.io/python:3.12.0-slim-bookworm

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="ChRIS Timer Plugin" \
      org.opencontainers.image.description="A ChRIS plugin that outputs the execution time of main script."

ARG SRCDIR=/usr/local/src/app
WORKDIR ${SRCDIR}

COPY requirements.txt .
RUN --mount=type=cache,sharing=private,target=/root/.cache/pip pip install -r requirements.txt

COPY . .
ARG extras_require=none
RUN pip install ".[${extras_require}]" \
    && cd / && rm -rf ${SRCDIR}
WORKDIR /

CMD ["commandname"]