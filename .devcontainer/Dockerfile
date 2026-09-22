FROM ubuntu:26.04

ENV LANG=C.UTF-8

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        iproute2 \
        python3 \
        python3-venv \
        sudo \
        systemd \
        systemd-resolved \
        libpam-systemd \
    && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
