FROM my_app_base


# ---------------------------------------------------
# AutoGluon
#   fit_summary()でplotする場合はbokehが必要
# ---------------------------------------------------
RUN pip install autogluon bokeh


# ---------------------------------------------------
# lightGBM
# NOTE:
#   公式ドキュメントを見るとLightGBM4.0.0 CUDA対応版への言及なし
#   -> 4.0.0だとCUDA版/GPU版いずれもAutoGluon0.8.2は正常動作しない模様なので、ダウングレードする
# ---------------------------------------------------
RUN pip uninstall -y lightgbm && \
    # pip install lightgbm==4.0.0 --no-binary lightgbm --no-cache lightgbm --config-settings=cmake.define.USE_CUDA=ON
    pip install lightgbm==3.3.5
