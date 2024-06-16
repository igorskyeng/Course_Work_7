from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsCreateAPIView, HabitsListAPIView, HabitsRetrieveAPIView,
                          HabitsUpdateAPIView, HabitsDestroyAPIView)


app_name = HabitsConfig.name


urlpatterns = [
    path('habits/create/', HabitsCreateAPIView.as_view(), name='habits_create'),
    path('habits/', HabitsListAPIView.as_view(), name='habits_list'),
    path('habits/<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habits_get'),
    path('habits/update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habits_update'),
    path('habits/delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habits_delete'),
]
