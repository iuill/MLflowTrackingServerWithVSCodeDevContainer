FROM my_app_base


# ---------------------------------------------------
# H2O
# NOTE: H2O Flowはあらかじめzip解凍してフォルダに配置
# ---------------------------------------------------
RUN apt update \
    && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
    default-jre \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*
RUN pip install H2O
