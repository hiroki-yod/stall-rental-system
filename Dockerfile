# ベースイメージ
FROM python:3.12

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを設定
RUN mkdir /code
WORKDIR /code

# pipenvをインストール
RUN pip install --upgrade pip && \
    pip install pipenv

# Pipfileをコピー
COPY Pipfile Pipfile.lock /code/

# 依存関係をインストール
RUN pipenv install --system --deploy

# プロジェクトファイルをコピー
COPY . /code/
