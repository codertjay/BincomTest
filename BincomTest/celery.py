import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BincomTest.settings')
# TODO: ADD TO ENV VARIABLE
BROKER_URL = 'RABBITMQL'

app = Celery('BincomTest')
# used redis broker if it exists
if BROKER_URL == 'REDIS':
    app = Celery('BincomTest', broker_url='redis://127.0.0.1:6379/0')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
