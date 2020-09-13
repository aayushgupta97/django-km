import requests
from celery.schedules import crontab
from celery import shared_task
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from datetime import timedelta
from .models import StateWiseData, CaseTimeSeries
from datetime import datetime

logger = get_task_logger(__name__)


@shared_task
def test_celery_worker():
    print("Celery Workers are working fine.")


# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def task_example():
    logger.info("Task started")
    logger.info("Task finished")


# run_every takes a timedelta object.
# A periodic task that will run every 10 seconds
@periodic_task(run_every=timedelta(seconds=10))
def task_example_timedelta():
    logger.info("Task started")
    logger.info("Task finished")


@periodic_task(run_every=timedelta(hours=12))
def task_state_data_fetch():
    logger.info("Task started: State data fetch from api.covid19")
    r = requests.get("https://api.covid19india.org/data.json")
    data = r.json()['statewise']
    for item in data:
        StateWiseData.objects.update_or_create(code=item['statecode'],
                                               name=item['state'],
                                               active=item['active'],
                                               confirmed=item['confirmed'],
                                               deaths=item['deaths'],
                                               recovered=item['recovered'])

    logger.info("Task finished")


@periodic_task(run_every=(crontab(hour="0", minute="55", day_of_week="*")))
def task_cases_time_series():
    r = requests.get("https://api.covid19india.org/data.json")
    data = r.json()['cases_time_series']
    for item in data:
        t = item['date'].rstrip() + " 2020"
        date = datetime.strptime(t, "%d %B %Y").date()
        CaseTimeSeries.objects.update_or_create(date=date,
                                                defaults={"daily_confirmed": item['dailyconfirmed'],
                                                          "daily_recovered": item['dailyrecovered'],
                                                          "daily_deceased": item['dailydeceased'],
                                                          "total_confirmed": item['totalconfirmed'],
                                                          "total_recovered": item['totalrecovered'],
                                                          "total_deceased": item['totaldeceased']}
                                                )
