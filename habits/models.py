from datetime import datetime

from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class PleasantHabit(models.Model):

    place = models.CharField(max_length=150, verbose_name='Место привычки')
    time = models.DateTimeField(default=datetime.now(), verbose_name='Время привычки')
    action = models.CharField(max_length=150, verbose_name='Действие привычки')
    time_to_complete = models.DateTimeField(default=datetime.now(), verbose_name='Время на выполнение')
    publication_sign = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'
        ordering = ('id',)


class Habits(models.Model):

    class PeriodHabits(models.TextChoices):
        ONE_DAY = "Раз в день", "Раз в день"
        ONE_WEEK = "Раз в неделю", "Раз в неделю"
        ONE_MONTH = "Раз в месяц", "Раз в месяц"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место привычки')
    time = models.DateTimeField(default=datetime.now(), verbose_name='Время привычки')
    action = models.CharField(max_length=150, verbose_name='Действие привычки')
    sign_pleasant_habit = models.BooleanField(default=True, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey(PleasantHabit, on_delete=models.CASCADE,
                                      verbose_name='Связанная привычка', **NULLABLE)
    frequency = models.CharField(max_length=50, default=PeriodHabits.ONE_DAY,
                                 choices=PeriodHabits, verbose_name='Периодичность рассылки')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение')
    time_to_complete = models.DateTimeField(default=datetime.now(), verbose_name='Время на выполнение')
    publication_sign = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('id',)
