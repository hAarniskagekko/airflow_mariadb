from datetime import timedelta

# [START import_module]
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    'perf_test',
    default_args=default_args,
    description='DAG to compare local and celery executor copncurrency',
    schedule_interval=None
)

short_task_1a = BashOperator(
    task_id='short1a',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

short_task_1b = BashOperator(
    task_id='short1b',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

short_task_1c = BashOperator(
    task_id='short1c',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

short_task_1d = BashOperator(
    task_id='short1d',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

mid_task_1a = BashOperator(
    task_id='mid1a',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_1b = BashOperator(
    task_id='midb',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_1c = BashOperator(
    task_id='mid1c',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_1d = BashOperator(
    task_id='mid1b',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_1e = BashOperator(
    task_id='mid1e',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

long_task_1a = BashOperator(
    task_id='long1a',
    depends_on_past=False,
    bash_command='sleep 180',
    retries=3,
    dag=dag,
)

long_task_1b = BashOperator(
    task_id='long1b',
    depends_on_past=False,
    bash_command='sleep 180',
    retries=3,
    dag=dag,
)

dummy_1 = DummyOperator(
    task_id='dummy1',
    dag=dag
)

short_task_2a = BashOperator(
    task_id='short2a',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

short_task_2b = BashOperator(
    task_id='short2b',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

short_task_2c = BashOperator(
    task_id='short2c',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

short_task_2d = BashOperator(
    task_id='short2d',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

mid_task_2a = BashOperator(
    task_id='mid2a',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_2b = BashOperator(
    task_id='mid2b',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_2c = BashOperator(
    task_id='mid2c',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_2d = BashOperator(
    task_id='mid2b',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

mid_task_2e = BashOperator(
    task_id='mid2e',
    depends_on_past=False,
    bash_command='sleep 25',
    retries=3,
    dag=dag,
)

long_task_2a = BashOperator(
    task_id='long2a',
    depends_on_past=False,
    bash_command='sleep 180',
    retries=3,
    dag=dag,
)

long_task_2b = BashOperator(
    task_id='long2b',
    depends_on_past=False,
    bash_command='sleep 180',
    retries=3,
    dag=dag,
)

dummy_2 = DummyOperator(
    task_id='dummy2',
    dag=dag
)

#Task deps
short_task_1a >> dummy_1
short_task_1b >> dummy_1
short_task_1c >> dummy_1
short_task_1d >> dummy_1
mid_task_1a >> dummy_1
mid_task_1b >> dummy_1
mid_task_1c >> dummy_1
mid_task_1d >> dummy_1
mid_task_1e >> dummy_1
long_task_1a >> dummy_1
long_task_1b >> dummy_1

dummy_1 >> short_task_2a
dummy_1 >> short_task_2b
dummy_1 >> short_task_2c
dummy_1 >> short_task_2d
dummy_1 >> mid_task_2a
dummy_1 >> mid_task_2b
dummy_1 >> mid_task_2c
dummy_1 >> mid_task_2d
dummy_1 >> mid_task_2e
dummy_1 >> long_task_2a
dummy_1 >> long_task_2b

short_task_2a >> dummy_2
short_task_2b >> dummy_2
short_task_2c >> dummy_2
short_task_2d >> dummy_2
mid_task_2a >> dummy_2
mid_task_2b >> dummy_2
mid_task_2c >> dummy_2
mid_task_2d >> dummy_2
mid_task_2e >> dummy_2
long_task_2a >> dummy_2
long_task_2b >> dummy_2
