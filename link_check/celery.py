from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "link_check.settings")
app = Celery("link_check")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'schedule-link-check': {
        'task': 'schedule_link_check',
        'schedule': 60,
    },
}
