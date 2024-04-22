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
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Исполнитель",
        related_name="executor",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        constraints = (
            UniqueConstraint(
                fields=("title", "customer"), name="uniq_title_customer"
            ),
        )
