FROM python:3.7.7-buster

ENV AIRFLOW_HOME airflow
# Install necessary  packages and airflow
RUN apt-get update -yqq
RUN apt-get upgrade -yqq

RUN pip install pymysql

RUN pip install apache-airflow[celery,mysql,redis]

# default image does not have jsii installed but it is neededs
RUN pip install jsii

# Create airflow group to link host folder permission to container users
RUN groupadd -g 4545 airflow

# Crete airflow user to run airflow
RUN useradd -g 4545 airflow

# Create home folder for airflow
RUN mkdir /airflow

#RUN airflow initdb

# Make airflow user owner of airflow folder
RUN chown -R :airflow /airflow/

RUN chmod -R 770 /airflow/
