from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты")

    phone = models.CharField(
        max_length=35, verbose_name="Номер телефона", blank=True, null=True
    )
    tg_name = models.CharField(
        max_length=50, verbose_name="Имя в Телеграм", blank=True, null=True
    )
    country = models.CharField(
        max_length=50, verbose_name="Country", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Фотография профиля",
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
