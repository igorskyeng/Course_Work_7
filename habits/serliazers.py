from rest_framework import serializers

from habits.models import Habits


class HabitsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'
