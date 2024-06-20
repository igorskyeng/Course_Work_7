from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serliazers import HabitsSerializers
from habits.models import Habits


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.user = self.request.user
        new_habits.save()


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializers()
    permission_classes = [IsAuthenticated & IsOwner]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)


class HabitsPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializers()
    permission_classes = [IsAuthenticated & IsOwner]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        return Habits.objects.filter(publication_sign=True)


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]


class HabitsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]
