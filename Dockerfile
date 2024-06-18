FROM python:3.10.14-slim-bullseye
RUN pip install psycopg2-binary
RUN pip install mysql-connector-python