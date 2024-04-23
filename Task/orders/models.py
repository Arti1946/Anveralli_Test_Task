from typing import NamedTuple

from django.db import models
from django.db.models import UniqueConstraint

from users.models import CustomUser


class Order(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Заказчик",
        related_name="customer",
    )
    responses = models.ManyToManyField(
        CustomUser,
        through="OrdersResponses",
        related_name="responses",
        verbose_name="Отклики",
    )

    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        verbose_name="Исполнитель",
        related_name="executor",
        null=True,
        blank=True,
    )

    class Meta:
        constraints = (
            UniqueConstraint(
                fields=("title", "customer"), name="uniq_title_customer"
            ),
        )
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.title


class OrdersResponses(models.Model):
    orders = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="orders_responses",
        verbose_name="Заказы",
    )
    responses = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="orders_responses",
        verbose_name="Отклики",
    )

    class Meta:
        verbose_name = "Заказ с откликом"
        verbose_name_plural = "Заказы с откликами"

    def __str__(self):
        return self.responses.username
