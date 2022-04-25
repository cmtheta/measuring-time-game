FROM python:3.9

ENV PROJECT_DIR measuring-time-game

# ワークディレクトリの設定
WORKDIR ${PROJECT_DIR}
ADD . /${PROJECT_DIR}  

# アップデート ＆ 必要なソフトウェアをインストール
RUN apt update && apt install -y sqlite3 vim less
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# データベースのマイグレーションを行う
RUN python /${PROJECT_DIR}/measuring_time_game/manage.py makemigrations
RUN python /${PROJECT_DIR}/measuring_time_game/manage.py migrate

# ローカルサーバーでの起動
CMD python3 /${PROJECT_DIR}/measuring_time_game/manage.py runserver 0.0.0.0:8000