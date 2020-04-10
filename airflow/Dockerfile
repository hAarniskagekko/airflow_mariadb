FROM python:3.8-buster

ENV AIRFLOW_HOME airflow
# Install necessary  packages and airflow
RUN apt-get update -yqq
RUN apt-get upgrade -yqq

RUN pip install apache-airflow[celery,mysql,redis]

# default image does not have jsii installed but it is neededs
RUN pip install jsii

# Copy Airflow configuration to airlfow home folder in container

COPY airflow.cfg /airflow/

RUN airflow initdb

RUN airflow webserver
