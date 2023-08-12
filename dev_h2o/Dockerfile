# ---------------------------------------------------------------------------------------------
# NOTE:
# このDockerfileではnvidia/cudaをベースとするアプローチを採用し、H2O用環境を構成する
#
# ref: https://h2o-release.s3.amazonaws.com/h2o/rel-3.42.0/2/index.html
# ---------------------------------------------------------------------------------------------

# nvidia/cudaはdevelにしかnvccが無いらしいのでdevelにする
FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu22.04

# 高速化のためパッケージのリポジトリを日本にする
RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list


# ---------------------------------------------------
# VSCode common-utils
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
# 依存パッケージやビルド・デバッグ用ツールなど
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
    default-jre \
    locales-all \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*


# ---------------------------------------------------
# python
# NOTE: 本来は3.9までの模様。とりあえず3.10のままにしてみる。
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
    # python3.11 \
    python3-pip

# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 && \
#     update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1


# ---------------------------------------------------
# pipを23.2.1以降にする
# lightGBM4.0.0をCUDA用にビルドするのに必要
# ※pipのバージョンが23.1.2だとビルドが途中で止まる
# ---------------------------------------------------
RUN pip install --upgrade pip==23.2.1 setuptools==68.0.0


# ---------------------------------------------------
# RAPIDS
# ref: https://docs.rapids.ai/install
# NOTE: CUDAのバージョンが微妙に一致していないがとりあえず試してみる
# ---------------------------------------------------
RUN pip install cudf-cu12 cuml-cu12 --extra-index-url=https://pypi.nvidia.com


# ---------------------------------------------------
# H2O
# NOTE: H2O Flowはあらかじめzip解凍してフォルダに配置
# ---------------------------------------------------
RUN pip install H2O


# ---------------------------------------------------
# lightGBM
# NOTE:
#   公式ドキュメントを見るとLightGBMのGPU対応は特に言及ないが、
#   一応GPU版を入れてみる
# ---------------------------------------------------
RUN pip uninstall -y lightgbm && \
    pip install lightgbm==4.0.0 --no-binary lightgbm --no-cache lightgbm --config-settings=cmake.define.USE_CUDA=ON


# ---------------------------------------------------
# ロケール
# ---------------------------------------------------
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ=Asia/Tokyo


# ---------------------------------------------------
# デフォルト実行
# ---------------------------------------------------
# CMD [ "java", "-jar", "/workspace/dev_h2o/h2o-3.42.0.2/h2o.jar", "-ip", "localhost" ]
