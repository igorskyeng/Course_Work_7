from celery import shared_task
from config.settings import TELEGRAM_API, TELEGRAM_CHAT_ID
from habits.models import Habits
import requests


@shared_task
def send_telebot(pk):
    habit = Habits.objects.get(pk=pk)

    message = (f'Время выполнить привычку: "{habit.action}" в '
               f'{habit.time.strftime("%H:%M")}, в {habit.place}.')

    params = {
        'text': message,
        'chat_id': TELEGRAM_CHAT_ID
    }

    requests.get(f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage', params=params)
