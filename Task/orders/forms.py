from django import forms

from .models import Order, OrdersResponses
from users.models import CustomUser


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("title", "description", "price")


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ("executor",)
