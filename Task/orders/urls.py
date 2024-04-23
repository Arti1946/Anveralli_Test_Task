from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("orders_list/", views.orders_list, name="orders_list"),
    path("detail/<int:order_id>", views.order_detail, name="order_detail"),
    path("order_create/", views.order_create, name="order_create"),
    path("lk/", views.lk_orders_list, name="lk"),
    path(
        "detail/<int:order_id>/choose_executor/<responser_id>/",
        views.choose_executor,
        name="choose_executor",
    ),
    path(
        "detail/<int:order_id>/reply_order/",
        views.reply_order,
        name="reply_order",
    ),
    path("lk/responses/", views.responses, name="responses"),
]
