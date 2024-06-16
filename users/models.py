from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)

    USERNAME_FIELD = "email"
    username = USERNAME_FIELD
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
