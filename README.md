# MLVSCodeDevcontainerWithMLflow

## 概要

機械学習用Pythonコード開発のための関連コンテナ一式をまとめたもの。

- 機械学習実行環境
    - Python3.11
    - CUDA/cuDNN
    - VSCode Devcontainer + common-utils
- MLflow
- DB
    - Postgres
    - pgAdmin
- Artifact
    - pure-ftpd

### 参考

- MLflow
    - GitHubリポジトリ
        - https://github.com/c60evaporator/mlflow_tutorials/tree/master
    - Qiita: MLflowの環境構築方法まとめ【Docker, S3】#シナリオ3: MLflow on localhost with Tracking Server
        - https://qiita.com/c60evaporator/items/e1fd57a0263a19b629d1#%E3%82%B7%E3%83%8A%E3%83%AA%E3%82%AA3-mlflow-on-localhost-with-tracking-server
- VSCode DevContainer
    - 以下参考
    - https://qiita.com/kaazzo/items/b1daa742ada89f04a130#docker-compose%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88
    - https://zenn.dev/saboyutaka/articles/9cffc8d14c6684
        - https://github.com/saboyutaka/ruby27-rails61-devcontainer

## 使い方

1. ターミナル等で以下実行
    ```
    git clone https://github.com/iuill/MLVSCodeDevcontainerWithMLflow.git
    cd MLVSCodeDevcontainerWithMLflow
    cp .env.sample .env
    ```
1. .envファイル内のHOST_IPを変更
1. ターミナル等で以下実行
    ```
    docker-compose up -d --build
    ```
1. VSCodeでフォルダを開く
1. VSCode左下の `><` をクリックし `コンテナーで再度開く` を実行
1. VSCode左下が `開発コンテナー: app` になることを確認

## ライセンス

ご参考

Qiita: ライセンスをつけないとどうなるの？#no license in github
https://qiita.com/Tatamo/items/ae7bf4878abcf0584291#no-license-in-github

