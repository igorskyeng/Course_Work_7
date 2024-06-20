from rest_framework import serializers

from habits.models import Habits
from habits.validators import HabitsValidator


class HabitsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'
        validators = [HabitsValidator(field='time_to_complete')]
