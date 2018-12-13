import sys
from celery import Celery
from _Config import Config

app = Celery("test")
app.config_from_object(Config)

# app.autodiscover_tasks()
