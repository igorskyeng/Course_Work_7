from django.contrib import admin
from habits.models import Habits, PleasantHabit
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'avatar', 'phone')
    list_filter = ('email',)
    search_fields = ('country', 'phone')


@admin.register(PleasantHabit)
class PleasantHabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'time', 'action', 'time_to_complete', 'publication_sign')
    list_filter = ('time',)
    search_fields = ('place', 'action')


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place', 'time', 'action', 'sign_pleasant_habit', 'related_habit', 'frequency',
                    'reward', 'time_to_complete', 'publication_sign')
    list_filter = ('user',)
    search_fields = ('place', 'action')
