FROM python:3.7.7-buster

ENV AIRFLOW_HOME airflow
# Install necessary  packages and airflow
RUN apt-get update -yqq
RUN apt-get upgrade -yqq

RUN pip install pymysql

RUN pip install apache-airflow[celery,mysql,redis]

# default image does not have jsii installed but it is neededs
RUN pip install jsii

COPY airflow.cfg /airflow/

COPY start_airflow.sh /airflow/
# Copy Airflow configuration to airlfow home folder in container

RUN useradd airflow

RUN chown -R airflow:airflow /airflow/
