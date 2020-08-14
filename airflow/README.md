## Put airflow.env file here.

This direcotry contains the definition for both airflow webserver/scheduler and the workers.

start_airflow.sh is only run in airflow web container.

Following env variables required:
```
# ENV variables for airflow containers

# [Core]
# Folder where the dags can be found.
AIRFLOW__CORE__DAGS_FOLDER=/airflow/dags
# Folder for airflow logs
AIRFLOW__CORE__BASE_LOG_FOLDER=/airflow//logs
# set airflow executor
AIRFLOW__CORE__EXECUTOR=CeleryExecutor
# Connection string to airflows database.
#It looks something like this: mysql+pymysql://airflow:PASSWORD@database:3306/airflow
AIRFLOW__CORE__SQL_ALCHEMY_CONN=
# Default value is 5. Limits the number of connections airflows tasks can make to a target database.
AIRFLOW__CORE__SQL_ALCHEMY_POOL_SIZE=5
# Limits the maximum number of tasks that can be running simultaneously for all workers combined (or how many tasks the scehduler will manage simultaneously).
AIRFLOW__CORE__PARALLELISM=16
# Limits the number of tasks that can be running inside single dag.
AIRFLOW__CORE__DAG_CONCURRENCY=16
# Let's not load airflows example dags...
AIRFLOW__CORE__LOAD_EXAMPLES=False
# Nor should we load unnecessary airflow default connections...
AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS=False
# Secret that saves airflow connection passwords.
#Make a good one. Like this for example: https://bcb.github.io/airflow/fernet-key
AIRFLOW__CORE__FERNET_KEY=

# [Webserver]
# Ip address of airflow webserver. Should propably match the container ip address,
AIRFLOW__WEBSERVER__WEB_SERVER_HOST=173.17.0.10
# Port that the webserver uses.
AIRFLOW__WEBSERVER__WEB_SERVER_PORT=8000

# [Celery]
# Limits the nuber of tasks that single worker instance can run.
AIRFLOW__CELERY__WORKER_CONCURRENCY=8
# Connection string to redis.
#Connection sting looks something like this: redis://:PASSWORD@redis:6379/0
AIRFLOW__CELERY__BROKER_URL=
# Connection string to celery result backend. This is the same as AIRFLOW__CORE__SQL_ALCHEMY_CONN but for celery executor.
#It looks something like this: db+mysql://airflow:PASSWORD@database:3306/airflow
AIRFLOW__CELERY__RESULT_BACKEND=
```
