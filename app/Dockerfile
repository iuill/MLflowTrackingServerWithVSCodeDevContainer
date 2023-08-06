# ---------------------------------------------------------------------------------------------
# NOTE:
# ベースのイメージは、mcr.microsoft.com か nvidia か 各ディストリ公式の選択肢がある。
# mcr.microsoft.com や 各ディストリの場合は、CUDA/cuDNNの導入が一苦労。
# とはいえ、nvidia/cudaのレイヤを見れば、導入はできると思われる。
# いずれのベースイメージを使うにせよ、CUDA/cuDNNの導入なり、
# Pythonやvscode common-utilsなりを個別に入れていくことになる。
# このDockerfileではnvidia/cudaをベースとするアプローチを採用する。
# ---------------------------------------------------------------------------------------------

# nvidia/cudaはdevelにしかnvccが無いらしいのでdevelにする
FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu22.04

# 高速化のためパッケージのリポジトリを日本にする
RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list


# ---------------------------------------------------
# VSCode setting
# ref: https://pc.atsuhiro-me.net/entry/2022/06/21/225400
# ---------------------------------------------------
# Options for setup script
ARG INSTALL_ZSH="false"
ARG UPGRADE_PACKAGES="true"
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 親ディレクトリから辿るパスの指定方法（docker-compose.yml側のcontextに注意）
# ref: https://qiita.com/mk-tool/items/1c7e4929055bb3b7aeda#%E7%8F%BE%E5%9C%A8%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%82%88%E3%82%8A%E3%82%82%E5%A4%96%E9%83%A8%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84
COPY ../.devcontainer/library-scripts/*.sh ../.devcontainer/library-scripts/*.env /tmp/library-scripts/
RUN yes | unminimize 2>&1 \ 
    && bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts


# ---------------------------------------------------
# 依存パッケージやデバッグ用ツールなど
# ---------------------------------------------------
RUN apt update \
    && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
    apt-utils \
    git \
    cmake \
    gcc \
    build-essential \
    libboost-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    wget \
    unzip \
    zlib1g \
    locales-all \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*


# ---------------------------------------------------
# python3.11
# ---------------------------------------------------
RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
    software-properties-common \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
    python3.11 \
    python3-pip

# ---------------------------------------------------
# pipを23.2.1以降にする
# lightGBM4.0.0でGPU用にビルドするのに必要っぽそう
# ※pipのバージョンが23.1.2だとビルドが途中で止まる
# ---------------------------------------------------
RUN pip install --upgrade pip==23.2.1 setuptools==68.0.0

# ---------------------------------------------------
# lightGBM
# ---------------------------------------------------
RUN pip install lightgbm==4.0.0 --no-binary lightgbm --no-cache lightgbm --config-settings=cmake.define.USE_CUDA=ON

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ=Asia/Tokyo
