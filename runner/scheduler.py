import random
import time

from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from runner.tasks import test_task

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@register_job(scheduler, "interval", seconds=5, replace_existing=True)
def test_job():
    test_task()


register_events(scheduler)

scheduler.start()
print("Scheduler started!")