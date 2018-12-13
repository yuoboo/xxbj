from celery import shared_task
from celerys import app


@shared_task
def add(x, y):
    return x+y


@shared_task
def max(x, y):
    return max(x, y)
