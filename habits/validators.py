from datetime import timedelta

from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = timedelta(minutes=2)
        time_to_complete = value.get(self.field)

        reward = value.get('reward')
        related_habit = value.get('related_habit')
        sign_pleasant_habit = value.get('sign_pleasant_habit')

        if reward and related_habit:
            raise serializers.ValidationError('Нельзя выбрать одновременный связанную привычку и вознаграждение.')

        if time_to_complete > time:
            raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд.')

        if related_habit and not related_habit.sign_pleasant_habit:
            raise serializers.ValidationError('В связанные привычки могут попадать только привычки с '
                                              'признаком приятной привычки.')

        if sign_pleasant_habit and (reward or related_habit):
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или '
                                              'связанной привычки.')
