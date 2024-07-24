# ベースイメージ
FROM python:3.11

# 環境変数を設定
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# 作業ディレクトリを設定
RUN mkdir /code
WORKDIR /code

# pipenvをインストール
RUN pip install --upgrade pip && \
    pip install pipenv

# Pipfileをコピー
COPY ./code/Pipfile /code/Pipfile
COPY ./code/Pipfile.lock /code/Pipfile.lock

# 依存関係をインストール
RUN pipenv install --system --deploy

# プロジェクトファイルをコピー
COPY . /code/
