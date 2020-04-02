from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawlweb.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

from django.conf import settings

app = Celery('crawlweb', broker='redis://127.0.0.1:6379/0')

app.config_from_object('django.conf:settings',namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

