# ref: https://github.com/microsoft/vscode-dev-containers/blob/main/containers/python-3/README.md
# version full list: https://mcr.microsoft.com/v2/vscode/devcontainers/python/tags/list
ARG VARIANT=3.11-bookworm
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

RUN apt update \
    && apt install -y --no-install-recommends \
    apt-utils \
    gcc \
    build-essential \
    locales-all \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ=Asia/Tokyo
