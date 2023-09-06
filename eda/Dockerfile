FROM my_app_base


# ---------------------------------------------------
# PyCario用依存パッケージ
# ---------------------------------------------------
RUN apt update \
    && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*


# ---------------------------------------------------
# sweetviz Autoviz ydata-profiling
#
# Note:
# ydata-profiling = 旧pandas-profiling
# ---------------------------------------------------
COPY ./eda/requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
