## Put airflow.env file here.

This direcotry contains the definition for both airflow webserver/scheduler and the workers.

start_airflow.sh is only run in airflow web container.

Following env variables required:
```
#Home folder for airflow in container
AIRFLOW_HOME=/airflow
#Database password for airflow user
AIRFLOW_PASSWD=
```
