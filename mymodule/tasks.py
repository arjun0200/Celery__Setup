import os, sys
from celery import Celery, group


app = Celery('tasks')

app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend = 'redis://localhost:6379/0',
    CELERY_TASK_DEFAULT_QUEUE = "default",
    result_expires=10,
    broker_connection_retry_on_startup = True,
    accept_content = ['json']
)

app.conf.broker_transport_options = {
    'retry_policy': {
       'timeout': 2.0
    }
}
app.conf.result_backend_transport_options = {
    'retry_policy': {
       'timeout': 2.0
    }
}


@app.task
def sum1(value):
    if value<=0:
        return 0
    return value + sum1(value-1)


if __name__ == '__main__': # when celery calling name of file.py "file"
    list = [10,20,30,40,50]
    job_2 = group([sum1.s(strat) for strat in list])
    results_2 = job_2.apply_async()
    app.worker_main(["worker", '--loglevel=INFO', '--include=tasks', '--concurrency=20']) #direct calling from program