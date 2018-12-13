import tasks
from celery import current_app


for n in current_app.tasks:
    print n

print current_app.loader.import_default_modules()
