from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = PhoneNumberField(null=True, blank=True, unique=True, verbose_name='номер телефона')
    # phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True,
    #                          help_text='Введите номер телефона')

    tg_name = models.CharField(max_length=50, verbose_name='ник в телеграм', null=True, blank=True,
                               help_text='Введите ник в телеграм')
    avatar = models.ImageField(upload_to='users_alt/avatars/', verbose_name='аватар', null=True, blank=True,
                               help_text='Загрузите аватарку')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f"{self.email}"