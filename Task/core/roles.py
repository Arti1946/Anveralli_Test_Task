from django.db import models


class Role(models.TextChoices):
    CUSTOMER = "Заказчик"
    EXECUTOR = "Исполнитель"
