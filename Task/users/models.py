from core.roles import Role
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField("Почта", unique=True, max_length=254)
    password = models.CharField(
        "Пароль", max_length=150, blank=False, null=False
    )
    role = models.CharField(
        choices=Role, blank=False, null=False, verbose_name="Роль"
    )
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    experience = models.TextField("Опыт")
    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
