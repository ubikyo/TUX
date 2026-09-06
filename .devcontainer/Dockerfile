FROM ubuntu:26.04

ENV LANG=C.UTF-8

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        python3 \
        python3-venv \
        sudo \
    && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
