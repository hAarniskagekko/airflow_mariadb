FROM python:3.7.7-buster

ENV AIRFLOW_HOME airflow
# Install necessary  packages and airflow
RUN apt-get update -yqq
RUN apt-get upgrade -yqq

RUN pip install pymysql

RUN pip install apache-airflow[celery,mysql,redis]

# default image does not have jsii installed but it is neededs
RUN pip install jsii

# Crete airflow user to run airflow
RUN useradd airflow

# Create home folder for airflow
RUN mkdir /airflow

# Make airflow user owner of airflow folder
RUN chown -R airflow:airflow /airflow/
