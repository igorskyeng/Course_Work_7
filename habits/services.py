from config import settings

from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import PeriodicTask


def create_reminder(habit):
    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_week='*' if habit.frequency == 'Раз в день' else '*/7',
        month_of_year='*',
        timezone=settings.TIME_ZONE
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'Habit task - {habit.action}',
        task='habits.tasks.send_telebot',
        args=[habit.id],
    )


def delete_reminder(habit):
    task_name = f'send_telebot{habit.id}'
    PeriodicTask.objects.filter(name=task_name).delete()


def update_reminder(habit):
    delete_reminder(habit)
    create_reminder(habit)
