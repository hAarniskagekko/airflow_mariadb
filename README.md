# airflow_mariadb

This repository contains the files needed to run Airflow with celery executor with Docker compose.

What to configure afeter pulling this repository:
- define mounting volumes for airflow dags and logs and for mariadb database filesystem
- Add airflow container user as owner for the host directories of dags and logs files
- Add .env files to airflow and mariadb directories as they are described in the respective directory README.md files

To do:
- figure out how to keep airflow scheduler running after docker-compose up
- add password for redis
- cleanup example dags from airflow
- fix airflow container jsii install error (probably by using older version)
- change airflow container to use alpine linux
- fix mariadb "Abosted connection" warnings
