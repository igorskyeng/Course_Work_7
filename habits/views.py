from rest_framework import generics

from habits.serliazers import HabitsSerializers
from habits.models import Habits


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()

    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.user = self.request.user
        new_habits.save()


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()


class HabitsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
