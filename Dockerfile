# python:3.9をベースとする
FROM python:3.9

ENV PROJECT_DIR measuring-time-game

# 作業ディレクトリの設定
WORKDIR ${PROJECT_DIR}

# ADD requirements.txt /${PROJECT_DIR}/

# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
ADD . /${PROJECT_DIR}/

# aptリポジトリをアップデート　＆　必要なソフトウェアをインストール
RUN apt update && apt install -y sqlite3 vim less
# pipをupgradeする
RUN pip install --upgrade pip
# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install --no-cache-dir -r requirements.txt



# RUN cd $PROJECT_NAME

# ローカルサーバーでの起動
# CMD python3 $WORKDIR/$PROJECT_NAME/manage.py runserver 0.0.0.0:8000
CMD /bin/bash