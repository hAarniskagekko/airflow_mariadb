# airflow_mariadb

This repository contains the files needed to run Airflow with celery executor with Docker compose.

What to configure after pulling this repository:
- define mounting volumes for airflow dags and logs and for mariadb database files
- Add airflow container group as owner for the hosts directories of dags and logs files. THE gid OF HOST MACHINE MUST MATCH THE CONTAINERS gid! (4545 as default)
- Add .env files to airflow and mariadb directories as they are described in their respective directory README.md files

When running dokcer-compose up for the first time airflow containers will fail because mariadb has not set up airfow db yet. Just rerun dokcer-compose up and it should be fine.

To do:
- make airlfow containers retry mariadb connection. Now airflow contianers fail the first time running docker-compose up because mariadb container takes some time to set up airlfow database.
- Make docker-compose command for redis set bind and password for it
- Make airflow web UI require authentication
- Make airflow initdb be part of some script. Now it needs to be ran manaually the first time
- fix airflow container jsii install error (probably by using older version)
- change airflow container to use alpine linux
- fix mariadb "Aborted connection" warnings
