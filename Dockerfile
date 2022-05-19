FROM python:3.9.13-alpine3.15

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pymysql
ENV USER_MAIL "usermail"
ENV PASS_MAIL "password"
ENV MYSQL_HOST "host"
ENV MYSQL_USER "userdb"
ENV MYSQL_PASSWORD "passdb"
ENV MYSQL_DB "db"
ENV MYSQL_PORT 3306
ENTRYPOINT python3 main.py

