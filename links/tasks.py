import datetime
from celery import shared_task
from django.utils.timezone import now
from link_check.celery import app
from links.models import Links
from links.services import status_check_service
from links.utils import chunk


@shared_task(name="schedule_link_check")
def schedule_link_check():
    current_timestamp = now()
    link_ids = []

    for link in Links.objects.filter(paused=False):
        should_check = (link.refresh_interval == 0) or \
                       (link.updated_at + datetime.timedelta(seconds=link.refresh_interval) <= current_timestamp)

        if should_check:
            link_ids.append(link.id)

    for link_ids_group in chunk(link_ids, 10):
        link_check.delay(args=link_ids_group)


@app.task
def link_check(args):
    new_links = []

    for link in Links.objects.filter(id__in=args):
        status = status_check_service.call(url=link.link)
        link.status = status

        new_links.append(link)

    Links.objects.bulk_update(new_links, ['status'])
