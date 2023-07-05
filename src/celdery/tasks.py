from .celery import app
from .red import r


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def sleep(numbers):
    with r.lock("task_lock"):
        import time

        time.sleep(numbers)
